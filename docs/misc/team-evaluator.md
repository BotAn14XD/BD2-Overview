---
description: A utility tool that evaluates Brown Dust II teams for general content, pinpoints teambuild mistakes and gives advices to improve the team.
comments: true
image: assets/images/site-assets/team-evaluator-banner.png
hero: assets/images/site-assets/index-pc-nav-30_2.avif
icon: fontawesome/solid/people-group

---

![Team Evaluator](../assets/images/site-assets/index-pc-nav-30_2.avif){: .card-header-img fetchpriority=high loading=eager }
#

Team Evaluator diagnoses your 5-unit roster for **General Content**, optimized around securing a clean **Turn 1 clear**.

The tool checks skill order, but ignores grid tile placement and costumes progression.

To evaluate the team, pick five **Costumes** (Not Characters) and it will give you a list of notes, grouped in 3 categories.

* **Error** — Rule-breaking or impossible setups (like fielding duplicate costumes of the same character, or teams that exceed starting SP even with max upgrades).
* **Warning** — Severe anti-synergies or mechanical bottlenecks (like missing buffers or order priority mismatches). While not necessarily fatal, resolving these will drastically improve consistency.
* **Advice** — Additional information that is worth knowing about the team composition.

---

<div id="bd2-checker">
  <div class="cells" id="bd2-cells"></div>
  <div class="controls">
    <button id="bd2-randomize" class="share-btn" type="button">Randomize team</button>
    <button id="bd2-preset-beginner" class="share-btn" type="button">Load New Player Starter Team</button>
  </div>
  <div id="bd2-results"></div>
  <div id="bd2-picker" class="picker-backdrop" hidden>
    <div class="picker-panel">
      <input type="text" id="bd2-picker-search" class="picker-search" placeholder="Search character…" autocomplete="off">
      <div id="bd2-picker-grid" class="picker-grid"></div>
    </div>
  </div>
</div>

??? info "v1.1.0 Notes & Known Limitations"
    Version 1.1.0 brings UI refinement, more precise dupe / SP control, potential liberation toggles and finetuned dictionary file.

    Nonetheless, advanced mechanics (such as conditional requirenments for DPS or placement validation) are still planned for future updates.

    Notice an inaccurate interaction or missing mechanic? Feedback and edge-case reports are welcome via [GitHub Issues](https://github.com/BotAn14XD/BD2-Overview/issues) or our [Discord Server](https://discord.gg/tays83ew3N).