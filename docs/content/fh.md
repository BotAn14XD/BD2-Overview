---
comments: true
image: 
---
![Fiend Hunter](../assets/images/site-assets/index-pc-nav-19.avif){: .card-header-img }
#

Fiend Hunter is the activity revolving around defeating a Boss, that becomes stronger with each level. Defeating the boss successfully grands various rewards.

To access the gamemode, press the [Season Event](events.md) logo, then click the corresponding button.

??? image "Image Guide"
    ![Image Guide](../assets/images/fiend-hunter/fh-access-menu.avif)

---

!!! image "Fiend Hunter Menu"
    ![Fiend Hunter Menu](../assets/images/fiend-hunter/Fiend%20Hunter.avif)

---
## Fiend Hunter Schedule

Fiend Hunter is a **Seasonal** biweekly content. Each Fiend Hunter is separated into $2$ phases, lasting 1 week only: 
    
* **Preparation Period**, during which you can do **Practice battles** and **cannot** obtain Rewards.
* **Hunting Period**, during which you attack the Boss directly and gain Rewards based on your performance.

??? image "Event Schedule"
    ![Event Schedule](../assets/images/season-event/schedule.avif)

Fiend Hunter schedule completely aligns with [Season Events](events.md), or, to be more precise, Fiend Hunter **is a part** or Season Events.
{{ redirect_btn('content/events/', 'More about Season Events', '#e5b567') }}

---

## Boss

Each Season you fight a different Boss. Each Boss occupies only specific tiles of the battlefield grid within 3x4 field, similar to Regular Battles.
??? image "Example of the tiles that are occupied by the Boss"
    ![Fiend Hunter Occupied Tiles](../assets/images/fiend-hunter/FH_tiles.avif)
{{ redirect_btn('mechanics/battle/#grid-system', 'More about Grid System', '#e5b567') }}

You can also check the tiles by inspecting the Boss info in Fiend Hunter Menu.

??? image "Image Guide" 
    ![Image Guide](../assets/images/fiend-hunter/FH_tiles_2.avif)

### Boss Levels

Fiend Hunter Bosses have $25$ initial Levels you can freely choose between in both **Normal** and **Practice** Battles, but, after defeating the Level 25, you will be facing Level $26$, meaning, boss, in theory, has infinitely many Difficulty Levels.

Each new Level is progressively harder thanks to change in parameters such as  {{ HP }} **HP** and {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta}.

### Boss Stats
Each Boss has its own predetermined **Base Value**, **Initial Growth** and **Scale Growth** parameters for {{ HP }} **HP** and {{ATK}} **ATK**{.yellow} or {{MATK}} **MATK**{.magenta}. These three parameters determine Boss **Health** and **Attack** potential on each Difficulty Level.

**Initial Growth** is responsible for scaling immediately, starting from Level 2, while **Scale Growth** makes much more impact going higher the difficulty.

!!! example "Stat Formula"
    $\text{Value} = \text{round}[B \cdot (1+(L-1) \cdot R \cdot 0.01 \cdot L^S)]$

    * $\text{B} \rightarrow \text{Base Value}$
    * $\text{L} \rightarrow \text{Boss Level}$
    * $\text{R} \rightarrow \text{Initial Growth Parameter}$
    * $\text{S} \rightarrow \text{Scale Growth Parameter}$

??? example "Formula Explanations & Limitations"
    * **Rounding** in formula is following:
        * For {{HP}} **HP**, **rounding down to 3 significant figures** is applied. 
        * For {{ATK}} **ATK**{.yellow} and {{MATK}} **MATK**{.magenta}, **rounding to the nearest integer** is applied instead.
    * Parameters $\text{B}$ and $\text{S}$ are never changed based on the level. However, that does not apply to the $\text{R}$, that *can* be changed on Level $11$ and $14$.

{{ redirect_btn('https://docs.google.com/spreadsheets/d/1c8SuOk7aAy2ZWZ13SjM-spg9YJ9zcN4g1lTWmpaQhYI/edit?gid=614503852#gid=614503852', 'Stats Data', '#e5b567') }}
{{ redirect_btn('https://docs.google.com/spreadsheets/d/1c8SuOk7aAy2ZWZ13SjM-spg9YJ9zcN4g1lTWmpaQhYI/edit?gid=1989714867#gid=1989714867', 'Parameters Data', '#e5b567') }}

### Boss Skills

All the Bosses have two type of skills: **Basic** and **Conditional** Skills. You can check the Skills via inspecting the Boss in Fiend Hunter Menu, similar to the tiles.
??? image "Image Guide"
    ![Skills Boss Information](../assets/images/fiend-hunter/fh_skills.avif)

* **Basic Skills** are the ones that boss will definitely use during the fight.
    * Last Basic Skill is always causing **Instant Death**, preventing from playing for a long turn period.
* **Conditional Skills** are the ones that boss will use only if particular condition is met.
    * Conditional Skill can be triggered only fixed amount per battle.
    * This type of Skill will override the next Basic Skill as soon as condition is met.

# WORK IN PROGRESS