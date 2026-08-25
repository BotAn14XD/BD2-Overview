---
description: A utility tool that displays Brown Dust II Fiend Hunter data and threshold damage required to clear a specific level.
comments: true
image: assets/images/site-assets/fh-banner.png
hero: assets/images/site-assets/index-pc-nav-29.avif
icon: material/calculator-variant

---

![Fiend Hunter](../assets/images/site-assets/index-pc-nav-29.avif){: .card-header-img fetchpriority=high loading=eager }
#

This is a calculator for [Fiend Hunter](../content/fh.md) Bosses stats and threshold damage. 

Type the Boss name, [Season Event](../content/events.md) or Property to open the stats for a specific Boss.

Table includes **Level**, {{HP}} **HP**{.white}, {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} and the Daily Threshold Damage (the consistent score required each day from Day 1 to successfully defeat that level by the final day).

Displayed Level amount can be changed, from 1 to 100 (default — 25).

If you are looking for raw Fiend parameters instead, refer to [this data file](https://github.com/BotAn14XD/BD2-Overview/blob/main/docs/assets/data/fiend-hunter-bosses.json) instead.

<div class="fh-calc">

<div class="search">
  <input
    type="text"
    class="search-input"
    id="search-input"
    placeholder="Search a boss by name, event, or property..."
    autocomplete="off"
    role="combobox"
    aria-expanded="false"
    aria-controls="dropdown"
  >
  <ul class="dropdown" id="dropdown" hidden></ul>
</div>

<div class="quick-boss-shortcut" id="quick-boss-shortcut">
  <span class="shortcut-label">Latest Boss:</span>
  <button type="button" class="boss-chip" id="latest-boss-chip">Loading…</button>
</div>

<div class="placeholder" id="placeholder">
  Search for a boss above to calculate its HP / ATK at every level.
</div>

<div class="card" id="card" hidden>
<div class="card-head">
    <div class="title-block">
    <h2 class="card-title" id="card-title">—</h2>
    <span class="card-subtitle" id="card-subtitle">—</span>
    <span class="break-tag" id="break-tag" hidden>Break season</span>
    </div>
    <span class="tag" id="property-tag"><span class="tag-dot"></span><span id="property-label">—</span></span>
</div>
 
<div class="toolbar">
    <div class="level-field">
    <label for="max-level">Display up to level</label>
    <input type="number" id="max-level" min="1" max="100" value="25">
    <div class="presets">
        <button type="button" class="preset-btn" data-level="10">10</button>
        <button type="button" class="preset-btn" data-level="15">15</button>
        <button type="button" class="preset-btn" data-level="25">25</button>
        <button type="button" class="preset-btn" data-level="30">30</button>
    </div>
    </div>
    <div class="actions">
    <button type="button" class="btn" id="copy-btn">
        <svg viewBox="0 0 24 24"><path d="M16 1H4a2 2 0 0 0-2 2v14h2V3h12V1zm3 4H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm0 16H8V7h11v14z" fill="currentColor"/></svg>
        <span>Copy table</span>
    </button>
    <button type="button" class="btn" id="save-btn">
        <svg viewBox="0 0 24 24"><path d="M4 5h3l1.6-2h6.8L17 5h3a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zm8 3a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 2a3 3 0 1 1 0 6 3 3 0 0 1 0-6z" fill="currentColor"/></svg>
        <span>Save image</span>
    </button>
    </div>
</div>
 
<div class="table-wrap">
<div class="table-scroll" id="table-scroll">
    <table class="stat-table" id="stat-table">
    <thead>
        <tr>
        <th>Level</th>
        <th>HP</th>
        <th>Threshold</th>
        <th id="atk-head">ATK</th>
        </tr>
    </thead>
    <tbody id="table-body"></tbody>
    </table>
</div>
</div>
</div>

</div>

!!! example "Stat Formula & Details"
    $\text{Value} = \text{round}\left[\text{Base} \cdot 1.1 \cdot \left(1 + (\text{Level}-1) \cdot \text{Rate} \cdot 0.01 \cdot \text{Level}^\text{Slope} \cdot \text{Stage Ratio}\right)\right]$

    * $\text{Base} \rightarrow \text{Base Value}$
    * $\text{Level} \rightarrow \text{Boss Level}$
    * $\text{Rate} \rightarrow \text{Initial Growth Parameter}$
    * $\text{Slope} \rightarrow \text{Scale Growth Parameter}$
    * $\text{Stage Ratio} \rightarrow \text{Level Related Multiplier}$

    ---

    * **Rounding** in the formula works as follows:
        * For {{HP}} **HP**, **rounding down to 3 significant figures** is applied.
        * For {{ATK}} **ATK**{.yellow} and {{MATK}} **MATK**{.magenta}, **rounding to the nearest integer** is applied instead, with 0.5 being rounded **down**.
    * Parameters **do not change** with level. However, boss has specific **levels**, after which a new **Stage** is applied. That *can* modify the final stat value, although recently (for at least 11 hunts) it has no impact.
