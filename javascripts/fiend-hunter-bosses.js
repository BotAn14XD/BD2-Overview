// ---------------------------------------------------------------------------
// Boss data
// ---------------------------------------------------------------------------
let BOSSES = [];
let SORTED_BOSSES = [];

// Path to the boss data file, resolved from the site root. Adjust this if
// you move fiend-hunter-bosses.json elsewhere in your docs/ folder.
const DATA_SRC = "/BD2-Overview/assets/data/fiend-hunter-bosses.json";

async function loadBosses() {
  const res = await fetch(DATA_SRC);
  if (!res.ok) throw new Error('Failed to load boss data: ' + res.status);
  BOSSES = await res.json();
  SORTED_BOSSES = [...BOSSES].sort((a, b) => b.season - a.season);
}

const PROPERTY_COLORS = {
  Fire:     '#ff7a52',
  Water:    '#4aa8ff',
  Wind:     '#5fd98a',
  Light:    '#f2cf5b',
  Darkness: '#b48bff'
};

function hexToRgba(hex, alpha) {
  const clean = hex.replace('#', '');
  const r = parseInt(clean.substring(0, 2), 16);
  const g = parseInt(clean.substring(2, 4), 16);
  const b = parseInt(clean.substring(4, 6), 16);
  return 'rgba(' + r + ',' + g + ',' + b + ',' + alpha + ')';
}

// ---------------------------------------------------------------------------
// Stat math
// ---------------------------------------------------------------------------
function statMultiplier(level, rate, slope, ratio = 1) {
  const val = 1 + (level - 1) * rate * 0.01 * Math.pow(level, slope) * ratio;
  return Math.max(1, val);
}

function stageRatioFor(level, s2Level, s2Ratio, s3Level, s3Ratio) {
  if (level <= s2Level) return 1;
  if (level <= s3Level) return s2Ratio;
  return s3Ratio;
}

// Rounds to the nearest integer, with .5 rounding down instead of up.
function roundHalfDown(x) {
  return Math.ceil(x - 0.5);
}

// Truncates to 3 significant figures without reintroducing floating-point
// noise. Uses the shortest round-trip exponential form of the number (rather
// than a fixed-digit one) so trailing float error like ...999999997 never
// gets rounded up into the digits we keep.
function floorToSigFigs(x, figs) {
  if (x === 0) return 0;
  const sign = Math.sign(x);
  x = Math.abs(x);
  const [mantissaStr, expPart] = x.toExponential().split('e');
  const e = parseInt(expPart, 10);
  let digits = mantissaStr.replace('.', '');
  digits = (digits + '0'.repeat(figs)).slice(0, figs);
  const decimals = Math.max(0, (figs - 1) - e);
  if (decimals === 0) {
    return sign * parseInt(digits, 10) * Math.pow(10, e - (figs - 1));
  }
  const value = parseInt(digits, 10) / Math.pow(10, decimals);
  return sign * Number(value.toFixed(decimals));
}

function computeStat(level, statBlock, s2Level, s2Ratio, s3Level, s3Ratio, defaultMode) {
  const { base, rate, slope, roundingMode } = statBlock;
  const ratio = stageRatioFor(level, s2Level, s2Ratio, s3Level, s3Ratio);
  const mult = statMultiplier(level, rate, slope, ratio);
  const raw = base * 1.1 * mult;
  const mode = roundingMode || defaultMode || 'sig3fig';
  return mode === 'integer' ? roundHalfDown(raw) : floorToSigFigs(raw, 3);
}

function getAtkBlock(boss) {
  if (boss.ATK) return { block: boss.ATK, label: 'ATK' };
  if (boss.MATK) return { block: boss.MATK, label: 'MATK' };
  return null;
}

function formatNumber(n) {
  return n.toLocaleString('en-US', { maximumFractionDigits: 6 });
}

function formatDate(iso) {
  const d = new Date(iso + 'T00:00:00');
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

function formatDateShort(iso) {
  const d = new Date(iso + 'T00:00:00');
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

// ---------------------------------------------------------------------------
// Threshold: minimum sustained daily damage to clear each level's HP pool
// by its own day, attacking once per day starting day 1, plus one bonus
// attack on any day a kill is scored. Uses BigInt because some bosses'
// HP at high levels exceeds Number.MAX_SAFE_INTEGER.
// ---------------------------------------------------------------------------
function ceilDivBig(a, b) {
  return (a + b - 1n) / b;
}

// hpSeries: plain-number HP values for levels 1..L, in order.
// eventDays: the boss's actual event length in calendar days (fixed per
// boss). Budget = eventDays + N - 1 attacks: one attack per real day of the
// event, plus one bonus attack for each level (except the last) that gets
// carried straight into the next one.
function minSustainedDamage(hpSeries, eventDays) {
  const N = hpSeries.length;
  if (N === 0) return 0n;
  const P = hpSeries.map(v => BigInt(Math.round(v)));
  const allowed = BigInt(eventDays + N - 1);
  let maxP = 0n;
  for (const p of P) if (p > maxP) maxP = p;
  if (maxP === 0n) return 0n;

  let lo = 1n, hi = maxP;
  while (lo < hi) {
    const mid = (lo + hi) / 2n;
    let sum = 0n;
    for (let i = 0; i < N; i++) {
      sum += ceilDivBig(P[i], mid);
      if (sum > allowed) break;
    }
    if (sum <= allowed) hi = mid; else lo = mid + 1n;
  }
  return lo;
}

// Inclusive day count between two ISO dates, e.g. Aug 20 - Aug 26 = 7 days.
function eventDayCount(dateStart, dateEnd) {
  const start = new Date(dateStart + 'T00:00:00');
  const end = new Date(dateEnd + 'T00:00:00');
  return Math.round((end - start) / 86400000) + 1;
}

// ---------------------------------------------------------------------------
// Elements
// ---------------------------------------------------------------------------
async function init() {
  const calcContainer = document.querySelector('.fh-calc');
  if (!calcContainer) return;

  try {
    await loadBosses();
  } catch (err) {
    console.error(err);
    const placeholder = document.getElementById('placeholder');
    if (placeholder) {
      placeholder.textContent = 'Could not load boss data. Check that fiend-hunter-bosses.json is next to this page.';
    }
    return;
  }


const input = document.getElementById('search-input');
const dropdown = document.getElementById('dropdown');
const placeholder = document.getElementById('placeholder');
const card = document.getElementById('card');
const maxLevelInput = document.getElementById('max-level');
const presetBtns = [...document.querySelectorAll('.preset-btn')];

let activeIndex = -1;
let currentMatches = [];
let selectedBoss = null;

  const latestChip = document.getElementById('latest-boss-chip');
  if (latestChip && SORTED_BOSSES.length > 0) {
    const latestBoss = SORTED_BOSSES[0];
    latestChip.textContent = `${latestBoss.name}`;
    latestChip.addEventListener('click', () => {
      selectBoss(latestBoss);
    });
  }


// ---------------------------------------------------------------------------
// Dropdown / search
// ---------------------------------------------------------------------------
function highlight(text, query) {
  if (!query) return text;
  const idx = text.toLowerCase().indexOf(query.toLowerCase());
  if (idx === -1) return text;
  return text.slice(0, idx) + '<mark>' + text.slice(idx, idx + query.length) + '</mark>' + text.slice(idx + query.length);
}

function matchBosses(query) {
  const q = query.trim().toLowerCase();
  if (!q) return SORTED_BOSSES;
  return SORTED_BOSSES.filter(b =>
    b.name.toLowerCase().includes(q) ||
    (b.seasonEvent || '').toLowerCase().includes(q) ||
    b.property.toLowerCase().includes(q)
  );
}

function renderDropdown(query) {
  currentMatches = matchBosses(query);
  activeIndex = -1;
  dropdown.innerHTML = '';

  if (currentMatches.length === 0) {
    const empty = document.createElement('li');
    empty.className = 'dropdown-empty';
    empty.textContent = 'No bosses match “' + query + '”.';
    dropdown.appendChild(empty);
    dropdown.hidden = false;
    input.setAttribute('aria-expanded', 'true');
    return;
  }

  currentMatches.forEach((boss, i) => {
    const li = document.createElement('li');
    li.className = 'option';
    li.id = 'option-' + i;
    li.setAttribute('role', 'option');
    li.innerHTML =
      '<span class="option-name">' + highlight(boss.name, query) + '</span>' +
      '<span class="option-meta">' + boss.property + ' · ' + formatDateShort(boss.dateStart) + '</span>';
    li.addEventListener('mousedown', (e) => {
      e.preventDefault();
      selectBoss(boss);
    });
    dropdown.appendChild(li);
  });
  dropdown.hidden = false;
  input.setAttribute('aria-expanded', 'true');
}

function updateActiveOption() {
  [...dropdown.children].forEach((el, i) => {
    if (el.classList.contains('option')) {
      el.setAttribute('aria-selected', i === activeIndex ? 'true' : 'false');
      if (i === activeIndex) el.scrollIntoView({ block: 'nearest' });
    }
  });
}

input.addEventListener('input', () => renderDropdown(input.value));
input.addEventListener('focus', () => renderDropdown(input.value));

input.addEventListener('keydown', (e) => {
  if (dropdown.hidden || currentMatches.length === 0) return;
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    activeIndex = Math.min(activeIndex + 1, currentMatches.length - 1);
    updateActiveOption();
  } else if (e.key === 'ArrowUp') {
    e.preventDefault();
    activeIndex = Math.max(activeIndex - 1, 0);
    updateActiveOption();
  } else if (e.key === 'Enter') {
    e.preventDefault();
    const pick = activeIndex >= 0 ? currentMatches[activeIndex] : currentMatches[0];
    if (pick) selectBoss(pick);
  } else if (e.key === 'Escape') {
    dropdown.hidden = true;
    input.setAttribute('aria-expanded', 'false');
  }
});

document.addEventListener('click', (e) => {
  if (!e.target.closest('.search')) {
    dropdown.hidden = true;
    input.setAttribute('aria-expanded', 'false');
  }
});

// ---------------------------------------------------------------------------
// Result card
// ---------------------------------------------------------------------------
function selectBoss(boss) {
  selectedBoss = boss;
  input.value = boss.name;
  dropdown.hidden = true;
  input.setAttribute('aria-expanded', 'false');
  placeholder.hidden = true;
  card.hidden = false;

  const subtitleParts = [];
  if (boss.seasonEvent) subtitleParts.push(boss.seasonEvent);
  subtitleParts.push(formatDate(boss.dateStart) + ' – ' + formatDate(boss.dateEnd));
  document.getElementById('card-subtitle').textContent = subtitleParts.join(' · ');
  document.getElementById('card-title').textContent = boss.name;
  document.getElementById('break-tag').hidden = !boss.isBreakSeason;

  const color = PROPERTY_COLORS[boss.property] || '#8fa0c9';
  const tag = document.getElementById('property-tag');
  tag.style.color = color;
  tag.style.background = hexToRgba(color, 0.18);
  tag.style.border = '1px solid ' + hexToRgba(color, 0.45);
  document.getElementById('property-label').textContent = boss.property;

  const atk = getAtkBlock(boss);
  document.getElementById('atk-head').textContent = atk ? atk.label : 'ATK';

  renderTable();
}

function clampLevel(n) {
  if (isNaN(n)) return 25;
  return Math.min(100, Math.max(1, n));
}

function renderTable() {
  if (!selectedBoss) return;
  const boss = selectedBoss;
  const atk = getAtkBlock(boss);
  const maxLevel = clampLevel(parseInt(maxLevelInput.value, 10) || 25);
  maxLevelInput.value = maxLevel;
  presetBtns.forEach(btn => btn.classList.toggle('is-active', Number(btn.dataset.level) === maxLevel));
  
  const tableScroll = document.getElementById('table-scroll');
  if (tableScroll) {
    tableScroll.classList.toggle('has-scroll', maxLevel > 35);
  }

  // Precompute HP for every level up to maxLevel once, since the threshold
  // for level L needs the full HP series for levels 1..L.
  const hpSeries = [];
  for (let level = 1; level <= maxLevel; level++) {
    hpSeries.push(computeStat(level, boss.HP, boss.stage2Level, boss.stage2Ratio, boss.stage3Level, boss.stage3Ratio));
  }
  const eventDays = eventDayCount(boss.dateStart, boss.dateEnd);

  const tbody = document.getElementById('table-body');
  tbody.innerHTML = '';

  for (let level = 1; level <= maxLevel; level++) {
    const hp = hpSeries[level - 1];
    const threshold = minSustainedDamage(hpSeries.slice(0, level), eventDays);
    const row = document.createElement('tr');
    
    if (level === 10 || level === 15) {
      row.classList.add('highlight-row');
    }

    let rowHtml =
      '<td>Lv. ' + level + '</td>' +
      '<td>' + formatNumber(hp) + '</td>' +
      '<td>' + threshold.toLocaleString('en-US') + '</td>';
    if (atk) {
      const atkVal = computeStat(level, atk.block, boss.stage2Level, boss.stage2Ratio, boss.stage3Level, boss.stage3Ratio, 'integer');
      rowHtml += '<td>' + formatNumber(atkVal) + '</td>';
    } else {
      rowHtml += '<td>—</td>';
    }
    row.innerHTML = rowHtml;
    tbody.appendChild(row);
  }
}

maxLevelInput.addEventListener('input', renderTable);
maxLevelInput.addEventListener('blur', renderTable);
presetBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    maxLevelInput.value = btn.dataset.level;
    renderTable();
  });
});

// ---------------------------------------------------------------------------
// Copy table
// ---------------------------------------------------------------------------
function flashButton(btn, text, cls, revertMs) {
  const label = btn.querySelector('span');
  const original = label.textContent;
  label.textContent = text;
  btn.classList.add(cls);
  setTimeout(() => {
    label.textContent = original;
    btn.classList.remove(cls);
  }, revertMs);
}

document.getElementById('copy-btn').addEventListener('click', async () => {
  const table = document.getElementById('stat-table');
  const rows = [...table.querySelectorAll('tr')];
  const tsv = rows
    .map(tr => [...tr.children].map(cell => cell.textContent.trim()).join('\t'))
    .join('\n');

  const btn = document.getElementById('copy-btn');
  try {
    await navigator.clipboard.writeText(tsv);
    flashButton(btn, 'Copied!', 'is-done', 1600);
  } catch (err) {
    const ta = document.createElement('textarea');
    ta.value = tsv;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      flashButton(btn, 'Copied!', 'is-done', 1600);
    } catch (err2) {
      flashButton(btn, 'Copy failed', 'is-error', 1600);
    }
    document.body.removeChild(ta);
  }
});

// ---------------------------------------------------------------------------
// Save image
// ---------------------------------------------------------------------------
document.getElementById('save-btn').addEventListener('click', async () => {
  const btn = document.getElementById('save-btn');
  const label = btn.querySelector('span');
  const original = label.textContent;

  if (typeof html2canvas === 'undefined') {
    flashButton(btn, 'Unavailable', 'is-error', 1800);
    return;
  }

  const originalCard = document.getElementById('card');
  const cardClone = originalCard.cloneNode(true);
  cardClone.id = '';
  cardClone.hidden = false;
  cardClone.style.margin = '0';

  // Drop the interactive controls (level input, presets, copy/save buttons) —
  // only the header and table belong in the exported image.
  const toolbarClone = cardClone.querySelector('.toolbar');
  if (toolbarClone) toolbarClone.remove();

  // Expand the scrollable table so every displayed level is captured, not
  // just whatever is currently visible in the viewport.
  const scrollClone = cardClone.querySelector('.table-scroll');
  if (scrollClone) {
    scrollClone.style.maxHeight = 'none';
    scrollClone.style.overflowY = 'visible';
  }

  // html2canvas 1.x has long-standing bugs capturing position: sticky
  // (it can mis-measure or throw mid-capture, aborting the whole export).
  // The live table uses sticky headers to stay visible while scrolling;
  // that scrolling is already removed above, so sticky isn't doing
  // anything useful for a flattened, full-height export — just dropping it
  // rather than risk the crash.
  cardClone.querySelectorAll('.stat-table thead th').forEach((th) => {
    th.style.setProperty('position', 'static', 'important');
    th.style.setProperty('top', 'auto', 'important');
  });

  // Must carry the .fh-calc class: every style rule is scoped under
  // ".fh-calc ..." for specificity safety, so without this the clone would
  // render completely unstyled once it's outside the real .fh-calc tree.
  const wrapper = document.createElement('div');
  wrapper.className = 'fh-calc';
  wrapper.style.position = 'fixed';
  wrapper.style.left = '-99999px';
  wrapper.style.top = '0';
  wrapper.style.width = originalCard.getBoundingClientRect().width + 'px';
  wrapper.appendChild(cardClone);
  document.body.appendChild(wrapper);

  // html2canvas 1.4.1 predates the modern CSS Color 4 syntax that
  // color-mix()-derived values can compute to (e.g. "rgb(91 140 255 / 0.16)"
  // instead of the legacy "rgba(91, 140, 255, 0.16)"), and its color parser
  // can choke on that silently. Several of the site's own theme tokens
  // (--bd-muted, --bd-fill-*, --bd-hairline) are color-mix-based.
  //
  // Reading ctx.fillStyle back out is NOT a safe fix — that getter's
  // serialization has evolved along with CSS Color 4 too, so it can hand
  // back the same "color(...)" function syntax that broke html2canvas in
  // the first place (confirmed: that's exactly what was happening here).
  // Instead, actually paint the pixel and read its raw bytes back via
  // getImageData, then build the rgba() string ourselves by hand. Byte
  // values out of getImageData are always plain 0-255 integers — there's
  // no color-function syntax anywhere in that path to go wrong.
  const normalizeCanvas = document.createElement('canvas');
  normalizeCanvas.width = normalizeCanvas.height = 1;
  const normalizeCtx = normalizeCanvas.getContext('2d');
  function normalizeColor(colorStr) {
    if (!colorStr) return colorStr;
    try {
      normalizeCtx.clearRect(0, 0, 1, 1);
      normalizeCtx.fillStyle = colorStr;
      normalizeCtx.fillRect(0, 0, 1, 1);
      const [r, g, b, a] = normalizeCtx.getImageData(0, 0, 1, 1).data;
      return a === 255 ? `rgb(${r}, ${g}, ${b})` : `rgba(${r}, ${g}, ${b}, ${(a / 255).toFixed(3)})`;
    } catch (e) {
      return colorStr;
    }
  }

  function flattenComputedColors(el) {
    // Map of JS (camelCase) computed-style keys to their real CSS (kebab-case)
    // property names, since CSSStyleDeclaration.setProperty() only accepts
    // the latter.
    const COLOR_PROPS = {
      color: 'color',
      backgroundColor: 'background-color',
      borderTopColor: 'border-top-color',
      borderRightColor: 'border-right-color',
      borderBottomColor: 'border-bottom-color',
      borderLeftColor: 'border-left-color'
    };
    const stack = [el];
    while (stack.length) {
      const node = stack.pop();
      if (node.nodeType !== 1) continue;
      const computed = getComputedStyle(node);
      for (const [jsProp, cssProp] of Object.entries(COLOR_PROPS)) {
        const val = computed[jsProp];
        // node.style[jsProp] = val would silently no-op here: every color/
        // background/border-color rule in this stylesheet is declared
        // !important (see header comment), and a plain (non-important)
        // inline style can never beat an !important stylesheet rule. Without
        // 'important' here, html2canvas re-resolves the cascade and still
        // sees the original, unnormalized color-mix()-derived value.
        if (val) node.style.setProperty(cssProp, normalizeColor(val), 'important');
      }
      stack.push(...node.children);
    }
  }
  flattenComputedColors(cardClone);

  label.textContent = 'Rendering…';
  try {
    const canvas = await html2canvas(cardClone, {
      backgroundColor: normalizeColor(getComputedStyle(cardClone).backgroundColor) || '#161d2e',
      scale: 2,
      useCORS: true
    });
    const link = document.createElement('a');
    const safeName = (selectedBoss ? selectedBoss.name : 'boss').replace(/[^a-z0-9]+/gi, '-').toLowerCase();
    link.download = 'fiend-hunter-' + safeName + '-stats.png';
    link.href = canvas.toDataURL('image/png');
    document.body.appendChild(link);
    link.click();
    link.remove();
    flashButton(btn, 'Saved!', 'is-done', 1600);
  } catch (err) {
    console.error('Screenshot failed:', err);
    btn.title = (err && err.message) ? err.message : String(err);
    flashButton(btn, 'Failed', 'is-error', 1800);
  } finally {
    wrapper.remove();
  }
});

}

if (typeof document$ !== 'undefined') {
  document$.subscribe(() => {
    init();
  });
} else {
  document.addEventListener('DOMContentLoaded', init);
}