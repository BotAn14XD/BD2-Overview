(function () {
  "use strict";

  const esc = (s) =>
    String(s).replace(/[&<>"']/g, (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
    );

  const fmt = (s) =>
    esc(s).replace(/&lt;(\/?)(i|em|b|strong)&gt;/g, "<$1$2>");

  function highlight(text, query) {
    if (!query) return esc(text);
    const i = text.toLowerCase().indexOf(query.toLowerCase());
    if (i === -1) return esc(text);
    return (
      esc(text.slice(0, i)) +
      "<mark>" + esc(text.slice(i, i + query.length)) + "</mark>" +
      esc(text.slice(i + query.length))
    );
  }

  function introLines(intro) {
    if (Array.isArray(intro)) return intro.filter((l) => String(l).trim() !== "");
    if (typeof intro === "string" && intro.trim()) return [intro];
    return [];
  }

  function buildEncounter(enc) {
    const lines = introLines(enc.intro);
    const intro = lines.length
      ? '<div class="rp-enc__intro">' +
          lines.map((l) => "<p>" + fmt(l) + "</p>").join("") +
        "</div>"
      : "";
    return (
      '<div class="rp-enc">' +
        '<div class="rp-enc__head">Visit #' + esc(enc.n) + "</div>" +
        intro +
        '<div class="rp-ans rp-ans--good">' +
          '<span class="rp-ans__mark">\u2713</span><span>' + fmt(enc.correct) + "</span>" +
        "</div>" +
        '<div class="rp-ans rp-ans--bad">' +
          '<span class="rp-ans__mark">\u2717</span><span>' + fmt(enc.wrong) + "</span>" +
        "</div>" +
      "</div>"
    );
  }

  function buildDrinks(drinks, prefix) {
    return (drinks || []).map((d) => {
      const inner = d.icon
        ? '<img src="' + prefix + esc(d.icon) + '" alt="' + esc(d.name) + '">'
        : '<span class="rapport__drink-name">' + esc(d.name) + "</span>";
      return '<span class="rapport__drink" title="' + esc(d.name) + '">' + inner + "</span>";
    }).join("");
  }

  function renderPanel(panel, c, prefix) {
    panel.innerHTML =
      '<div class="rapport__header">' +
        '<h3 class="rapport__title"><small>' + esc(c.character) + "</small>" + esc(c.costume) + "</h3>" +
        '<div class="rapport__drinks">' + buildDrinks(c.drinks, prefix) + "</div>" +
      "</div>" +
      '<div class="rapport__encounters">' +
        (c.encounters || [])
          .slice()
          .sort((a, b) => a.n - b.n)
          .map(buildEncounter)
          .join("") +
      "</div>";
    panel.hidden = false;
  }

  function initOne(root) {
    if (root.dataset.rpReady) return;
    root.dataset.rpReady = "1";

    const src = root.dataset.src || "assets/data/rapport.json";
    const prefix = root.dataset.prefix || "/";

    root.innerHTML =
      '<div class="rapport__search">' +
        '<input class="rapport__input" type="text" autocomplete="off" ' +
        'placeholder="Search a costume or character\u2026" ' +
        'role="combobox" aria-expanded="false" aria-autocomplete="list">' +
        '<ul class="rapport__list" role="listbox" hidden></ul>' +
      "</div>" +
      '<div class="rapport__panel" hidden></div>' +
      '<button type="button" class="rapport__back-btn" aria-label="Back to search" hidden>' +
        '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>' +
        '<span>Search</span>' +
      '</button>';

    const input = root.querySelector(".rapport__input");
    const list = root.querySelector(".rapport__list");
    const panel = root.querySelector(".rapport__panel");
    const searchBox = root.querySelector(".rapport__search");
    const backBtn = root.querySelector(".rapport__back-btn");

    let data = [];
    let matches = [];
    let active = -1;
    let isSearchIntersecting = true;

    // Visibility Evaluator for Back-to-Search Button
    function updateBackBtn() {
      const shouldShow = !isSearchIntersecting && !panel.hidden;
      backBtn.hidden = !shouldShow;
    }

    // Observer to track if the search box is on screen
    let isScrolledPast = false;

    // Visibility Evaluator for Back-to-Search Button
    function updateBackBtn() {
      const shouldShow = isScrolledPast && !panel.hidden;
      backBtn.hidden = !shouldShow;
    }

    // Observer to track if the search box has been scrolled ABOVE the viewport
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          // Only treat as "scrolled past" if it's out of view AND its top position is above the viewport (< 0)
          isScrolledPast = !entry.isIntersecting && entry.boundingClientRect.top < 0;
          updateBackBtn();
        });
      },
      { threshold: 0 }
    );
    observer.observe(searchBox);

    backBtn.addEventListener("click", () => {
      input.scrollIntoView({ behavior: "smooth", block: "center" });
      input.focus({ preventScroll: true });
    });

    fetch(src)
      .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then((json) => { data = json.costumes || []; })
      .catch(() => {
        panel.hidden = false;
        panel.innerHTML =
          '<div class="rapport__placeholder">Couldn\u2019t load costume data. ' +
          "Check the path in <code>data-src</code>.</div>";
        updateBackBtn();
      });

    function closeList() {
      list.hidden = true;
      input.setAttribute("aria-expanded", "false");
      active = -1;
    }

    function openList(q) {
      const query = q.trim().toLowerCase();
      matches = query
        ? data.filter(
            (c) =>
              c.costume.toLowerCase().includes(query) ||
              (c.character || "").toLowerCase().includes(query)
          )
        : [];
      if (!query) { closeList(); return; }

      list.innerHTML = matches.length
        ? matches.map((c, i) =>
            '<li class="rapport__option" role="option" data-i="' + i + '" aria-selected="false">' +
              '<span class="rapport__option-name">' + highlight(c.costume, q) + "</span>" +
              '<span class="rapport__option-char">' + highlight(c.character || "", q) + "</span>" +
            "</li>"
          ).join("")
        : '<li class="rapport__empty">No matches</li>';

      list.hidden = false;
      input.setAttribute("aria-expanded", "true");
      active = -1;
    }

    function setActive(i) {
      const opts = list.querySelectorAll(".rapport__option");
      opts.forEach((o) => o.setAttribute("aria-selected", "false"));
      if (i >= 0 && i < opts.length) {
        opts[i].setAttribute("aria-selected", "true");
        opts[i].scrollIntoView({ block: "nearest" });
      }
      active = i;
    }

    function choose(i) {
      const c = matches[i];
      if (!c) return;
      input.value = c.costume;
      closeList();
      renderPanel(panel, c, prefix);
      updateBackBtn();
    }

    input.addEventListener("input", () => openList(input.value));
    input.addEventListener("focus", () => { if (input.value.trim()) openList(input.value); });
    input.addEventListener("keydown", (e) => {
      const n = matches.length;
      if (list.hidden || !n) return;
      if (e.key === "ArrowDown") { e.preventDefault(); setActive((active + 1) % n); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive((active - 1 + n) % n); }
      else if (e.key === "Enter") { e.preventDefault(); choose(active >= 0 ? active : 0); }
      else if (e.key === "Escape") { closeList(); }
    });
    list.addEventListener("mousedown", (e) => {
      const li = e.target.closest(".rapport__option");
      if (li) { e.preventDefault(); choose(+li.dataset.i); }
    });

    root._rpClose = closeList;
  }

  function initAll() {
    document.querySelectorAll(".rapport").forEach(initOne);
  }

  if (!window.__rapportClickBound) {
    window.__rapportClickBound = true;
    document.addEventListener("click", (e) => {
      document.querySelectorAll(".rapport").forEach((root) => {
        if (root._rpClose && !root.contains(e.target)) root._rpClose();
      });
    });
  }

  window.rapportInit = initAll;

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(initAll);
  } else if (document.readyState !== "loading") {
    initAll();
  } else {
    document.addEventListener("DOMContentLoaded", initAll);
  }
})();