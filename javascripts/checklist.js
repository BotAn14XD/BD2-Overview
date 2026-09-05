/* ============================================================
   Checklist — unified data-driven rendering
   Everything (permanent trackers, repeating tasks, week-templated
   events, overrides) is defined in checklist.json and rendered
   through ONE path (renderItem). No hand-authored checkbox markup
   anywhere — new.md is just empty tab shells.
   ============================================================ */

async function initChecklist() {
  // Bail out on pages with no checklist tabs at all.
  if (!document.querySelector(".checklist-group")) return;

  const STORAGE_KEY = "bd2_checklist_state";
  const TIMESTAMP_KEY = "bd2_checklist_timestamps";
  let state = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  let timestamps = JSON.parse(localStorage.getItem(TIMESTAMP_KEY) || "{}");

  const now = new Date();

  // --- TEST MODE ---
  // Append ?bd2_test_date=2026-08-20T16:00:00Z to the page URL to run all
  // reset/cycle logic below as if "now" were that instant — no system
  // clock changes needed.
  const _testDateParam = new URLSearchParams(location.search).get("bd2_test_date");
  if (_testDateParam) {
    const _parsed = new Date(_testDateParam);
    if (!isNaN(_parsed)) {
      now.setTime(_parsed.getTime());
      console.warn("[checklist] TEST MODE — using fake date:", now.toISOString());
    } else {
      console.warn("[checklist] bd2_test_date could not be parsed, ignoring:", _testDateParam);
    }
  }

  // Storage-key prefix per cadence. Combined with an item's own numeric
  // "id" to form its storage key (e.g. cadence "daily" + id 3 -> "d_3"),
  // so ids only need to be unique WITHIN a cadence, not site-wide, and
  // there's no hand-typed string id to get wrong or duplicate.
  const CADENCE_PREFIX = {
    daily: "d_", weekly: "w_", biweekly: "bw_", monthly: "m_",
    seasonal: "s_", biseasonal: "bs_", permanent: "p_"
  };

  const PRIORITY_RANK = { high: 0, low: 1 };
  function sortItems(list) {
    return [...list].sort((a, b) => {
      const pa = PRIORITY_RANK[a.priority] ?? 0;
      const pb = PRIORITY_RANK[b.priority] ?? 0;
      if (pa !== pb) return pa - pb;
      return (a.id ?? 0) - (b.id ?? 0);
    });
  }

  // --- Reset boundary helpers ---
  function getLastMidnightUTC() {
    const d = new Date(now);
    d.setUTCHours(0, 0, 0, 0);
    return d.getTime();
  }
  function getLastWednesday15UTC() {
    const d = new Date(now);
    d.setUTCHours(15, 0, 0, 0);
    let day = d.getUTCDay();
    let diff = (day - 3 + 7) % 7;
    if (day === 3 && now < d) diff = 7;
    d.setUTCDate(d.getUTCDate() - diff);
    return d.getTime();
  }

  // Settlement lock: true if `now` falls on the given UTC weekday, at or
  // after the given UTC hour (window closes at the next 00:00 UTC daily
  // reset automatically, since the weekday check stops matching then).
  function isLockedByDayHour(day, hour) {
    if (day === undefined || day === null || hour === undefined || hour === null) return false;
    return now.getUTCDay() === Number(day) && now.getUTCHours() >= Number(hour);
  }

  // --- Synchronous resets (don't need checklist.json) ---
  const lastDailyResetTS = getLastMidnightUTC();
  if (!timestamps.lastDailyReset || timestamps.lastDailyReset < lastDailyResetTS) {
    Object.keys(state).forEach((k) => { if (k.startsWith("d_")) delete state[k]; });
    timestamps.lastDailyReset = lastDailyResetTS;
  }
  const lastWeeklyResetTS = getLastWednesday15UTC();
  if (!timestamps.lastWeeklyReset || timestamps.lastWeeklyReset < lastWeeklyResetTS) {
    Object.keys(state).forEach((k) => { if (k.startsWith("w_")) delete state[k]; });
    timestamps.lastWeeklyReset = lastWeeklyResetTS;
  }
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  localStorage.setItem(TIMESTAMP_KEY, JSON.stringify(timestamps));

  // --- renderItem: the ONLY place that builds checklist DOM ---
  // Every item — permanent, repeating, or template/override-driven —
  // goes through here, so markup shape (and thus styling, restore
  // behavior, lock behavior) is identical regardless of origin.
  function renderItem(container, storageId, item, { locked, badge, priority } = {}) {
    if (!container || document.getElementById(storageId)) return;

    const wrapper = document.createElement("div");
    wrapper.className = "checklist-item";
    wrapper.dataset.priority = priority || item.priority || "high";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.id = storageId;
    checkbox.checked = !!state[storageId];

    if (locked && !checkbox.checked) {
      wrapper.classList.add("is-locked");
      checkbox.disabled = true;
    }
    wrapper.dataset.locked = locked ? "true" : "false";

    const label = document.createElement("label");
    label.htmlFor = storageId;

    // Icon: {icon} token in the name gets replaced; otherwise, if an
    // icon is given, it's prepended. icon_path is an actual image path
    // (matching your MATERIALS_DB/DISHES_DB [path, name] convention),
    // NOT a CSS class that magically knows which image to show.
    let name = item.name || "";
    const iconHtml = item.icon_path
      ? `<img class="icon" src="${item.icon_path}" alt="${item.icon_label || ""}" title="${item.icon_label || ""}">`
      : "";
    name = name.includes("{icon}") ? name.replace("{icon}", iconHtml) : iconHtml + name;

    const badgeHtml = badge ? `<span class="badge">${badge}</span>` : "";
    const lockNoteHtml = `<span class="lock-note">(Settlement in progress — resets 00:00 UTC)</span>`;
    label.innerHTML = `${badgeHtml}<span>${name}</span>${lockNoteHtml}`;

    wrapper.appendChild(checkbox);
    wrapper.appendChild(label);
    container.appendChild(wrapper);
  }

  // --- Fetch the unified data file ---
  let data = null;
  try {
    const res = await fetch("../assets/data/checklist.json");
    if (res.ok) data = await res.json();
  } catch (err) {
    console.warn("checklist.json not loaded or failed to parse:", err);
  }

  if (data) {
    // Cycle-derived resets (biweekly / seasonal / bi-seasonal), all off
    // the same anchor_date so nothing drifts independently.
    const anchor = new Date(data.anchor_date);
    const cycleDays = data.patch_cycle_days || 28;
    const totalDaysElapsed = Math.floor((now.getTime() - anchor.getTime()) / (1000 * 60 * 60 * 24));

    const biSeasonDays = cycleDays * 2; // 56 days
    const biSeasonElapsedDays = ((totalDaysElapsed % biSeasonDays) + biSeasonDays) % biSeasonDays;

    const currentBiweekCycle = Math.floor(totalDaysElapsed / 14);
    if (timestamps.lastBiweekCycle === undefined || timestamps.lastBiweekCycle !== currentBiweekCycle) {
      Object.keys(state).forEach((k) => { if (k.startsWith("bw_")) delete state[k]; });
      timestamps.lastBiweekCycle = currentBiweekCycle;
    }

    const currentCycleNumber = Math.floor(totalDaysElapsed / cycleDays);
    if (timestamps.lastSeasonCycle === undefined || timestamps.lastSeasonCycle !== currentCycleNumber) {
      Object.keys(state).forEach((k) => { if (k.startsWith("s_")) delete state[k]; });
      timestamps.lastSeasonCycle = currentCycleNumber;
    }

    const currentBiSeasonCycle = Math.floor(currentCycleNumber / 2);
    if (timestamps.lastBiSeasonCycle === undefined || timestamps.lastBiSeasonCycle !== currentBiSeasonCycle) {
      Object.keys(state).forEach((k) => { if (k.startsWith("bs_")) delete state[k]; });
      timestamps.lastBiSeasonCycle = currentBiSeasonCycle;
    }

    const currentBiSeasonStart = new Date(anchor.getTime());
    currentBiSeasonStart.setUTCDate(currentBiSeasonStart.getUTCDate() + currentBiSeasonCycle * biSeasonDays);
    const nextBiSeasonReset = new Date(currentBiSeasonStart.getTime());
    nextBiSeasonReset.setUTCDate(nextBiSeasonReset.getUTCDate() + biSeasonDays);

    const msUntilReset = nextBiSeasonReset.getTime() - now.getTime();
    const hoursUntilReset = msUntilReset / (1000 * 60 * 60);

    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    localStorage.setItem(TIMESTAMP_KEY, JSON.stringify(timestamps));

    // --- Permanent (manual-reset-only trackers) ---
    const container_permanent = document.getElementById("checklist-permanent");
    sortItems(data.permanent || []).forEach((item) => {
      renderItem(container_permanent, `p_${item.id}`, item, { locked: false });
    });

    // --- Repeating (daily/weekly/biweekly/monthly/seasonal/biseasonal) ---
    sortItems(data.repeating || []).forEach((item) => {
      const targetTab = item.target_tab || item.cadence;
      const container = document.getElementById(`checklist-${targetTab}`);
      const prefix = CADENCE_PREFIX[item.cadence] || "x_";

      let locked = isLockedByDayHour(item.settlement_day, item.settlement_hour);

      if (item.settlement_hours_before_reset !== undefined) {
        locked = hoursUntilReset <= item.settlement_hours_before_reset && hoursUntilReset > 0;
      }

      renderItem(container, `${prefix}${item.id}`, item, { locked });
    });

    // --- Week-templated events & overrides (cycle_template / overrides) ---
    injectDynamicEvents(data);
  }

  // Priority separation: run AFTER everything (repeating + dynamic events)
  // has been rendered into every container, since dynamic events append
  // later and would otherwise land under the wrong heading if we tried to
  // insert dividers as items rendered instead of doing one final pass.
  document.querySelectorAll(".checklist-group").forEach(finalizeContainerPriority);

  bindCheckboxes();

  function finalizeContainerPriority(container) {
    const rank = { high: 0, low: 1 };
    const items = Array.from(container.querySelectorAll(":scope > .checklist-item"));
    if (items.length === 0) return;

    // Stable sort — items with equal priority keep their existing relative
    // order (repeating items are already id-ordered from sortItems()).
    items.sort((a, b) => (rank[a.dataset.priority] ?? 0) - (rank[b.dataset.priority] ?? 0));

    const distinctPriorities = new Set(items.map((i) => i.dataset.priority || "high"));
    container.querySelectorAll(":scope > .priority-divider").forEach((d) => d.remove());

    let lastPriority = null;
    items.forEach((item) => {
      const p = item.dataset.priority || "high";
      // Skip headers entirely if every item in this tab shares one
      // priority — a "High Priority" label on a tab with nothing else is
      // just noise.
      if (distinctPriorities.size > 1 && p !== lastPriority) {
        const divider = document.createElement("div");
        divider.className = "priority-divider";
        divider.textContent = p === "high" ? "High Priority" : "Low Priority";
        container.appendChild(divider);
        lastPriority = p;
      }
      container.appendChild(item); // re-appending an existing node MOVES it
    });
  }

  function injectDynamicEvents(schedule) {
    const anchor = new Date(schedule.anchor_date);
    const cycleDays = schedule.patch_cycle_days || 28;

    const totalDaysElapsed = Math.floor((now.getTime() - anchor.getTime()) / (1000 * 60 * 60 * 24));
    let cycleDayIndex = totalDaysElapsed % cycleDays;
    if (cycleDayIndex < 0) cycleDayIndex += cycleDays;
    const currentWeekNum = Math.floor(cycleDayIndex / 7) + 1;
    const weekKey = `week_${currentWeekNum}`;

    const cycleStartDate = new Date(anchor.getTime());
    const currentCycleNumber = Math.floor(totalDaysElapsed / cycleDays);
    cycleStartDate.setUTCDate(cycleStartDate.getUTCDate() + currentCycleNumber * cycleDays);

    // Anchor each event to the start of its OWN template week, not the
    // season start — offset_start_days/offset_end_days are relative to
    // whichever week (week_1..week_N) the event is actually templated
    // under.
    const weekStartDate = new Date(cycleStartDate.getTime());
    weekStartDate.setUTCDate(weekStartDate.getUTCDate() + (currentWeekNum - 1) * 7);

    let activeEvents = [];

    (schedule.overrides || []).forEach((override) => {
      const start = new Date(override.start);
      const end = new Date(override.end);
      if (now >= start && now < end) {
        activeEvents.push({
          id: override.id || override.event_id,
          name: override.name,
          tag: override.tag,
          is_daily_reset: override.is_daily_reset || false,
          target_tab: override.target_tab || (override.is_daily_reset ? "daily" : "seasonal"),
          suppress_default_cycle: override.suppress_default_cycle || false,
          is_settlement_locked: false
        });
      }
    });

    const templateWeek = schedule.cycle_template?.[weekKey];
    if (templateWeek?.events) {
      templateWeek.events.forEach((evt) => {
        if (activeEvents.some((o) => o.suppress_default_cycle && o.id === (evt.id || evt.event_id))) return;

        const evtStart = new Date(weekStartDate.getTime());
        evtStart.setUTCDate(evtStart.getUTCDate() + (evt.offset_start_days || 0));
        evtStart.setUTCHours(0, 0, 0, 0);

        const evtEnd = new Date(weekStartDate.getTime());
        evtEnd.setUTCDate(evtEnd.getUTCDate() + (evt.offset_end_days || 6));
        evtEnd.setUTCHours(evt.settlement_utc_hour || 15, 0, 0, 0);

        const settlementHours = evt.settlement_duration_hours ?? 9;
        const lockedEnd = new Date(evtEnd.getTime() + settlementHours * 60 * 60 * 1000);

        if (now >= evtStart && now < lockedEnd) {
          activeEvents.push({
            ...evt,
            id: evt.id || evt.event_id,
            target_tab: evt.target_tab || (evt.is_daily_reset ? "daily" : "seasonal"),
            is_settlement_locked: now >= evtEnd
          });
        }
      });
    }

    const prefixMap = { daily: "d_", weekly: "w_", biweekly: "bw_", monthly: "m_", seasonal: "s_", biseasonal: "bs_" };
    activeEvents.forEach((evt) => {
      const targetTab = evt.target_tab || "seasonal";
      const container = document.getElementById(`checklist-${targetTab}`);
      if (!container) return;
      const prefix = prefixMap[targetTab] || "s_";
      const storageId = `${prefix}dyn_${evt.id}`;
      renderItem(container, storageId, { id: evt.id, name: evt.name }, {
        locked: evt.is_settlement_locked, badge: evt.tag, priority: evt.priority || "high"
      });
    });
  }

  function isInSettlementLock(item) {
    return item.dataset.locked === "true";
  }

  function bindCheckboxes() {
    document.querySelectorAll(".checklist-item").forEach((item) => {
      const cb = item.querySelector('input[type="checkbox"]');
      if (!cb) return;

      // renderItem() already creates every item pre-checked and
      // pre-locked as appropriate — this is a defensive re-sync only,
      // not the primary mechanism, since everything now goes through one
      // creation path.
      if (state[cb.id] && !cb.checked) {
        item.classList.add("no-anim");
        cb.checked = true;
        requestAnimationFrame(() => requestAnimationFrame(() => item.classList.remove("no-anim")));
      }
      if (!cb.checked && isInSettlementLock(item)) {
        item.classList.add("is-locked");
        cb.disabled = true;
      }

      cb.onchange = (e) => {
        state[e.target.id] = e.target.checked;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      };

      item.onclick = (e) => {
        if (cb.disabled) return;
        if (e.target.tagName === "INPUT" || e.target.closest("label") || e.target.closest("a")) return;
        cb.checked = !cb.checked;
        cb.dispatchEvent(new Event("change", { bubbles: true }));
      };
    });
  }
}

if (typeof document$ !== "undefined" && document$.subscribe) {
  document$.subscribe(initChecklist);
} else if (document.readyState !== "loading") {
  initChecklist();
} else {
  document.addEventListener("DOMContentLoaded", initChecklist);
}