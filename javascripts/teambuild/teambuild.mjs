import { rules } from "./rules.mjs";
import { evaluateTeam } from "./engine.mjs";

const upgradeIconBase = new URL("../../assets/images/icons/upgrades/", import.meta.url);
const potentialIconBase = new URL("../../assets/images/icons/range/", import.meta.url);
const unitsUrl = new URL("../../assets/data/character-summary.json", import.meta.url);
const charAssetsUrl = new URL("../../assets/data/char-assets.json", import.meta.url);
const torsoImageBase = new URL("../../assets/images/character-illustration/torso/", import.meta.url);

const RECOMMENDED_STARTER_TEAM = [
  "b_rank_idol_helena",
  "hand_of_salvation_elpis",
  "kind_student_samay",
  "summer_vacation_dalvi",
  "dream_bride_eclipse"
];

const SLOT_COUNT = 5;

function resolveUnitEffects(unit, activePotentials = new Set()) {
  const effects = new Set(unit?.effects || []);

  if (unit?.potentials && activePotentials) {
    for (const pot of unit.potentials) {
      if (activePotentials.has(pot.id)) {
        if (Array.isArray(pot.removeEffects)) {
          pot.removeEffects.forEach(e => effects.delete(e));
        }
        if (Array.isArray(pot.addEffects)) {
          pot.addEffects.forEach(e => effects.add(e));
        }
      }
    }
  }

  return Array.from(effects);
}

function calculateUnitSP(unit, dupe = 5, activePotentials = new Set()) {
  if (!unit) return 0;
  let cost = unit.spCost ?? 0;

  if (unit.spBreak) {
    const breakTiers = Object.keys(unit.spBreak)
      .map(Number)
      .sort((a, b) => a - b);
    for (const tier of breakTiers) {
      if (dupe >= tier) {
        cost = unit.spBreak[tier];
      }
    }
  }

  if (unit.potentials && activePotentials) {
    for (const pot of unit.potentials) {
      if (activePotentials.has(pot.id) && pot.spDelta) {
        const delta = parseInt(pot.spDelta, 10);
        if (!isNaN(delta)) cost += delta;
      }
    }
  }

  return Math.max(0, cost);
}

const createEmptySlot = () => ({ id: null, dupe: 5, potentials: new Set() });

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

  const teamState = Array.from({ length: SLOT_COUNT }, createEmptySlot);
  let activeSlot = null;

  const cellsDiv = root.querySelector("#bd2-cells");
  cellsDiv.style.setProperty("--slot-count", SLOT_COUNT);
  const pickerBackdrop = root.querySelector("#bd2-picker");
  const pickerSearch = root.querySelector("#bd2-picker-search");
  const pickerGrid = root.querySelector("#bd2-picker-grid");

  // --- Cells -----------------------------------------------------------

  // --- Cells -----------------------------------------------------------

  function renderCells() {
    cellsDiv.innerHTML = "";

    const teamHasPotentials = teamState.some(slot => {
      if (!slot.id) return false;
      const unit = units.find(u => u.id === slot.id);
      return (unit?.potentials?.length ?? 0) > 0;
    });

    teamState.forEach((slot, i) => {
      const unit = slot.id ? units.find(u => u.id === slot.id) : null;
      const currentSP = unit ? calculateUnitSP(unit, slot.dupe, slot.potentials) : null;
      const potentials = unit?.potentials || [];

      const cell = document.createElement("div");
      cell.className = "cell";
      cell.tabIndex = 0;
      cell.setAttribute("role", "button");
      cell.setAttribute("aria-label", unit ? `Slot ${i + 1}: ${unit.name}` : `Slot ${i + 1}: empty`);

      cell.innerHTML = `
        <div class="cell-image-wrap">
          ${unit
            ? (unit.imageUrl
                ? `<img src="${unit.imageUrl}" alt="${unit.name}" loading="lazy" draggable="false">`
                : `<span class="cell-placeholder">?</span>`)
            : `<span class="cell-placeholder">+</span>`}

          ${unit ? `
            <div class="cell-dupe-wrap">
              <button type="button" class="cell-dupe-trigger" title="Change upgrade tier (+0 to +5)" aria-haspopup="listbox" aria-label="Upgrade level">
                <img class="cell-dupe-img" src="${new URL(`upgrade_${slot.dupe}.avif`, upgradeIconBase).href}" alt="+${slot.dupe}">
              </button>
              <div class="cell-dupe-menu" hidden role="listbox">
                ${[0, 1, 2, 3, 4, 5].map(lvl => `
                  <button type="button" 
                          class="cell-dupe-item ${slot.dupe === lvl ? "active" : ""}" 
                          data-level="${lvl}"
                          role="option"
                          aria-selected="${slot.dupe === lvl}">
                    <img src="${new URL(`upgrade_${lvl}.avif`, upgradeIconBase).href}" alt="+${lvl}">
                  </button>
                `).join("")}
              </div>
            </div>
          ` : ""}

          ${unit ? `<div class="cell-sp-bar" title="Turn 1 SP Cost">${currentSP} SP</div>` : ""}
        </div>

        <!-- Drag Reorder Handle (Keyboard Accessible) -->
        <div class="cell-drag-bar">
          <button type="button" 
                  class="cell-drag-handle" 
                  title="Drag or use Left/Right arrows to reorder" 
                  aria-label="Reorder slot ${i + 1}">
            <svg viewBox="0 0 16 16" width="16" height="12" aria-hidden="true">
              <circle cx="3" cy="5" r="1.3"></circle>
              <circle cx="8" cy="5" r="1.3"></circle>
              <circle cx="13" cy="5" r="1.3"></circle>
              <circle cx="3" cy="11" r="1.3"></circle>
              <circle cx="8" cy="11" r="1.3"></circle>
              <circle cx="13" cy="11" r="1.3"></circle>
            </svg>
          </button>
        </div>

        <!-- Costume Name (Top-aligned) -->
        <div class="cell-name ${unit ? "" : "empty"}">
          ${unit ? unit.name : `Slot ${i + 1}`}
        </div>

        ${teamHasPotentials ? `
          <div class="cell-potentials-row">
            ${potentials.map(p => {
              const iconName = p.icon || p.id.replace(/_\d+$/, "");
              const isChecked = slot.potentials.has(p.id);
              return `
                <button type="button" 
                        class="cell-pot-btn ${isChecked ? "active" : ""}" 
                        data-pot-id="${p.id}"
                        title="${p.label || p.id} (Click to toggle)"
                        aria-pressed="${isChecked}">
                  <img src="${new URL(`${iconName}.avif`, potentialIconBase).href}" alt="${p.label || p.id}">
                </button>
              `;
            }).join("")}
          </div>
        ` : ""}
      `;

      cell.addEventListener("click", (e) => {
        if (e.target.closest("button") || e.target.closest(".cell-dupe-wrap")) return;
        openPicker(i);
      });
      cell.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openPicker(i);
        }
      });

      const dupeWrap = cell.querySelector(".cell-dupe-wrap");
      if (dupeWrap) {
        const trigger = dupeWrap.querySelector(".cell-dupe-trigger");
        const menu = dupeWrap.querySelector(".cell-dupe-menu");

        trigger.addEventListener("click", (e) => {
          e.stopPropagation();
          cellsDiv.querySelectorAll(".cell-dupe-menu").forEach(m => {
            if (m !== menu) m.hidden = true;
          });
          menu.hidden = !menu.hidden;
        });

        menu.querySelectorAll(".cell-dupe-item").forEach(item => {
          item.addEventListener("click", (e) => {
            e.stopPropagation();
            slot.dupe = Number(item.dataset.level);
            menu.hidden = true;
            renderCells();
            runEvaluation();
          });
        });
      }

      cell.querySelectorAll(".cell-pot-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          const potId = btn.dataset.potId;
          if (slot.potentials.has(potId)) {
            slot.potentials.delete(potId);
          } else {
            slot.potentials.add(potId);
          }
          renderCells();
          runEvaluation();
        });
      });

      const dragHandle = cell.querySelector(".cell-drag-handle");
      if (dragHandle) {
        dragHandle.addEventListener("keydown", (e) => {
          if (e.key === "ArrowLeft" && i > 0) {
            e.preventDefault();
            swapCells(i, i - 1);
            // Refocus handle in the new slot position
            setTimeout(() => cellsDiv.children[i - 1]?.querySelector(".cell-drag-handle")?.focus(), 0);
          } else if (e.key === "ArrowRight" && i < SLOT_COUNT - 1) {
            e.preventDefault();
            swapCells(i, i + 1);
            setTimeout(() => cellsDiv.children[i + 1]?.querySelector(".cell-drag-handle")?.focus(), 0);
          }
        });

        attachDragHandle(dragHandle, i);
      }

      cellsDiv.appendChild(cell);
    });
  }

  function swapCells(i, j) {
    if (j < 0 || j >= SLOT_COUNT) return; // no-op past the edges
    [teamState[i], teamState[j]] = [teamState[j], teamState[i]];
    renderCells();
    runEvaluation();
  }

  function moveSlot(from, to) {
    if (from === to) return;
    const [item] = teamState.splice(from, 1);
    teamState.splice(to, 0, item);
    renderCells();
    runEvaluation();
  }

  // --- Drag & drop reordering --------------------------------------------
  //
  // Pointer Events unify mouse/touch/pen into one code path, so there's no
  // need for a separate mobile vs. desktop engine or a library like
  // SortableJS for what is only ever a fixed 5-cell row. Gesture
  // disambiguation is handled by giving drag its own handle icon: the
  // handle carries no click behavior, so it never competes with "click a
  // cell to open the picker", and it gets `touch-action: none` so it never
  // fights the page for a touch-scroll gesture.

  let dragCtx = null;
  const DRAG_THRESHOLD_PX = 4; // ignore tiny jitter so a plain tap on the handle doesn't visually "flash" a drag

  function attachDragHandle(handle, index) {
    if (!handle) return;
    handle.addEventListener("pointerdown", (e) => {
      if (e.button !== 0 && e.pointerType === "mouse") return; // primary mouse button only
      e.preventDefault();
      e.stopPropagation();
      startDrag(e, index, handle);
    });
  }

  function startDrag(e, index, handle) {
    const sourceCell = cellsDiv.children[index];
    if (!sourceCell) return;
    const rect = sourceCell.getBoundingClientRect();

    handle.setPointerCapture(e.pointerId);

    const ghost = sourceCell.cloneNode(true);
    ghost.classList.add("drag-ghost");
    ghost.style.width = `${rect.width}px`;
    ghost.style.height = `${rect.height}px`;
    ghost.style.left = `${rect.left}px`;
    ghost.style.top = `${rect.top}px`;
    document.body.appendChild(ghost);

    sourceCell.classList.add("dragging");

    dragCtx = {
      pointerId: e.pointerId,
      handle,
      ghost,
      fromIndex: index,
      currentIndex: index,
      offsetX: e.clientX - rect.left,
      offsetY: e.clientY - rect.top,
      startX: e.clientX,
      startY: e.clientY,
      moved: false
    };

    handle.addEventListener("pointermove", onDragMove);
    handle.addEventListener("pointerup", onDragEnd);
    handle.addEventListener("pointercancel", onDragEnd);
  }

  function onDragMove(e) {
    if (!dragCtx || e.pointerId !== dragCtx.pointerId) return;

    if (!dragCtx.moved) {
      const dist = Math.hypot(e.clientX - dragCtx.startX, e.clientY - dragCtx.startY);
      if (dist < DRAG_THRESHOLD_PX) return;
      dragCtx.moved = true;
    }

    dragCtx.ghost.style.left = `${e.clientX - dragCtx.offsetX}px`;
    dragCtx.ghost.style.top = `${e.clientY - dragCtx.offsetY}px`;

    // Cells sit in a single fixed-column row (never wraps), so nearest-center
    // on the X axis alone is enough to find the drop target.
    const cells = Array.from(cellsDiv.children);
    let nearestIndex = dragCtx.currentIndex;
    let nearestDist = Infinity;
    cells.forEach((cell, idx) => {
      const r = cell.getBoundingClientRect();
      const center = r.left + r.width / 2;
      const dist = Math.abs(e.clientX - center);
      if (dist < nearestDist) {
        nearestDist = dist;
        nearestIndex = idx;
      }
    });

    cells.forEach((cell, idx) => {
      cell.classList.toggle("drag-over", idx === nearestIndex && idx !== dragCtx.fromIndex);
    });
    dragCtx.currentIndex = nearestIndex;
  }

  function onDragEnd(e) {
    if (!dragCtx || e.pointerId !== dragCtx.pointerId) return;

    const { handle, ghost, fromIndex, currentIndex, moved } = dragCtx;

    if (handle.hasPointerCapture(e.pointerId)) handle.releasePointerCapture(e.pointerId);
    handle.removeEventListener("pointermove", onDragMove);
    handle.removeEventListener("pointerup", onDragEnd);
    handle.removeEventListener("pointercancel", onDragEnd);

    ghost.remove();
    Array.from(cellsDiv.children).forEach(cell => cell.classList.remove("dragging", "drag-over"));

    dragCtx = null;

    if (moved && currentIndex !== fromIndex) {
      moveSlot(fromIndex, currentIndex);
    }
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

    const takenCharacters = new Set(
      teamState
        .filter((slot, idx) => idx !== activeSlot && slot.id)
        .map(slot => {
          const u = units.find(unit => unit.id === slot.id);
          return u?.character || u?.id;
        })
    );

    pickerGrid.innerHTML = "";

    if (matches.length === 0) {
      pickerGrid.innerHTML = `<p class="picker-empty">No characters match "${query}".</p>`;
      return;
    }

    for (const unit of matches) {
      const unitChar = unit.character || unit.id;
      const isTaken = takenCharacters.has(unitChar);

      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = `picker-item ${isTaken ? "is-disabled" : ""}`;
      btn.disabled = isTaken;
      btn.title = isTaken ? `${unit.name} (Character already in another slot)` : unit.name;

      btn.innerHTML = `
        ${unit.imageUrl
          ? `<img src="${unit.imageUrl}" alt="${unit.name}" loading="lazy">`
          : `<div class="picker-item-noimg" title="No image found for this unit">?</div>`}
        <div class="picker-item-name">${unit.name}</div>
        ${isTaken ? `<span class="picker-item-badge">In Team</span>` : ""}
      `;

      if (!isTaken) {
        btn.addEventListener("click", () => selectUnit(unit.id));
      }

      pickerGrid.appendChild(btn);
    }
  }

  function selectUnit(unitId) {
    if (activeSlot === null) return;
    teamState[activeSlot] = { id: unitId, dupe: 5, potentials: new Set() };
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
  document.addEventListener("click", () => {
    cellsDiv.querySelectorAll(".cell-dupe-menu").forEach(m => (m.hidden = true));
  });

  // --- Evaluation --------------------------------------------------------

  function runEvaluation() {
    const team = teamState
      .map(slot => {
        if (!slot?.id) return null;
        const unit = units.find(u => u.id === slot.id);
        if (!unit) return null;
        return {
          ...unit,
          dupe: slot.dupe,
          activePotentials: slot.potentials,
          currentSP: calculateUnitSP(unit, slot.dupe, slot.potentials),
          effects: resolveUnitEffects(unit, slot.potentials) // <-- Dynamically mutates effects
        };
      })
      .filter(Boolean);

    const resultsDiv = root.querySelector("#bd2-results");
    resultsDiv.innerHTML = "";

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
    const shuffled = shuffle([...units]);
    const selectedUnits = [];
    const seenCharacters = new Set();

    for (const u of shuffled) {
      const charKey = u.character || u.id;
      if (!seenCharacters.has(charKey)) {
        seenCharacters.add(charKey);
        selectedUnits.push(u);
        if (selectedUnits.length === SLOT_COUNT) break;
      }
    }

    selectedUnits.forEach((u, i) => {
      teamState[i] = { id: u.id, dupe: 5, potentials: new Set() };
    });
    for (let i = selectedUnits.length; i < SLOT_COUNT; i++) {
      teamState[i] = createEmptySlot();
    }
    renderCells();
    runEvaluation();
  });

  root.querySelector("#bd2-preset-beginner")?.addEventListener("click", () => {
    RECOMMENDED_STARTER_TEAM.slice(0, SLOT_COUNT).forEach((id, i) => {
      teamState[i] = { id, dupe: 5, potentials: new Set() };
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