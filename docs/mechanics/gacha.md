---
description: 
comments: true
image: assets/images/site-assets/gacha-banner.png
hero: assets/images/site-assets/index-pc-nav-31.avif
icon: material/dice-multiple

---

![Gacha](../assets/images/site-assets/index-pc-nav-31.avif){: .card-header-img fetchpriority=high loading=eager }
# Gacha {: .sr-only }

Gacha is the main source of getting **Costumes** of Characters and Character's [Exclusive Gear](../progression/gear.md#exclusive-gear).

To access it, press the **Draw** button in Home Screen.

??? image "Image Guide"
    ![Gacha Access](../assets/images/gacha/draw-access.avif)

!!! question "Draw Tab seems to be unavailable?" 
    That is happening because you did not clear **Master Pack 1 (Edge of Dimensions)**. Refer to the New Player Guide for more guidance regarding clearing Master Pack.

    {{ redirect_btn('new', 'New Player Guide', '#4caf50') }} 

!!! image "Draw Menu"
    ![Draw Menu](../assets/images/gacha/gacha_display.avif)

---

## Overview

The gacha consists of banners and can be split into two categories: **Costumes** and **Gear**. Alternatively, they can be categorized into **Standard (Pick-Up)** and **Unique** banners.

A single summon costs **1** {{Draw_Ticket}} **Draw Ticket** or **200** {{Dia}} **Free Dia** (for 10 pulls, **10** {{Draw_Ticket}} Draw Tickets or **2000** {{Dia}} Free Dia respectively).

Some unique banners can also accept {{Selective_Exclusive_Draw_Ticket}} **Selective Exclusive Draw Ticket** or other specific tickets related to the banner.

The game always consumes {{Dia}} Paid Dia **last**, meaning there is a strict order in which consumables are used:

* {{Selective_Exclusive_Draw_Ticket}} **Selective Exclusive Draw Ticket** &rarr; {{Draw_Ticket}} **Draw Ticket** &rarr; {{Dia}} **Free Dia** &rarr; {{Dia}} **Paid Dia**

---

## Mechanics

### Rates

Brown Dust II relies on a simple draw system.

* Each Costume / Gear banner has fixed rates that are not changed based on the number of Draws you performed.
* There is no pity system as if guaranteeing featured Costume after obtaining the offrate, therefore you can lose to offrate multiple times in a row.
* There are things called "soft pity" — [Guaranteed Draw mechanic](#guaranteed-draws) and "hard pity" — [Draw Points mechanic](#draw-points-mechanic) that overall help you, a player, to obtain more costumes.

!!! question "Isn't this system greedy towards the players?"
    In a vacuum, a lack of hard guarantee on featured units seems unforgiving. However, given the generous 3% base 5★ rate, steady {{Draw_Ticket}} Draw Ticket income, and manageable dupe scaling, the overall economy is **F2P-friendly**.

!!! warning "To players from other gachas"
    As was stated, in Brown Dust II, <u>**rates do not gradually ramp up**</u>. **"Soft pity" refers to the flat guaranteed 5★ at 100 pulls, while "Hard pity" refers to the 200-point spark exchange.**

    For more explanation, read the sections below.

### Draw Points Mechanic

Each time you perform a single Draw in Pick-Up or specific Unique banners, **1 Draw Point** is obtained. It is a separate tracker designated to **each banner**.

For Pick-Up Banners, once you reach **200 Draw Points**, you can exchange them to obtain **Featured Costume / Gear**. Alternatively, you can exchange Draw Points for {{Powder_of_Hope}} **Powder of Hope** at a 1:1 ratio without any extra requirements.

To do that, simply press the "Exchange" button in the banner's menu. There is an additional confirmation window afterward, so do not be afraid of pressing it by accident.

!!! image "Image Guide"
    ![Exchange_guide](../assets/images/gacha/exchange.avif)

!!! question "Do Draw Points Carry Over? If no, are they wasted?"
    As said before, Draw Points are only for **individual** banners; therefore, **they do not carry over**, leaving you with converting excess points into {{Powder_of_Hope}} **Powder of Hope** as the only viable choice.

    ---
    
    You do not need to exchange {{Powder_of_Hope}} **Powder of Hope** manually; when the banner ends, you automatically gain the {{Powder_of_Hope}} **Powder** equal to the amount of Draw Points you had on those banners.

### Guaranteed Draws

Guaranteed Draw is a Draw that happens if you **fail to obtain ★5 Costume / ★5 {{UR_Grade}} Gear** 100 times in a row. This includes **any** Costume or Gear, not just featured.

To observe the count of the "soft pity", find the counter above the Draw Points counter. 

!!! image "Guaranteed Draw Counter"
    ![Soft Pity Counter](../assets/images/gacha/soft-pity.avif)

* Guaranteed Draw *usually* forces the Draw to be ★5 Costume or ★5 {{UR_Grade}} Gear, respectively, keeping original rates intact (therefore, for the most part, making a 50%/50% ratio). The only exception to it is **12-Pick Selective Draw**.
* Guaranteed Draw counter is **shared** across same **type** of banners, e.g. **Costume Pick-Up** banners. They are **different** between **Gear** and **Costumes**, as well as **Unique** banners.
* Once you obtain any ★5 Costume or ★5 {{UR_Grade}} Gear, the counter gets reset regardless of how many it has been on.

??? example "Technical details (Pity Resolution Order)"
    The 100th draw evaluates standard base rates before applying the guarantee.

    If the 100th pull rolls a 5★ naturally *(usually 3% base chance)*, the draw resolves against the standard banner rate table and resets the counter. The guaranteed pity mechanic only executes if the 100th pull fails its initial check *(usually 97% of the time)*, at which point the engine forces an outcome from the banner's designated safety table.

    While irrelevant for standard 50/50 banners, this priority order is a vital distinction for custom draw simulators and special pools (such as the 12-Pick Selective Draw), where the guaranteed drop table uses different internal weighting than the standard pool.

!!! tip "Pity Manipulation Strategy"
    Because the 100-count safety net is **shared across all active banners of the same type**, you can control where the guaranteed Costume or Exclusive Gear lands:

    1. Build your counter up to **99/100** using daily free pulls or your own earned pulls across active banners.
    2. Switch to the banner featuring the costume you actually want, and perform pull **100/100** there to trigger the 50/50 check on that specific featured unit or gear.
    
    *Note:* This does not prevent an off-rate outcome, but it ensures your 50% chance is focused entirely on the target costume rather than an unwanted duplicate.

---

## Standard (Pick-Up) Banners

Standard (Pick-Up) banners feature 1 Costume or Gear. Their duration is usually 2 weeks, but banners can also run for 1 or 4 weeks.

??? question "Why are Durations Different?"
    Duration is based mostly on external factors.

    * **1-week banners** are usually reserved for old Costumes that have not seen a rerun in a long time (or were not featured before).
    * **2-week banners** are the most common and reserved for new Costumes, as well as most reruns. 
    * **4-week banners** are reserved for **Limited Costumes** and Costumes featuring **Special / Prestige Skins**.

### Rates

Costume Pick-Up banner has a **3%** chance to give a ★5 Costume, with half of that (**1.5%**) being allocated for a featured Costume.

Gear Pick-Up banner has a bit more complicated system due to Rarity and Character dependency, but it still has a **1.5%** chance to get featured Gear.

??? abstract "More Detailed Rates"
    === "Costume Pick-Up"

        <div class="responsive-table-wrapper">
        <table class="data-table">
        <thead>
            <tr>
            <th>★5 (Featured)</th>
            <th>★5 (Off-rate)</th>
            <th>★4</th>
            <th>★3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td>1.5%</td>
            <td>1.5%</td>
            <td>14.0%</td>
            <td>83.0%</td>
            </tr>
        </tbody>
        </table>
        </div>
        
    === "Exclusive Gear"
        
        <div class="responsive-table-wrapper">
        <table class="data-table">
        <thead>
            <tr>
                <th>Character Base</th>
                <th>UR (Featured)</th>
                <th>UR (Off-rate)</th>
                <th>SR</th>
                <th>R</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="yellow">**★5 Characters**</td>
                <td>1.5%</td>
                <td>1.5%</td>
                <td>2.0%</td>
                <td>—</td>
            </tr>
            <tr>
                <td class="yellow">**★4 Characters**</td>
                <td>—</td>
                <td>2.5%</td>
                <td>8.5%</td>
                <td>17.0%</td>
            </tr>
            <tr>
                <td class="yellow">**★3 Characters**</td>
                <td>—</td>
                <td>4.0%</td>
                <td>16.0%</td>
                <td>47.0%</td>
            </tr>
        </tbody>
        </table>
        </div>

### Banner Specifics

* Each day, you get a **free Draw attempt** for **each active Pick-Up banner**. To quickly use them all, press the **"Bulk Free Draw"** button in the bottom left corner of the screen.

??? image "Image Guide"
    ![Bulk Free Draw](../assets/images/gacha/bulk-free-draw.avif)

* Banners can feature **Non-limited** and **Limited** Costumes / Gear. It is easy to distinguish them by the **"Special"** label for **Limited** Costumes / Gear.

??? image "Limited Costumes / Gear Display in a Gacha Screen"
    ![Limited Banners](../assets/images/gacha/limited-banners.avif)

* **Non-Limited** Costumes **usually** go in the {{Powder_of_Hope}} **Powder of Hope Shop** after the banner ends. This means that instead of spending excessive {{Draw_Ticket}} **Draw Tickets** on a last copy, you could **wait** and purchase the last copy **from the Shop** instead.

??? question "When Does a Costume NOT Enter the Powder of Hope Shop?"
    It happens if the Costume **is limited**, or if the costume was featured on a short **1-week banner**. 1-week reruns do not follow a guaranteed shop rotation and depend entirely on developer discretion.

### Pulling Guide

For the Costumes, refer to the [**Banner Recommendations**](https://zormolo.github.io/BD2-Banner-Recommendation/).

Recommended pull targets are primarily determined by skill [breakpoints](../misc/slang.md?term=Breakpoint). For most costumes, {{pl1}} is such a stopping point (due to -1 SP). However, sometimes you want to go {{pl5}} because it is a support or a personal preference.

When any Upgrade Level is mentioned, it does not necessarily mean obtaining it via Draw only; {{Powder_of_Hope}} **Powder of Hope Shop** and **Pub** **are also viable sources** to get specific Costumes, so plan your pulls while keeping these extra sources of the Costumes in mind.

{{ redirect_btn('https://zormolo.github.io/BD2-Banner-Recommendation/', 'Banners Recommendations', '#4caf50') }}

For the Exclusive Gear, **avoid pulling it**. Since only one copy is required throughout the whole game, there is no reason to rush Exclusive Gear, unless it is for a Collaboration Character (therefore, limited) or if you're actively ranking.

---

## Unique Banners

### (Newbie) Infinite Draw

This banner is available when you open the Gacha tab for the first time. This banner allows you to reroll an infinite number of times and confirm (claim) whichever 10-pull result you prefer.

!!! image "(Newbie) Infinite Draw"
    ![Newbie Infinite Draw](../assets/images/gacha/newbie_inf_draw.avif)

* The banner offers 5 Costumes and 5 Exclusive Gears.
* One Costume is guaranteed ★5 from a fixed pool of Costumes.
* Only **one** Costume can be ★5.
* No 5★ {{UR_Grade}} Gear is possible from the banner. The highest gear you can achieve is 5★ {{SR_Grade}}, 4★ {{UR_Grade}} and 3★ {{UR_Grade}}.

!!! tip "Pulling Guide {{ share_btn('inf') }}"
    ![The Curse Celia](../assets/images/faq/celia_illust.avif){ width="128" align=right }
    Target [The Curse Celia](https://browndust2.miraheze.org/wiki/The_Curse_Celia), regardless of whichever secondary characters or gear appear in the roll.
    
    She is a **late-game oriented investment**, so do not expect heavy impact in early progression. Nonetheless, you may find her useful for her **Absorption Skill** and **chainer capabilities** for **Last Night**.

    ---

    ??? image "Draw Example"
        ![Newbie Infinite Banner Example](../assets/images/gacha/newbie_inf_draw_2.avif)

    Other *viable*, although not recommended options: 

    * [Gentle Maid Anastasia](https://browndust2.miraheze.org/wiki/Gentle_Maid_Anastasia) — Good Physical [DPS](../misc/slang.md?term=DPS). You can pick her as an alternative, but Supports are higher in priority than DPS.
    * [Top Idol Helena](https://browndust2.miraheze.org/wiki/Helena/Top_Idol) — Defensive / Utility Support that is lower in priority than Offensive ones.
    * [The Lapis Witch Scheherazade](https://browndust2.miraheze.org/wiki/Scheherazade/The_Lapis_Witch) — Magical PvP-oriented pick, which is not great for a mostly PvE-oriented game.
    * [Piercing Magic Bow Eleaneer](https://browndust2.miraheze.org/wiki/Eleaneer/Piercing_Magic_Bow) — Physical PvP-oriented pick, which is not great for a mostly PvE-oriented game.

    Gear from this banner is not relevant — offered {{SR_Grade}} Exclusive Gear is falling behind once you have progressed into gear crafting.

    ---

    **Do not worry if you selected someone else**. Your choice here will not make or break account progression. You will naturally acquire off-rate copies over time, and a single +0 copy has minimal impact on long-term viability.

---

### Newbie Welcome ★5 Costume Guaranteed Draw

This banner is open for 14 days after account creation. It allows you to pick three Costumes, and on each 10th pull, you will receive one of the selected costumes.

Note that <u>**this is paid banner**</u> that uses {{Dia}} **Paid Dia**, **2000** per 10 draws, resulting in **6000** for the whole banner.

!!! image "Newbie Welcome ★5 Costume Guaranteed Draw"
    ![Newbie Welcome ★5 Costume Guaranteed Draw](../assets/images/gacha/newbie_paid_banner.avif)

* Banner selection is limited to Costumes that were released before **April 25th, 2024**. This means that the banner offers a scarce amount of Supports that were present during that time.

!!! tip "Pulling Guide {{ share_btn('nb') }}"

    **Purchasing this banner is entirely optional**. You can consider it a way to speed up the progression.

    If you are committed, choose [Adventurer of the Unknown Diana](https://browndust2.miraheze.org/wiki/Diana/Adventurer_of_the_Unknown), [B-Rank Idol Helena](https://browndust2.miraheze.org/wiki/Helena/B-Rank_Idol) and [Homunculus Lathel](https://browndust2.miraheze.org/wiki/Lathel/Homunculus).

    In case you have either of them listed at {{pl5}}, consider picking substitutes from the image below. 

    ??? image "Support List for Newbie Welcome ★5 Costume Guaranteed Draw"
        ![Newbie Welcome ★5 Costume Guaranteed Draw Banner Recommendations](../assets/images/gacha/nb-advice.avif)
   
---

### (Paid) Infinite Draw

Unlike the (Newbie) Infinite Draw, this special variant is only offered during major events, such as Anniversaries, Half-Anniversaries, or seasonal celebrations.

It is a <u>**paid cash banner costing ~$17 USD**</u> (or regional equivalent) to finalize and claim your selected 10-pull result.

!!! image "(Paid) Infinite Draw"
    ![Paid Infinite Draw](../assets/images/gacha/paid_inf_banner.avif)

* At least one ★5 Costume is guaranteed each time you draw.
* Multiple ★5 Costumes are possible to obtain within a Draw.
* The Costume pool is locked to units released before the banner's launch date (e.g., the banner shown above includes costumes released before September 10, 2026).
* The Costume pool does not include Limited Costumes.
* This Infinite Draw usually lasts for 4 weeks.

!!! tip "Pulling Guide {{ share_btn('paid-inf') }}"

    **Purchasing this banner is entirely optional**. This banner offers high acceleration value for newer accounts lacking core team buffers, but loses value for late-game players. Because the pool contains zero limited costumes, treat this purchase purely as account progression tempo rather than an exclusive collection opportunity.

    Nonetheless, if you want to purchase this banner, focus on obtaining **3 Supports** (such as [Pure White Blessing Refithea](https://browndust2.miraheze.org/wiki/Refithea/Pure_White_Blessing), [B-Rank Idol Helena](https://browndust2.miraheze.org/wiki/Helena/B-Rank_Idol), [Dark Saintess Liberta](https://browndust2.miraheze.org/wiki/Liberta/Dark_Saintess) or [Adventurer of the Unknown Diana](https://browndust2.miraheze.org/wiki/Diana/Adventurer_of_the_Unknown)).
    
    Keep in mind that **reaching relatively good rolls can be extremely time-consuming**, so you either have to spend a good amount of time rolling the banner, or could make a compromise at some point, for example, to 2 Supports & 1 DPS.

    ??? image "Support List for Infinite Draw"
        ![Paid Infinite Draw Recommendations](../assets/images/gacha/paid_inf_banner_advice.avif)

---

### 12PICK Golden Hand Selective Draw

This banner allows you to choose a pool of 12 Costumes. Purchasing the 10-pull guarantees that 3 Draws will be 5★ Costumes chosen exclusively from your selected pool, while also granting the exclusive 'Golden Hand' in-game title if you have not unlocked it previously.

It is a <u>**paid cash banner costing ~$17 USD**</u> (or regional equivalent).

!!! image "12PICK Golden Hand Selective Draw"
    ![12PICK Golden Hand Selective Draw](../assets/images/gacha/gh-12pick-banner.avif)

* The Costume pool is locked to units released before the banner's launch date (e.g., the banner shown above includes costumes released before September 10, 2026).
* The Costume pool does not include Limited Costumes.
* This 12PICK Selective Draw usually lasts for 4 weeks.

!!! tip "Pulling Guide {{ share_btn('gh-12p') }}"

    **Banner is optional**, but it is slightly better than [Paid Infinite Draw](#paid-infinite-draw). While you cannot infinitely change your outcome, restricting the results to a handful of useful Costumes is better for progressing.

    Either way, similarly to other banners, you should focus on **Supports**. If you are completely new, you can use the following choice: 

    * **Queen of Gluttis Granadair ({{Water}} Water)**
    * **Shrine Maiden of Purification Granadair ({{Water}} Water)**
    * **Water Park Queen Wilhelmina ({{Water}} Water)**
    * **Homunculus Lathel ({{Fire}} Fire)**
    * **Dark Saintess Liberta ({{Fire}} Fire)**
    * **Onsen Manager Liberta ({{Fire}} Fire)**
    * **Adventurer of the Unknown Diana ({{Wind}} Wind)**
    * **Magical Innovator Diana ({{Wind}} Wind)**
    * **Robin Hood Zenith ({{Wind}} Wind)**
    * **B-Rank Idol Helena ({{Light}} Light)**
    * **Pure White Blessing Refithea ({{Light}} Light)**
    * **Poolside Fairy Refithea ({{Light}} Light)**

    If you already own any of the recommended units at {{pl5}}, swap them out for the alternate utility supports listed in the Substitutes reference sheet below.

    ??? image "12PICK Golden Hand Selective Draw Recommendations"
        ![12PICK Golden Hand Selective Draw Recommendations](../assets/images/gacha/gh-12pick-advice.avif)

---

### Step-Up Draw

This banner allows you to perform 40 draws across four sequential stages to guarantee a copy of the featured Costume.

It is a <u>**Paid Dia banner**</u> requiring a total of **5000** {{Dia}} **Paid Dia** to complete all four steps.

!!! image "Step-Up Draw"
    ![Step-Up Draw](../assets/images/gacha/step-up.avif)

* This banner appears mostly for limited units or on half/full anniversaries and lasts as long as a [Pick-Up banner](#standard-pick-up-banners) for the same Costume.
* Each following step unlocks after purchasing the previous.
* The price for each step is not equal; Initial 10 Draws cost **2000** {{Dia}} **Paid Dia**, while the last ones cost **500** {{Dia}} **Paid Dia**. 
* For the first 30 Draws, there is a **1.5%** chance to obtain a featured Costume (similar to the [Pick-Up banner](#standard-pick-up-banners)). In the last 10 Draws, getting a featured Costume is guaranteed.
* The Costume pool does not include Limited Costumes.

!!! abstract "Steps Prices"

    * Step 1: **2000** {{Dia}} **Paid Dia**
    * Step 2: **1500** {{Dia}} **Paid Dia**
    * Step 3: **1000** {{Dia}} **Paid Dia**
    * Step 4: **500** {{Dia}} **Paid Dia**

!!! tip "Pulling Guide {{ share_btn('stepup') }}"
    **Step-Up banners are entirely optional**. While they were historically the primary source for spending {{Dia}} **Paid Dia**, modern seasonal events (such as the **Paid Dia Exchange**) often offer better value.

    If you decide to commit, commit to the **full clear** (all 4 steps), because initial 10 Draws are the most expensive ones and cost 40% of whole banner price while not providing guarantee copy.

---

### ★5 Costume Guaranteed Draw

These banners allow you to obtain a ★5 Costume from each Draw.

!!! image "★5 Costume Guaranteed Draw"
    ![★5 Costume Guaranteed Draw](../assets/images/gacha/anni-tix-banner.avif)

* These banners use **specific currency** — {{Third_Anniversary_S5_Costume_Draw_Ticket}} **★5 Costume Draw Tickets**.
* These banners are **permanent** as long as you have unspent currency ({{Third_Anniversary_S5_Costume_Draw_Ticket}} ★5 Costume Draw Tickets). Once you spend all Tickets, these banners vanish from the Draw menu.
* The Costume pool is locked to units released before the banners' launch date (e.g., the banner shown above includes costumes released before June 4, 2026).
* The Costume pool does not include **limited** Costumes.

!!! tip "Pulling Guide {{ share_btn('anni-banner') }}"

    Since {{Third_Anniversary_S5_Costume_Draw_Ticket}} **★5 Costume Draw Tickets** are given on special occasions in **limited** quantities, and each new Banner uses different **Costume Tickets** (for example, 2nd Anniversary / 3rd Anniversary ones), **there is no point in saving these tickets**. Using them immediately is **strongly recommended**.
    
    Moreover, the more you hoard these tickets, the bigger the chance of them awarding you {{Golden_Thread}} **Golden Thread** instead of a Costume, which is worse for the account progression.

---

### 1Pick Selective Draw

This banner allows you to select a Costume to draw, essentially creating a custom [Pick-Up banner](#standard-pick-up-banners).

!!! image "1Pick Selective Draw"
    ![1Pick Selective Draw](../assets/images/gacha/1pick.avif)

* You can only change your selected costume **up to 10 times total**. Confirming a costume selection consumes an attempt immediately, **even if you did not perform a single draw on that unit**.
* The Costume pool is locked to units released before the banner's launch date.
* The Costume pool does not include **limited** Costumes.
* The designated Costume has a rate of ~1.51% rate for Featured Costume, in comparison to 1.5% for [Pick-Up banner](#standard-pick-up-banners). Total rate for ★5 is 3%.
* This banner has **Draw Points** and own, separate **soft pity counter**.
* This banner allows the usage of {{Selective_Exclusive_Draw_Ticket}} **Selective Exclusive Draw Ticket**.
* The banner does NOT have **free daily draws**.
* The banner lasts for 8 — 12 weeks.

!!! tip "Pulling Guide {{ share_btn('1pick') }}"
    Generally speaking, this banner **is not worth using**, contrary to popular belief.

    If you want a short answer as to why, that is because other banners, in particular [12Pick Selective Draw](#12pick-selective-draw) and [Pick-Up banners](#standard-pick-up-banners), are better than it. 

    1Pick banner is good when you know the exact weakness of your current roster and you are trying to close that gap, but otherwise it is not as good as player can think it is. 

    For a more detailed breakdown, refer to the section below.

    ---

    The only few exceptions to not using 1Pick can be selecting Costume that is having rerun (and you are planning to obtain), or if you already possess the game knowledge to optimize your roster without a guide.

!!! warning "1Pick vs 12Pick / Pick-Up banners {{ share_btn('1pick-12pick-comparison') }}"

    **Reasons why 12Pick is better than 1Pick:**
    
    * 1Pick has **offrates**, which reduces the overall efficiency of the banner, while 12Pick only rolls off-rates when triggering the soft pity safety net.
    * 1Pick prioritizes fewer Costumes to pull, but in larger quantities (dupes). While it's not bad per se, Brown Dust II is still a **roster** game, and having multiple supports in a minimal "working" state is better compared to one overinvested support.
    * New players have worse game understanding even with guidance from different sources. That means it is easier to opt for questionable decisions. 
    * 12Pick, despite having no hard pity, still gives {{Powder_of_Hope}} **Powder of Hope**, which, in the long run, equals Costumes the same way 1Pick does.   

    ---

    **Reasons why Pick-Up banners are better than 1Pick:**

    * Normal Pick-Up banners are always accompanied by the event that awards {{Draw_Ticket}} **Draw Tickets** for obtaining featured Costumes from {{pl0}} to {{pl4}}. If you use 1Pick on a non-featured unit, you will not obtain these tickets immediately, which slows your progression to some degree.

---

### 12Pick Selective Draw

12Pick Selective Draw (the game's permanent Standard Banner) allows you to select 12 Costumes that exclusively share the entire 3.0% 5★ rate pool (0.25% each).

It is NOT [12Pick Golden Hand Selective Draw](#12pick-golden-hand-selective-draw) and can be pulled using ordinary resources.

!!! image "12Pick Selective Draw"
    ![12Pick Selective Draw](../assets/images/gacha/12pick.avif)

* You can change your selected Costumes at any time.
* The Costume pool is locked to units released before. New Costumes appear in 12Pick after their Pick-Up ends.
* The Costume pool does not include **limited** Costumes.
* All 12 Costumes have a 0.25% chance, resulting in a total of 3%. It is impossible to obtain off-rate except through soft pity.
* This banner tracks its own **Draw Points** and features a dedicated **soft pity** counter.
* The banner **does not have an exchange feature for specific Costumes**; instead, all Draw Points can be converted into {{Powder_of_Hope}} **Powder of Hope**.
* This banner allows the usage of {{Selective_Exclusive_Draw_Ticket}} **Selective Exclusive Draw Ticket**.
* The banner does NOT have **free daily draws**.
* The banner is available **permanently**.

!!! warning "Soft Pity in 12Pick Banner"
    If you reach a guaranteed ★5 Costume in the 12Pick banner, **you can obtain any non-limited ★5 Costume**, not just one of the chosen 12.

    **It is intended behavior**. You can check rates for Guaranteed ★5 Costume [here](https://browndust2.gitbook.io/probabilitydetails_en/other-probabilities/guaranteed-draw-pity#id-12pick-selective-draw-guaranteed-draw).

    Otherwise, during standard rolls, **it is impossible to obtain off-rate**, which makes this banner highly valuable.

!!! tip "Pulling Guide {{ share_btn('12pick') }}"

    **You should consider this banner from time to time.** Using {{Selective_Exclusive_Draw_Ticket}} **Selective Exclusive Draw Tickets** on this banner specifically is highly advised; however there are also cases you can use {{Draw_Ticket}} **Draw Tickets** as well.

    The best time to spend on this banner is when you think you have enough pulls to cover future releases for some time or when current banners are optional or skip.

    In selection, you should prioritize **supports**. There is no single ideal order to pick supports, but you could go with the following:

    * **Queen of Gluttis Granadair ({{Water}} Water)** (until {{pl5}})
    * **Shrine Maiden of Purification Granadair ({{Water}} Water)** (until {{pl5}})
    * **Water Park Queen Wilhelmina ({{Water}} Water)** (until {{pl4}})
    * **Homunculus Lathel ({{Fire}} Fire)** (until {{pl5}})
    * **Dark Saintess Liberta ({{Fire}} Fire)** (until {{pl5}})
    * **Onsen Manager Liberta ({{Fire}} Fire)** (until {{pl5}})
    * **Adventurer of the Unknown Diana ({{Wind}} Wind)** (until {{pl5}})
    * **Magical Innovator Diana ({{Wind}} Wind)** (until {{pl0}})
    * **Robin Hood Zenith ({{Wind}} Wind)** (until {{pl3}} or {{pl5}})
    * **B-Rank Idol Helena ({{Light}} Light)** (until {{pl5}})
    * **Pure White Blessing Refithea ({{Light}} Light)** (until {{pl1}} or {{pl5}})
    * **Poolside Fairy Refithea ({{Light}} Light)** (until {{pl3}} or {{pl5}})

    !!! image "Visual Costume Display"
        ![12-Pick Recommendations](../assets/images/faq/12-pick.avif)

    Once you have upgraded any primary targets to their recommended breakpoints, you can swap those with the following instead:

    * **Poolside Guardian Zenith ({{Wind}} Wind)** (until {{pl5}})
    * **Iron Monarch Wilhelmina ({{Water}} Water)** (until {{pl4}})
    * **Sunny Inn Hand Helena ({{Light}} Light)** (until {{pl5}})
    * **Red Riding Hood Rou ({{Darkness}} Darkness)** (until {{pl5}})
    * **Young Lady Blade ({{Darkness}} Darkness)** (until {{pl5}})
    * **Medical Club Teresse ({{Water}} Water)** (until {{pl5}})
    * **Shadowed Dream Sonya ({{Darkness}} Darkness)** (until {{pl4}} or {{pl5}})
    * **Miracle Marine Mamonir ({{Water}} Water)** (until {{pl5}})
    * **Heavenly Guardian Successor Glacia ({{Water}} Water)** (until {{pl4}})
    * **New Hire Seir ({{Darkness}} Darkness)** (until {{pl5}})
    * **Shadowed Bunny Eleaneer ({{Darkness}} Darkness)** (until {{pl4}})
    * **Retired Legend Olivier ({{Light}} Light)** (until {{pl4}})

    By the time you need a replacement for replacements, you should be able to understand the game slightly more to make your own choices. If you still struggle with that, do not hesitate to ask in the [Discord Server](https://discord.gg/tays83ew3N).

---

### Property Costume Guaranteed Draw

This banner allows you to select a specific **Property (Element)** and guarantees a random **★5 Costume** from that element on every draw.

!!! image "Property Costume Guaranteed Draw"
    ![Property Costume Guaranteed Draw](../assets/images/gacha/proptix.avif)

* This banner uses **specific currency** — {{Property_Selective_Draw_Exchange_Ticket}} **Property Selective Draw Exchange Ticket**.
* This banner is hidden by default but appears as soon as you have any {{Property_Selective_Draw_Exchange_Ticket}} **Property Selective Draw Exchange Ticket**. Using all the tickets will remove the banner from the Draw menu until you obtain more.
* You are allowed to pick from {{Water}} Water, {{Fire}} Fire, {{Wind}} Wind, {{Light}} Light and {{Darkness}} Darkness properties.
* Newly released non-limited Costumes are permanently added to their respective Property pool once their debut Pick-Up banner ends.
* You are **guaranteed** to obtain a ★5 Costume, but it will be **random** within the chosen Property, and you cannot influence this.
* The Costume pool does not include **limited** Costumes.

!!! tip "Pulling Guide {{ share_btn('proptix') }}"
    
    This banner is a good source to obtain Costumes. In most cases, you get 3 tickets monthly, and, usually, using them right away is better compared to hoarding. 

    At the beginning you can focus on getting decent upgrade level for [Refithea](https://browndust2.miraheze.org/wiki/Refithea)'s and [Helena](https://browndust2.miraheze.org/wiki/Helena)'s Costumes ({{Light}} **Light**), but, generally speaking, any Property is decent to pick. 

    Later on, focus on the Property that you have weaker supports in. 

    Even later on, when you have most of the units at {{pl5}}, focus on the Property that minimizes your chances of rolling excess +5 duplicates (converting into {{Golden_Thread}} **Golden Thread**), even if it means picking up units with barely any usage.

---

### 12Pick Exclusive Gear Selective Draw

This banner is similar to the regular [12Pick Selective Draw](#12pick-selective-draw), but for [Exclusive Gear](../progression/gear.md#exclusive-gear) instead.

!!! image "12Pick Exclusive Gear Selective Draw"
    ![12Pick Exclusive Gear Selective Draw](../assets/images/gacha/12pick-gear.avif)

* The banner is available mostly during anniversaries and half anniversaries or other special occasions.
* You can change your selected Gears at any time.
* The Gear pool is locked to the Gear released before the banner's launch date.
* The Gear pool does not include **limited** Gear (for Collaboration Units).
* All 12 Gear pieces have a 0.25% chance, resulting in a total of 3%. It is impossible to obtain off-rate except through soft pity.
* This banner tracks its own **Draw Points** and features a dedicated **soft pity** counter.
* The banner **does not have an exchange feature for specific Gear**; instead, all Draw Points can be converted into {{Powder_of_Hope}} **Powder of Hope**.
* This banner allows the usage of {{Selective_Exclusive_Draw_Ticket}} **Selective Exclusive Draw Ticket**.
* The banner does NOT have **free daily draws**.
* The banner usually lasts for **8 weeks**.

!!! warning "Soft Pity in 12Pick Exclusive Gear Banner"
    If you reach guaranteed {{UR_Grade}} ★5 Gear in the 12Pick Exclusive Gear banner, **you can obtain any non-limited {{UR_Grade}} ★5 Gear**, not just one of the chosen 12.

    **It is intended behavior**.

    Otherwise, during standard rolls, **it is impossible to obtain off-rate**, which makes this banner valuable.


!!! tip "Pulling Guide {{ share_btn('12pick-weapon') }}"

    As stated previously, **pulling Gear is not recommended**, unless you rank or want limited Gear for limited Characters (such as Collaboration ones). 

    Nonetheless, this banner can help you to speed up gathering Gear towards the late game, when you have most of the costumes upgraded to the {{pl5}}. 

    This banner eliminates the need to wait for individual gear reruns. However, because gear only requires a single copy, and you are forced to lock in 12 targets, the banner becomes inefficient once you need fewer than 12 weapons. Any remaining slots will be filled with unwanted weapons that dilute your chances of rolling the few pieces you actually want.

---

### Draw Gear

The **Draw Gear** banner serves as the permanent, uncurated standard pool for Character Exclusive Gear.

!!! image "Draw Gear"
    ![Draw Gear](../assets/images/gacha/draw-gear.avif)

* The banner contains all standard Exclusive Gears released to date. Newly introduced exclusive gear is permanently added after its debut Pick-Up banner.
* The Gear pool does not include **limited** Gear.
* This banner has its own **Draw Points** and shares a **soft pity** counter with gear [Pick-Up banners](#standard-pick-up-banners).
* The banner **does not have an exchange feature for specific Gear**; instead, all Draw Points can be converted into {{Powder_of_Hope}} **Powder of Hope**.
* The banner does NOT have **free daily draws**.
* The banner is available **permanently**.

!!! tip "Pulling Guide {{ share_btn('draw-gear') }}"

    **Avoid the banner**. It has no controllable gains, and aiming for random Exclusive Gear is just a bad strategy.

---

### SR / UR Exclusive Gear Guaranteed Draw

These two banners allow you to obtain UR / SR Exclusive Gear, respectively. They are permanent banners and are available at any time.

!!! image "UR Exclusive Gear Guaranteed Draw"
    ![UR Exclusive Gear Guaranteed Draw](../assets/images/gacha/ur_exclusive_gear.avif)

* The banners contain all standard Exclusive Gears released to date. Newly introduced exclusive gear is permanently added after its debut Pick-Up banner.
* The Gear pool does not include **limited** Gear.
* The banners use {{UR_Exclusive_Gear_Guaranteed_Draw_Exchange_Ticket}} **UR Exclusive Gear Guaranteed Draw Exchange Ticket** and {{SR_Exclusive_Gear_Guaranteed_Draw_Exchange_Ticket}} **SR Exclusive Gear Guaranteed Draw Exchange Ticket**, respectively.

!!! abstract "Pulling Rates"

    Gear rates are slightly more complex due to separation based on Character Rarity. 

    * ★5 Exclusive Gear: 15%
    * ★4 Exclusive Gear: 35%
    * ★3 Exclusive Gear: 50%


!!! tip "Pulling Guide {{ share_btn('ur-sr-gear') }}"
    
    Since these banners rely on specific Tickets to be pulled, you do not really need to have any strategy.

    While the {{UR_Grade}} banner has occasional upside (a 15% chance to hit a ★5 character's gear), the {{SR_Grade}} banner is completely obsolete — even top-roll {{SR_Grade}} exclusive weapons are strictly inferior to standard crafted {{UR_Grade}} {{IV}} gear.

<style>
.md-typeset a[target="_blank"]::after,
.md-typeset a[href^="http://"]::after,
.md-typeset a[href^="https://"]::after {
    display: none !important;
}
</style>