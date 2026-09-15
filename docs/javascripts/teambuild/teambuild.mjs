import { rules } from "./rules.mjs";
import { evaluateTeam } from "./engine.mjs";

const RECOMMENDED_STARTER_TEAM = [
  "b_rank_idol_helena",
  "hand_of_salvation_elpis",
  "kind_student_samay",
  "summer_vacation_dalvi",
  "dream_bride_eclipse"
];

const SLOT_COUNT = 5;

const unitsUrl = new URL("../../assets/data/character-summary.json", import.meta.url);
const charAssetsUrl = new URL("../../assets/data/char-assets.json", import.meta.url);
const torsoImageBase = new URL("../../assets/images/character-illustration/torso/", import.meta.url);

async function init(root) {
  const [gameUnits, charAssets] = await Promise.all([
    fetch(unitsUrl).then(r => r.json()),
    fetch(charAssetsUrl).then(r => r.json())
  ]);

  const charAssetsById = new Map(charAssets.map(a => [a.id, a]));
  const units = gameUnits.map(unit => {
    const asset = charAssetsById.get(unit.id);
    if (!asset) {
      console.warn(`bd2-checker: no image asset found for tagged unit "${unit.id}" — check the id matches char-assets.json.`);
    }
    return {
      ...unit,
      imageUrl: asset ? new URL(`${asset.torso}.avif`, torsoImageBase).href : null
    };
  });

  const teamState = new Array(SLOT_COUNT).fill(null); // holds unit ids or null
  let activeSlot = null;

  const cellsDiv = root.querySelector("#bd2-cells");
  cellsDiv.style.setProperty("--slot-count", SLOT_COUNT);
  const pickerBackdrop = root.querySelector("#bd2-picker");
  const pickerSearch = root.querySelector("#bd2-picker-search");
  const pickerGrid = root.querySelector("#bd2-picker-grid");

  // --- Cells -----------------------------------------------------------

  function renderCells() {
    cellsDiv.innerHTML = "";
    teamState.forEach((unitId, i) => {
      const unit = unitId ? units.find(u => u.id === unitId) : null;
      const cell = document.createElement("div");
      cell.className = "cell";
      cell.tabIndex = 0;
      cell.setAttribute("role", "button");
      cell.setAttribute("aria-label", unit ? `Slot ${i + 1}: ${unit.name}. Click to change.` : `Slot ${i + 1}: empty. Click to pick a character.`);
      cell.innerHTML = `
        <div class="cell-image-wrap">
          ${unit
            ? (unit.imageUrl
                ? `<img src="${unit.imageUrl}" alt="${unit.name}" loading="lazy">`
                : `<span class="cell-placeholder" title="No image found for this unit">?</span>`)
            : `<span class="cell-placeholder">+</span>`}
        </div>
        <div class="cell-arrows">
          <button type="button" class="cell-arrow" data-dir="left" ${i === 0 ? "disabled" : ""} aria-label="Move slot ${i + 1} left">◀</button>
          <button type="button" class="cell-arrow" data-dir="right" ${i === SLOT_COUNT - 1 ? "disabled" : ""} aria-label="Move slot ${i + 1} right">▶</button>
        </div>
        <div class="cell-name ${unit ? "" : "empty"}">${unit ? unit.name : `Slot ${i + 1}`}</div>
      `;
      cell.addEventListener("click", () => openPicker(i));
      cell.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openPicker(i); }
      });

      // Arrow clicks must not bubble up to the cell's own click handler
      // (which would otherwise also open the picker for this slot).
      cell.querySelector('[data-dir="left"]').addEventListener("click", (e) => {
        e.stopPropagation();
        swapCells(i, i - 1);
      });
      cell.querySelector('[data-dir="right"]').addEventListener("click", (e) => {
        e.stopPropagation();
        swapCells(i, i + 1);
      });

      cellsDiv.appendChild(cell);
    });
  }

  function swapCells(i, j) {
    if (j < 0 || j >= SLOT_COUNT) return; // no-op past the edges
    [teamState[i], teamState[j]] = [teamState[j], teamState[i]];
    renderCells();
    runEvaluation();
  }

  // --- Picker modal ------------------------------------------------------

  function openPicker(slotIndex) {
    activeSlot = slotIndex;
    pickerSearch.value = "";
    renderPickerGrid("");
    pickerBackdrop.hidden = false;
    pickerSearch.focus();
  }

  function closePicker() {
    pickerBackdrop.hidden = true;
    activeSlot = null;
  }

  function renderPickerGrid(query) {
    const q = query.trim().toLowerCase();
    const matches = q
      ? units.filter(u => u.name.toLowerCase().includes(q))
      : units;

    pickerGrid.innerHTML = "";

    if (matches.length === 0) {
      pickerGrid.innerHTML = `<p class="picker-empty">No characters match "${query}".</p>`;
      return;
    }

    for (const unit of matches) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "picker-item";
      btn.innerHTML = `
        ${unit.imageUrl
          ? `<img src="${unit.imageUrl}" alt="${unit.name}" loading="lazy">`
          : `<div class="picker-item-noimg" title="No image found for this unit">?</div>`}
        <div class="picker-item-name">${unit.name}</div>
      `;
      btn.addEventListener("click", () => selectUnit(unit.id));
      pickerGrid.appendChild(btn);
    }
  }

  function selectUnit(unitId) {
    if (activeSlot === null) return;
    teamState[activeSlot] = unitId;
    closePicker();
    renderCells();
    runEvaluation();
  }

  pickerSearch.addEventListener("input", () => renderPickerGrid(pickerSearch.value));
  pickerBackdrop.addEventListener("click", (e) => {
    if (e.target === pickerBackdrop) closePicker(); // click outside the panel
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !pickerBackdrop.hidden) closePicker();
  });

  // --- Evaluation --------------------------------------------------------

  function runEvaluation() {
    const team = teamState
      .map(id => (id ? units.find(u => u.id === id) : null))
      .filter(Boolean);

    const resultsDiv = root.querySelector("#bd2-results");
    resultsDiv.innerHTML = "";

    // Require all slots to be filled before evaluating
    if (team.length < SLOT_COUNT) {
      resultsDiv.innerHTML = `<p class="empty-msg">Select all ${SLOT_COUNT} costumes to evaluate the team.</p>`;
      return;
    }

    const results = evaluateTeam(team, {}, rules);

    if (results.length === 0) {
      resultsDiv.innerHTML = `<p class="empty-msg">No warnings triggered.</p>`;
      return;
    }

    for (const r of results) {
      const div = document.createElement("div");
      div.className = `result ${r.severity}`;
      div.innerHTML = `<span class="tag">${r.severity}</span>${r.message}`;
      resultsDiv.appendChild(div);
    }
  }

  root.querySelector("#bd2-randomize")?.addEventListener("click", () => {
    const pool = shuffle([...units]).slice(0, SLOT_COUNT);
    pool.forEach((u, i) => { teamState[i] = u.id; });
    for (let i = pool.length; i < SLOT_COUNT; i++) teamState[i] = null;
    renderCells();
    runEvaluation();
  });

  root.querySelector("#bd2-preset-beginner")?.addEventListener("click", () => {
  RECOMMENDED_STARTER_TEAM.slice(0, SLOT_COUNT).forEach((id, i) => {
    teamState[i] = id;
  });
  renderCells();
  runEvaluation();
  });

  renderCells();
}

function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function setupChecker() {
  const root = document.getElementById("bd2-checker");
  
  if (root && !root.dataset.initialized) {
    root.dataset.initialized = "true";
    init(root);
  }
}

if (typeof document$ !== "undefined") {
  document$.subscribe(setupChecker);
} else {
  document.addEventListener("DOMContentLoaded", setupChecker);
}