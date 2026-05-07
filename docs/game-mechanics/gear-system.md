---

description: A comprehensive guide to the Gear and Crafting systems in Brown Dust 2. Master gear progression, including grades, tiers, upgrade levels, and refinement scores. Learn expert strategies for substat rerolling, Alchemy material farming, and optimizing builds for all DPS and support character types.
comments: true
image: assets/images/site/gear-system-banner.png

---
# **Gear System & Crafting Guide — Brown Dust 2**
The Gear System is an important character progression system. It increases a character's stats, improving damage output or improving sustain on the battlefield.

There are **5 gear slots** available for your characters: {{Weapon}} **Weapon**, {{Armor}} **Armor**, {{Helmet}} **Helmet**, {{Accessory}} **Accessory** and {{Gloves}} **Gloves**.

Generally speaking, {{Weapon}} **Weapon**, {{Accessory}} **Accessory** and {{Gloves}} **Gloves** are considered to be offensive gear, while {{Armor}} **Armor** and {{Helmet}} **Helmet** are considered to be defensive gear.

![Gear Slots](../assets/images/gear-system/gear-slots.avif)

For each gear piece, there is at least 1 Basic Attribute (Main Stat) and 3 Options (Substats) which carry those additional stats.

Gear is obtainable via **Crafting** (which is the main source), **Event Shop** or by pulling in gacha *(Exclusive Gear only)*.

Gear has a lot of different layers, defining how good it actually is. These layers are **Grade (Rarity)**, **Tier**, **Upgrade Level**, **Upgrade Rank (Score)**, **Basic Attributes & Options**.

!!! tip "Looking for Build Advice?"
    Already know how the system works and just want to know what to craft or equip?
    
    **Jump straight to the [Crafting Guide](#crafting-guide) or [Gearing Guide](#gearing-guide)**.

---

## **Gear Grade (Rarity)**

There are a total of 4 grades (rarities) that gear can have:

* {{N_Grade}} **N Grade** 
* {{R_Grade}} **R Grade**
* {{SR_Grade}} **SR Grade**
* {{UR_Grade}} **UR Grade**

You can see the grade in the top right corner of each gear piece or to the right of the gear name if you decide to check it in more detail.
??? image "Image Guide"
    ![Grade Visual Explanation](../assets/images/gear-system/grade_display.avif)

!!! example "Grade difference"
    * The main difference is the **amount of stats each Grade gives**. N gives the least, UR gives the most.
    * The second difference is the **amount of Basic Attributes (main stats)** and/or their specifics. It is explained in more detail in [this chapter](#basic-attributes), although it is recommended to just follow the natural explanation without skipping other sections.

---

## Gear Tier
Each **Grade** can have different **Tiers**. There are a total of **4 Tiers** which are shown as **roman numbers** from {{I}} through {{IV}} for a crafted gear piece. The higher the number, the better.

* Exclusive Gear has no number, although its tier is {{IV}}.
* Event Shop Gear has no number either, although its tier is {{III}}.

!!! example "Another <u>very useful</u> way to check for gear Tier"
    You can check the gear tier by checking the amount of **stars**.

    * **Zero silver** stars mean the tier is {{I}}.
    * **One silver** star means tier is {{II}}.
    * **Two silver** stars means tier is {{III}}.
    * **Three silver** stars means tier is {{IV}}.
    * **One <u>gold</u>** star means it is an exclusive gear. 

??? image "Image Guide"
    ![Tiers Visual Explanation](../assets/images/gear-system/gear_tiers.avif)

!!! warning "Crafting RNG"
    When you craft gear, it has a set chance to get a specific tier:

    * {{I}}: **50%**;
    * {{II}}: **30%**;
    * {{III}}: **15%**;
    * {{IV}}: **5%**.

    Even though Tier {{IV}} is very rare, it provides much better stats compared to Tier {{I}}. It is fine to use Tier {{III}} gear, although with no huge investment into it. **You should avoid actively using Tier {{I}} and Tier {{II}}**.

---

## Gear Level

The next layer of Gear investment is its **Level**. Each level enhances **Basic Attribute** values.

Each Gear can be upgraded up to a total of 9 times, resulting in having a **+9 Gear piece**.

Each upgrade costs {{Gold}} **Gold** (price depends on the Grade and Upgrade Level) and has **a chance to fail**. If the upgrade fails, there is **no penalty or downgrade risk**.

!!! note ""
    For detailed info about success chances, check [**CatlessCat's sheet**](https://docs.google.com/spreadsheets/d/1m9PI5N6a_iHl1LM0Agub0L9i0BrlXeFE0k2_M7vQQC0/edit?usp=sharing).
    
    Alternatively, use [**Official Gitbook**](https://browndust2.gitbook.io/probabilitydetails_en/other-probabilities/gear-crafting-and-refining#upgrade-success-probability).

On **+3**, **+6** and **+9 Level**, Option (Substats) slots are opened.<br>Aside from unlocking Option slot itself, they enhance **Basic Attribute values** via Upgrade Scores, similar to Levels, although the +9 slot has way more impact compared to the +3 one. Each slot also receives the letter {{C}},{{B}},{{A}} or {{S}}, the functionality of which will be covered in the [next chapter](#gear-refinement).


!!! note ""
    **For detailed info about the mathematical side of upgrade values, check [this sheet](https://docs.google.com/spreadsheets/d/14S1ry3hblNeOZgmkk3VLdjNv8LERnrdzQ26V-ecc5Yk/edit?usp=sharing).**

??? image "Image Guide"
    ![Upgrade Feature Visual Explanation](../assets/images/gear-system/upgrade_view.avif)
    !!! warning "Level representation"
        As you can see from the picture, some gear pieces have their level in the preview, while others have a star in its place. Do not worry — that star is a natural extension of the Upgrade system and replaces the level indicator when you reach +9 automatically.

!!! warning "Time saving feature"
    To prevent exhaustion and to guarantee quick upgrade, press the **Repeat** button, set the slider to the max (or use the MAX button), then hit the **Upgrade** button, and, finally, press the {{Skip}} **Skip** button.
    ??? image "Image Guide"
        ![Upgrade Guide](../assets/images/gear-system/upgrade_guide.avif)
     
---

## ![Gear Refinement](../assets/images/gear-system/icons/score_system.avif){.icon-header} **Gear Refinement**

Gear Refinement comes right after Upgrades. When you reach +9 and all Options are unlocked, the **star with the number inside** will be unlocked as well. 

It is the so-called **Gear Score**, which represents the most important layer of enhancing values given by the gear.
Each of the refinement scores is represented by the letters {{C}}, {{B}}, {{A}} and {{S}}, with {{S}} being the best possible one.

As was mentioned earlier, each following Option slot has a bigger impact towards the overall score. **The weighted sum of slots gives the final score.**

* The Minimum Total Score is **6**, being {{C}}{{C}}{{C}}.
* The Maximum Total Score is **24**, being {{S}}{{S}}{{S}}.
* Increasing the score by 1 has the same **Basic Attribute** value increase as upgrading the gear by 1 level.

??? example "Detailed Score Explanation"
    * Each letter is assigned a number 1-4, with {{C}} receiving 1 and {{S}} 4 correspondingly.
    * Second and third letter bonus is multiplied by 2 and 3 correspondingly.
    * Each letter value is added towards the Total Score.
    !!! warning ""
        ![Gear Score Calculations](../assets/images/gear-system/score_calculation.avif)

??? tip "Interesting yet totally useless fact"
    * Scores from **6 to 11** are displayed with ![6-11 Score Star](../assets/images/gear-system/icons/score_6_11.avif "6-11 Score Star"){.icon} star.
    * Scores from **12 to 16** are displayed with ![12-16 Score Star](../assets/images/gear-system/icons/score_12_16.avif "12-16 Score Star"){.icon} star.
    * Scores from **17 to 20** are displayed with ![17-20 Score Star](../assets/images/gear-system/icons/score_17_20.avif "17-20 Score Star"){.icon} star.
    * Scores from **21 to 24** are displayed with ![21-24 Score Star](../assets/images/gear-system/icons/score_21_24.avif "21-24 Score Star"){.icon} star.

You can change the Gear Score you have by a process called Refinement. It uses {{Gold}} **Gold** and {{Refining_Powder}} **Refining Powder** to roll one of 81 possible scores ({{C}}{{C}}{{C}}, {{B}}{{C}}{{C}}, ... , {{S}}{{S}}{{S}}).

* <u>**You keep the best score obtained, meaning there is no possible downgrade for the gear**</u>.
* The higher the score, the lower the chances of it appearing. This becomes especially noticeable after score 18, when the chances decrease significantly, making maxed gear a whale-level challenge.
* Despite multiple possible letter combinations for the same score, they have no difference in Base Attributes value increase.

??? info "Probability Chances (for UR gear)"
    ![Gear Refinement](../assets/images/gear-system/bbs.avif)
    **Alternatively, use [Official Gitbook](https://browndust2.gitbook.io/probabilitydetails_en/other-probabilities/gear-crafting-and-refining#refinement-probability-by-upgrade-level), although keep in mind it uses a different way to describe the same percentages.**

!!! warning "Time saving feature"
    To prevent exhaustion and to do refinement much quicker, press the **Repeat** button, set the slider to the max (or use the MAX button), then hit the **Refinement** button, and, finally, press the {{Skip}} **Skip** button.

    It is advised to have the **"Ends once refining succeeds"** feature ON as it prevents you from overspending the powder. Although it means that upgrading gear to Score 18 will take a few cycles. 
    ??? image "**Image Guide**"
        ![Refinement Guide](../assets/images/gear-system/refinement_guide.avif)
     
---

## Gear Stats
### Basic Attributes
Different Gear pieces have different Basic Attributes, which define how good the gear actually is. You tend to use different gear for different purposes, so it is important to know what to use and when. 

* {{N_Grade}} and {{UR_Grade}} Gear have **1** and **2 Basic Attributes** respectively. These attributes are **not** rerollable.
* {{R_Grade}} and {{SR_Grade}} Gear have **2 Basic Attributes**, with Attribute 1 **fixed** and Attribute 2 **rerollable** via the refinement menu. The reroll options for Attribute 2 are always between "relevant stats": this means that offensive gear will only have offensive options and the same goes for defensive gear. Moreover, offensive gear will give options only relevant to the 1st Attribute in terms of damage type. 
* **Exclusive Gear** has **2 Basic Attributes** regardless of rarity, with Attribute 1 **swappable** between two relevant stats for no cost. Attribute 2 behaves similarly to {{R_Grade}} / {{SR_Grade}} gear.

You can check possible stats for each individual gear piece by pressing the ? in the refinement menu. 
??? image "Image Guide"
    ![Possible Basic Attributes for gear](../assets/images/gear-system/possible_options_check.avif)

### Options
**Options**, also known as **substats**, can be rerolled regardless of the gear's **Grade** or **Tier**. As was discussed above, there are a total of **3** Options, each giving some random stat. 

Similar to Basic Attributes, you can obtain mostly "relevant" stats only, although their variety is bigger compared to Basic Attributes; for example, defensive gear can roll offensive stats of the **same damage type** (DEF armor can roll ATK, MRES armor can roll MATK).

* Option **values** depend on the **Grade** and **Tier** of the gear.
* Option **values** DO NOT depend on the **Gear (Total) Score**.
* Option **values** DO NOT depend on the **Individual Refinement Score** of each **Option slot**. *(Having either {{C}} or {{S}} will **not** change the values)*

You can check the possible Option stats for each individual gear piece by pressing the ? in the refinement menu. 
??? image "Image Guide"
    ![Possible Options for gear](../assets/images/gear-system/possible_options_check2.avif)

## Options Reroll
As it was stated earlier, you can change the Options (and in some cases Basic Attribute 2) to the desired ones. To do that, click the ![Option Reroll](../assets/images/gear-system/icons/icon_optionreroll.avif "Option Reroll"){ .icon } in the Gear Menu.

??? image "Image Guide"
    ![Reroll Menu](../assets/images/gear-system/substat_menu_access.avif)

On the right side of the menu you can see the stats allowed to be rerolled.<br>
Each reroll uses currency — {{Gold}} **Gold** and either {{Refining_Stone}} **Refining Stones** or {{Refining_Crystal}} **Refining Crystals**. The initial price depends on the **Grade** of the gear.

* For {{R_Grade}} gear, only {{Refining_Stone}} **Refining Stones** can be used. 
* For {{SR_Grade}} and {{UR_Grade}} gear, both can be used, with {{Refining_Stone}} **Refining Stones** taking priority. They basically act as {{Refining_Crystal}} **Refining Crystals** at a 10:1 ratio. You cannot spend Crystals before depleting Stones first, although it is more convenient this way.

To do the reroll, press the **Option Refinement** button. After that, you're given a choice of **keeping previous stats *(Keep Option button)***, **taking new stats *(Confirm button)*** or **rerolling once more *(Retry button)***.

* You can leave your choice unconfirmed for up to 12 hours. After that, the game will keep the previous ones.

??? image "Reroll Image"
    ![Reroll Image](../assets/images/gear-system/reroll_confirm.avif)

!!! example "Locking Stats"
    Rerolling and praying to get 3 or 4 desired stats at once can be a lot to ask. With that in mind, you can **lock** the desired stat to prevent it from being rerolled. 
    
    To do that, press ![Lock Icon](../assets/images/gear-system/icons/icon_lock.avif){.icon} **Lock Icon** on the left of stat. Keep in mind that **this will increase currency consumption by the base amount for each stat locked, reaching x4 the price for 3 stats locked**.
    ??? image "**Price Dependency based on the amount of locked stats**"
        ![Price Dependency](../assets/images/gear-system/price_dependency.avif)

---

!!! abstract "Summary so far"
    Each gear piece has its own **Grade** and **Tier**. **Grades** vary from {{N_Grade}} to {{UR_Grade}}, while **Tiers** vary from {{I}} to {{IV}}.<br>**The higher the Grade and Tier are, the better the gear is.**<br>That means that {{N_Grade}} {{I}} gear is the worst, while {{UR_Grade}} {{IV}} Gear is the best (except Exclusive gear).

    ---

    Each Gear piece can be **upgraded to 9 levels**, **enhancing values** given by the gear and **unlocking Options** (substats).

    After you upgrade your gear to +9, you can **refine** it to obtain a **score** from **6** to **24**, which enhances its values further. The higher the score is, the better, but chances are slimmer. Only the best refinement is kept, you cannot downgrade the gear.

    ---
    
    Another unlock after +9 is **Options**, aka **substats**. They give extra stats which are rerollable into desired ones. Their values are fixed and depend only on gear **Grade** and **Tier**. Values **do not** depend on **Gear Score** in any way. 
---

## Special Gear
### Event Gear
In the **Season Event Shop** you can obtain special gear. It is essentially {{UR_Grade}} {{III}} and {{SR_Grade}} {{III}} Gear pieces, but they have some unique mechanics.

??? image "**Event Shop Menu; White border shows gears, yellow shows Upgrading material**"
    ![Eshop Menu](../assets/images/gear-system/eshop.avif)

* Event Gear has no Roman number, representing tier, but, as established earlier, it is Tier {{III}} due to the amount of stars.
* Event Gear does **not** require {{Gold}} **Gold** for upgrading its level. Instead, it uses a **corresponding Upgrading material** (different for each gear) and **has no fail chance**.
    * {{UR_Grade}} **Gear** uses **3** currency per level upgrade. (Total: **27**)
    * {{SR_Grade}} **Gear** uses **1** currency per level upgrade. (Total: **9**)
* Event Gear does **not** have a Refinement process at all; instead, the **Gear automatically gets a {{S}} Score for each Option slot**, resulting in a **Gear Score of 24**.

??? image "Visual Demonstration"
    ![Event Gear Upgrading Screen](../assets/images/gear-system/event_gear_upgrade2.avif)

Except for things mentioned above, Gear is **identical** to the gear of the same **Grade**. 

!!! tip "Advice regarding Event Gear"
    **Do NOT purchase {{SR_Grade}} Gear.**
    
    If you have **enough** currency and you bought more important stuff beforehand, you can purchase **{{UR_Grade}} Gear and <u>27</u> Upgrade 
    materials**. 

    You can keep buying them until the end game since they are better than craftable {{UR_Grade}} {{III}} for **Support Bonus** of **Last Night**.
    ??? image "**Quick Event Shop Priority Guide**"
        ![Event Shop Recs](../assets/images/gear-system/eshop_recs.avif)

---

### Exclusive Gear
**Exclusive (EX) Gear** is a type of gear obtainable **from gacha only**. It is displayed with **one gold star** instead of a **Tier**. 

As its name might suggest, this type of gear **can only be equipped on a specific character this gear is suitable for**. Similar to Event Gear, it also slightly differs from craftable gear. 

* <u>Each Exclusive gear gets an **Exclusive Attribute**, an **additional stat**.</u> Its value depends only on the **Grade** of the gear.
* Despite also not having a Roman number, each Exclusive gear inherits the stats of the {{IV}} Tier of a given Grade. That means, {{UR_Grade}} {{EX}} scales the same way {{UR_Grade}} {{IV}} does.
    * In very simple words, **{{EX}} Gear is the equivalent of an {{IV}}, but with an extra stat on top.**
* There are {{R_Grade}} {{EX}}, {{SR_Grade}} {{EX}} and {{UR_Grade}} {{EX}} Gears. {{R_Grade}} {{EX}} only exists for 3-4★ Characters, while the rest exist for any character.
* **There is exactly one exclusive gear for each character.** It can be any piece of gear, although *in most cases* it is {{Weapon}} **Weapon** / {{Accessory}} **Accessory** for DPS characters.

* **Basic Attribute 1** of the {{EX}} Gear is **swappable between two options** with no cost, while **Basic Attribute 2** is **rerollable**, similar to Options.

Except for things mentioned above, Gear is **identical** to the gear of the same **Grade**.

??? image "Exclusive Gear Reroll Menu"
    ![EX Gear Reroll Menu](../assets/images/gear-system/ex_gear_reroll.avif)

!!! example "EX Gear Impact"
    * **{{SR_Grade}} {{EX}} Gear is roughly equal to {{UR_Grade}} {{III}} Craftable Gear.**
    * **{{UR_Grade}} {{EX}} Gear gives ~10-20% more damage compared to {{UR_Grade}} {{IV}} Craftable Gear.**

!!! question "What do I do with duplicate Exclusive Gear for a character?"
    If you happen to get a second gear copy,

    * If it's a 5★ Character's gear, **keep 1 duplicate** in case you need another build and **dismantle** the rest. 
    * If it's 3★ or 4★ Character's gear, **dismantle** any extra dupe.
    * If it's {{SR_Grade}} Gear regardless of the character, **dismantle** it as well. 
        * Before committing to the dismantle, check related section [below](#gear-dismantle).

---

## ![Gear Crafting Icon](../assets/images/gear-system/icons/talent_bufficon_9_l.avif){.icon} **Crafting Gear**
When it comes down to **crafting the gear**, you need to use **Fred's** or **Layla's Crafting Field Ability**.

To do that, press the ![Field Ability](../assets/images/gear-system/icons/icon_fieldskill.avif "Field Ability"){.icon} **Field Ability** icon on the bottom of your screen and find either the characters mentioned above.

??? image "Image Guide"
    ![Field Ability Location](../assets/images/gear-system/crafting_ability.avif)

Alternatively, use **"Craft Gear"** button in the ![Gear Menu Icon](../assets/images/icons/icon_pictorialbook4.avif "Gear Menu"){ .icon } **Gear** section of {{Bag}} **Bag**.

* **Fred and Layla have no difference in terms of Ability, so you can use the one you want.**

In the menu, you can see all the gear you can possibly craft, sorted by rarity. You can click on any gear to check more details about it. 

??? image "Gear Crafting Menu"
    ![Gear Crafting Menu](../assets/images/gear-system/crafting_menu.avif)

To craft the Gear, you must have corresponding materials and {{Ability_Pill}} **Ability Pills**. You can check which resources are needed in the bottom left corner of the menu. In the same corner, you can also adjust the amount of the Gear you want to craft.

??? image "Individual Gear Crafting Menu"
    ![Individual Gear Crafting Menu](../assets/images/gear-system/crafting_menu2.avif)

!!! example "Ability Rank"
    You will not be able to craft {{UR_Grade}} gear right from the start. If you try to do so, you'll be met with **"Your Ability Skill Level is too low"** error pop-up.

    To fix this, you need to **upgrade** your Ability to the **Legendary** rank. For that, you need to **earn Ability EXP <u>by simply crafting gear</u> and upgrading Rank with Ability Book once you reach the EXP cap.**
    ??? image "Image Guide"
        ![Ability Rank Upgrade Guide](../assets/images/gear-system/abrank.avif)
    !!! tip "The best way to farm EXP"
        To get the EXP the most efficiently, **craft {{N_Grade}} or {{R_Grade}} gear** until you obtain **Legendary** Crafting Ability Rank. 

        **Avoid crafting {{SR_Grade}} Gear as it is not worth the resources spent.**

    !!! question "How to Obtain Ability Books?"
        In order to upgrade Ability, aside from EXP, you need {{S1_Ability_S_Book}} **Ability Books**.

        Here is where to obtain each of them:

        * {{S1_Ability_S_Book}} **★1 Ability S. Book**: Story Pack 3 *(Mist Man)* Shop.
        * {{S2_Ability_S_Book}} **★2 Ability S. Book**: Story Pack 3 *(Mist Man)* Shop.
        * {{S3_Ability_S_Book}} **★3 Ability S. Book**: Story Pack 10 *(Homunculus)* Shop / [Evil Castle](../content-packs/evil-castle.md) Shop.
        * {{S4_Ability_S_Book}} **★4 Ability S. Book**: [Evil Castle](../content-packs/evil-castle.md) Shop.

    !!! tip "Upgrade Settings Feature"
        You can press **"Upgrade Settings"** button in crafting menu to instantly upgrade and / or dismantle crafted gear. 

        It is most useful when it comes down to {{Refining_Powder}} **Refining Powder** farming using {{N_Grade}} gear.
        ??? image "Upgrade Settings Menu"
            ![Upgrade Settings Menu](../assets/images/gear-system/upgrade_settings_menu.avif)

---

## ![Alchemy Icon](../assets/images/gear-system/icons/talent_bufficon_8_l.avif "Alchemy"){.icon} Alchemy
In case you were wondering where to obtain materials for your crafting, the answer is mostly **Alchemy**. It is the **Field Ability** of Scheherazade. 

To access her ability, you need to repeat the same steps as for crafting, but picking Scheherazade instead. 
??? image "Image Guide"
     ![Field Ability Location](../assets/images/gear-system/alchemy_ability.avif)
    
In the Alchemy menu, you can make more advanced materials out of more common ones with the help of {{Ability_Pill}} **Ability Pills**. Each common material has its own tree for upgrading. 

Upon clicking the individual item, you can set the desired amount of material you want to obtain and do the alchemy.

??? image "Individual Material Alchemy Menu"
    ![Individual Material Alchemy Menu](../assets/images/gear-system/alchemy_menu2.avif)

!!! example "Ability Rank (again)"
    Similarly to crafting, you will not be able to make high-end materials immediately. To do that, you need to upgrade **Ability Rank** as well. 
    
    You can follow the same steps as described above in [Crafting section](#crafting-gear).
    !!! tip "Best way to farm EXP"
        For Alchemy, it does not really matter much since you're going to use almost every material eventually. Thus, try to craft the least expensive stuff first, for example: 

        * {{Plain_Leather}} **Plain Leather** into {{Fine_Leather}} **Fine Leather**.
        * {{Plain_Fabric}} **Plain Fabric** into {{Fine_Fabric}} **Fine Fabric**.
        * {{Peat}} **Peat** into {{Coal}} **Coal**.

!!! tip "![Alchemy Icon](../assets/images/gear-system/icons/icon_alchemy_red.avif "Alchemy QoL"){ .icon } An Important QoL Feature"
    When you want to craft or do alchemy and have no materials, sometimes you can see the button under specific material with the {{Ability_Pill}} **Ability Pills** cost. 

    This is **not** buying them — **this is the cost of Alchemy** for this amount of material. By pressing the button, the game does needed Alchemy for you. 

    * **This still uses all materials required to do Alchemy.**
    ??? image "Detailed Image Cost Explanation"
        ![Alchemy QoL Image Explanation](../assets/images/gear-system/detailed_qol_alch_explanation.avif)

---

## Gear Menu
You can access all your gear via the Gear Menu, located in the **second** tab (![Gear Menu Icon](../assets/images/icons/icon_pictorialbook4.avif "Gear Menu"){ .icon }) of {{Bag}} **Bag**. 
??? image "Gear Menu Image"
    ![Gear Menu Image](../assets/images/gear-system/gear-location.avif)

In this menu, you can check specifics about any gear you have, as well as access Refinement Menu etc. 

### See Details Feature
The **See Details** feature is a toggle that allows you to see more information about gear on page, more particularly, its values. 

It can be useful but as time passes by, you start understanding the gear without needing to toggle that feature on.
??? image "Image of See Details Feature ON"
    ![See Details Feature](../assets/images/gear-system/see_details.avif)
### Compare Feature
The **Compare** feature allows you to compare stats of two gears of your choice. It displays the difference in the Options and / or Main Attributes values.

First clicked gear becomes the "main" one, and any following gear is compared to the main. You can freely change compared gear by pressing different gear you want.

That being said, the inability to properly display a meaningful comparison, especially when it comes down to substats, makes it a nearly useless feature. 
??? image "Image of Compare Feature"
    ![Compare Feature](../assets/images/gear-system/compare_feature.avif)

### Custom Marks
The Custom Marks feature allows you to mark specific gear. To do that, press "Custom Marks Settings" in the gear preview tab. 
??? image "Image Guide"
    ![Custom Mark Guide](../assets/images/gear-system/custom_mark1.avif)

This Mark is customizable, allowing you to choose 15 icons, 110 numbers ($0, 1, \dots , 100$ & $ 00, 01, \dots, 09$) and 6 colors, resulting in 750 different unique combinations. 

??? image "Custom Mark Settings Menu"
    ![Custom Mark Settings Menu](../assets/images/gear-system/custom_mark2.avif)

### ![Gear Filter](../assets/images/gear-system/icons/icon_filter.avif "Gear Filter"){.icon} Filter
Aside from filtering by the **slot** the gear is for, you can also use the **Filter** feature to enhance this process even further. To access the menu, press the ![Gear Filter](../assets/images/gear-system/icons/icon_filter.avif "Gear Filter"){.icon} **Gear Filter** icon in the top right corner of the Gear Menu.
??? image "Filter Menu"
    ![Gear Filter Menu](../assets/images/gear-system/filter_menu.avif)

* **Parts:** Filter for a gear slot ({{Weapon}} **Weapon**, {{Armor}} **Armor** etc.)
* **Category:** Filter for **Exclusive**, **Fiend (Event)** and **Craftable gear**.
* **Rank:** Filter for a **Grade** ({{N_Grade}} — {{UR_Grade}})
* **Rarity:** Filter for a **Tier** ({{I}} — {{IV}})
* **Upgrade Level:** Filter for Gear Level ($\ge +3$, $\ge +6$, $\ge +9$)
* **Upgrade Score:** Filter for Gear Score ($\le 10$, $\le 17$, $\ge 18$)
* **Basic/Exclusive Attribute:** Filter for Basic or Exclusive Attribute, offering any of the possible stats to choose from.

### Sorting
With the **Sorting** feature, you have the ability to sort the gear according to your preference. 
Possible Sorting options:

* By Highest / Lowest Grade.
* By Recently / Oldest Acquired.
* By Highest / Lowest Upgrades.
* By Highest / Lowest ATK, ATK%, Magic ATK, Magic ATK%, HP, HP%, DEF, Magic Resist, Crit Rate, Crit DMG.
* With / Without Custom Mark First.

??? image "Sorting "With Custom Mark First" (left) vs "By Highest Grade" (right)"
    ![Different Sortings](../assets/images/gear-system/sorting.avif)

### Upgrade All
The **Upgrade All** feature allows you to bulk upgrade the gear **level**. To do that, select the gear needed, press $\checkmark$ and set up upgrade settings. 
??? image "Image Guide"
    ![Upgrade All Feature](../assets/images/gear-system/upgrade_all.avif)

!!! tip "Easier Selection"
    Similar to the filter, you can choose the gear more easily. To do that, click on the three dots button near $\times$ and $\checkmark$. 

    In this menu, you can choose the **Grade**, **Fiend (Event) Gear**, **Tier (Rarity)** for crafted gear and character's exclusive gear.
    ??? image "Filter Showcase"
        ![Upgrade All Filter Showcase](../assets/images/gear-system/filter_upgrade_all.avif)

!!! warning ""
    You can only upgrade the **level**. It means that to change the refining score, you need to go to each individual gear piece. 

### Select Gear
Select Gear is a feature that allows you to bulk dismantle the gear. 

It behaves similarly to the **Upgrade All** feature.
??? image "Image Guide"
    ![Select Gear Feature](../assets/images/gear-system/select_gear.avif)

!!! tip "Easier Selection"
    The filter for picking gear here is similar to the Upgrade All feature, with the sole exception of one more toggle: **Include Upgraded Gear**.
    ??? image "Filter Showcase"
        ![Select Gear Filter Showcase](../assets/images/gear-system/filter_select_gear.avif)

* This feature will not allow you to dismantle **locked** or **equipped** gear.
 
---

## ![Dismantle Icon](../assets/images/gear-system/icons/icon_decomposition.avif){.icon-header} Gear Dismantle

Dismantle is a process to get rid of gear pieces in exchange for {{Refining_Powder}} **Refining Powder**, {{Refining_Stone}} **Refining Stones** or {{Refining_Crystal}} **Refining Crystals**.

* {{Refining_Stone}} **Refining Stones** are obtained from {{R_Grade}} Gear only.
* {{Refining_Crystal}} **Refining Crystals** are obtained from {{SR_Grade}} and {{UR_Grade}} Gear.
* {{Refining_Powder}} **Refining Powder** amount depends on the **Grade** of the gear and **Upgrade Level**. 
* {{Refining_Stone}} **Refining Stones** / {{Refining_Crystal}} **Refining Crystals** amount depends on Gear **Tier (Rarity)**.

!!! abstract ""
    To check the exact values, refer to [**Catless Cat's sheet**](https://docs.google.com/spreadsheets/d/1m9PI5N6a_iHl1LM0Agub0L9i0BrlXeFE0k2_M7vQQC0/edit?usp=sharing).

To do the dismantle, it is better to use the [**Upgrade All**](#upgrade-all) or [**Select Gear**](#select-gear) Features, described above.

!!! example "Dismantle Advice"
    Since {{Refining_Powder}} **Refining Powder** gain depends on **Upgrade Level**, before dismantling, upgrade your gear to **+7**. 
    
    This way, you get the most efficient {{Refining_Powder}} **Refining Powder** amount {{Gold}} **Gold**-wise.

!!! question "What do I do with duplicate Exclusive Gear for a character?"
    Check [Exclusive Gear section](#exclusive-gear).

---

## Crafting Guide

As a new player, you should prioritize **offensive** gear instead of **defensive**. To put it simply, it is fine to run a glass cannon strategy for the story, as long as you evaporate everything on Turn 1. 

As was mentioned above, offensive gear is <u>**mostly**</u> {{Weapon}} **Weapon**, {{Accessory}}**Accessory** and {{Gloves}} **Gloves**. 

The whole crafting guide essentially comes down to your current needs. Here's an example of what your progression can look like as a player who never touched crafting:

!!! example "Crafting Guide"
    1. Use the code **WAITING4LEGEND** to obtain {{UR_Grade}} {{III}} {{Venomous_Touch}} **Venomous Touch**.
    2. Craft {{N_Grade}} or {{R_Grade}} Gear to upgrade [**Ability Skill**](#crafting-gear).
    3. Once you upgrade Crafting Ability to Legendary, obtain {{UR_Grade}} {{III}} {{Weapon}} **Weapon** <!--({{Travel_Gods_Friend}} **Travel God's Friend**{.magenta} / {{Evil_Dragons_Blade}} **Evil Dragons Blade**{.yellow})--> and {{UR_Grade}} {{III}} {{Gloves}} **Gloves** for your Main DPS. <!--({{Dragon_Scales_Protection}} **Dragon Scales Protection**{.magenta} / {{Shackle_of_Treachery}} **Shackle of Treachery**{.magenta} / {{God_Kings_Silver_Arm}} **God-King's Silver Arm**{.yellow} / {{Prime_Authority}} **Prime Authority**{.yellow})-->
    
        !!! question "How do I decide what exactly to craft?"
            Decide by the team you're running. A proper team utilizes either {{Physical}} **Physical**{.yellow} or {{Magical}} **Magical**{.magenta} Damage type.

            * If you utilize both damage types, it is better to ask for the help in [**Discord**](https://discord.gg/browndust2), since it's most likely not a good one. 
            
            <br>
            When it comes down to the {{Weapon}} **Weapon**, it means crafting {{Evil_Dragons_Blade}} **Evil Dragon's Blade**{.yellow} for the {{Physical}} **Physical**{.yellow} DPS and {{Travel_Gods_Friend}} **Travel God's Friend**{.magenta} for the {{Magical}} **Magical**{.magenta} one. 
            
            Other weapons are usually niche ones and are not necessary for a new player to worry about.  
            <br>
            The same applies to the {{Gloves}} **Gloves**, meaning {{God_Kings_Silver_Arm}} **God-King's Silver Arm**{.yellow} / {{Prime_Authority}} **Prime Authority**{.yellow} for the {{Physical}} **Physical**{.yellow} DPS and {{Dragon_Scales_Protection}} **Dragon Scales Protection**{.magenta} / {{Shackle_of_Treachery}} **Shackle of Treachery**{.magenta} for the **Magical**{.magenta} one.

            * {{God_Kings_Silver_Arm}} **God-King's Silver Arm**{.yellow} and {{Shackle_of_Treachery}} **Shackle of Treachery**{.magenta} are **generally better** for a **new player** and are still used for some DPS in late game, while {{Prime_Authority}} **Prime Authority**{.yellow} and {{Dragon_Scales_Protection}} **Dragon Scales Protection**{.magenta} are used more in the **late game**, but could be **less powerful at the start**. 
            
            Either way, you will use **both gloves types**, so it is **up to you what to choose**.

    4. Craft one more {{UR_Grade}} {{III}} {{Venomous_Touch}} **Venomous Touch**, {{Weapon}} **Weapon** and {{Gloves}} **Gloves** for the second DPS of the team.
    5. Move onto crafting one or two sets of the {{UR_Grade}} {{IV}} offensive gear, following the same pattern as in 4th point, starting from {{Venomous_Touch}} **Venomous Touch**.
    6. Craft 2 {{UR_Grade}} {{III}} {{Armor}} **Armor** and {{Helmet}} **Helmet** pieces each. 

        !!! question "What {{Armor}} Armor and {{Helmet}} Helmet should I craft?"
            Generally speaking, armor usage depends on the enemy. 
            
            That means crafting {{Invulnerable_Armor}} **Invulnerable Armor**{ .yellow }, {{Helm_of_Carnage}} **Helm of Carnage**{ .yellow } or {{Fiend_Guard}} **Fiend Guard**{ .magenta } and {{Radiant_Wisdom}} **Radiant Wisdom**{ .magenta } sets. 

           The rest of the armor types are more niche so it's not really worth investing in them as a new player.

    7. Craft {{UR_Grade}} {{IV}} Gear of the opposite Damage type for the second team.
    8. Craft whatever you feel necessary. 
        * {{Accessory}} **Accessory**, in particular {{Venomous_Touch}} **Venomous Touch** should be the highest priority overall, followed by {{Gloves}} **Gloves**, then {{Weapon}} **Weapon** and {{Armor}} **Armor**.
            * Note that {{Weapon}} **Weapons** take less priority later in the game due to being mostly replaced by **Exclusive Gear**, so you will not need that much of it compared to {{Gloves}} **Gloves**. On the contrary, {{Armor}} **Armor** and {{Helmet}} **Helmets** are required in large numbers when it comes down to 3 teams in **Fiend Hunter** on high difficulty levels.

---

## Gearing Guide

When it comes down to gearing a character, you should understand that there are 6 types of characters in the game. 

1. **Standard DPS**, which utilize their own {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} to perform actions.
    * *Example: Nebris, Olivier, Blade.*
2. **Fixed Damage DPS**, which deal **Fixed Damage** to the enemy.
    * *Example: Justia, Alec*
3. **HP-reliant DPS**, which use {{HP}} **own HP** to do damage. 
    * *Example: Granhildr (Boo Ghost), Mamonir.*
4. **Enemy HP-reliant DPS**, which in order to deal damage, use {{HP}} **enemy HP**.
    * *Example: Angelica, Rou (Nature's Claw).*
5. **Stat-Dependent Supports**, which benefit from some stats to increase the buff to allies.
    * *Example: Diana (Anti-Dystopia), Rou (Red Riding Hood).*
6. **Other Supports**, which do not have offensive capabilities, and whose skills do not rely on anything said above.
    * *Example: Liberta, Refithea, Helena.*

For all of these types the build you want is different.
<div class="tab-align" markdown>

=== "Standard DPS"
    Standard characters rely on a mix of {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} and {{CritDMG}} **Crit DMG** to deal DMG. 

    This usually means builds like:

    * {{Evil_Dragons_Blade}} **Evil Dragon's Blade**{.yellow} $+$ {{Venomous_Touch}} **Venomous Touch** $+$ {{Prime_Authority}} **Prime Authority**{.yellow};
    * {{Travel_Gods_Friend}} **Travel God's Friend**{.magenta} $+$ {{Venomous_Touch}} **Venomous Touch** $+$ {{Dragon_Scales_Protection}} **Dragon Scales Protection**{.magenta};
    * {{Evil_Dragons_Blade}} **Evil Dragon's Blade**{.yellow} $+$ {{Venomous_Touch}} **Venomous Touch** $+$ {{God_Kings_Silver_Arm}} **God-King's Silver Arm**{.yellow};
    * {{Travel_Gods_Friend}} **Travel God's Friend**{.magenta} $+$ {{Venomous_Touch}} **Venomous Touch** $+$ {{Shackle_of_Treachery}} **Shackle of Treachery**{.magenta}.

    {{UR_Grade}} **Exclusive Gear** can replace any gear piece in these builds, as was mentioned earlier. 

    !!! question "Stats Amount"
        You should aim for 2000 {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} and 600 {{CritDMG}} **Crit DMG** as a baseline for this type of DPS.  

    Some DPS like Eclipse *might* use another {{Weapon}} Weapon to achieve the best damage, but, generally speaking, it only matters for minmaxing.<br>If you still want to craft the best gear ever possible, check [Gear Calculator](#gear-calculator) section. 
    
    When it comes down to {{Armor}} **Armor**, and {{Helmet}} **Helmet**, there are a few combinations:

    * {{Invulnerable_Armor}} **Invulnerable Armor**{ .yellow } $+$ {{Helm_of_Carnage}} **Helm of Carnage**{ .yellow } if enemy deals {{Physical}} **Physical**{.yellow} damage
    * {{Fiend_Guard}} **Fiend Guard**{ .magenta } $+$ {{Radiant_Wisdom}} **Radiant Wisdom**{ .magenta } if enemy deals {{Magical}} **Magical**{.magenta} damage
    * {{Immortal_Golden_Armor}} **Immortal Golden Armor**{ .yellow } $+$ {{Helm_of_Death}} **Helm of Death**{ .yellow } if enemy deals {{Physical}} **<u>Fixed, True or Consumed</u> Physical**{.yellow} damage
    * {{Hellfire_Robe}} **Hellfire Robe**{ .magenta } $+$ {{Crown_of_Galaxy}} **Crown of Galaxy**{ .magenta } if enemy deals {{Magical}} **<u>Fixed, True or Consumed</u> Magical**{.magenta} damage
    
=== "Fixed Damage DPS"
    Since Fixed Damage **cannot crit**, there is no reason to invest in {{CritDMG}} **Crit Damage**.

    Although, it is worth mentioning that this type of DPS is heavily underperforming and **not worth building whatsoever**.

    Therefore, the most used builds are the following:

    * {{Peerless_Javelin}} **Peerless Javelin**{.yellow} $+$ {{Prime_Authority}} **Prime Authority**{.yellow};
    * {{Demons_Forbidden_Book}} **Demon's Forbidden Book**{.magenta} $+$ {{Dragon_Scales_Protection}} **Dragon Scales Protection**{.magenta}.

    {{Accessory}} **Accessory** can be {{Ring_of_the_Lake}} **Ring of the Lake** or {{Charming_Gaze}} **Charming Gaze**, since it provides at least something more valuable such as {{HP}} HP, compared to {{Venomous_Touch}} **Venomous Touch** with {{CritDMG}} **Crit DMG** stats only.

    {{Armor}} **Armor** and {{Helmet}} **Helmet** choices follow the same logic as for [Standard DPS](#__tabbed_1_1).

=== "HP-reliant DPS"

    Since these DPS rely on {{HP}} **HP** to deal damage, their main stats should be {{HP}} **HP** and {{CritDMG}} **Crit DMG**. 

    Therefore, builds are:

    * {{Immortal_Golden_Armor}} **Immortal Golden Armor**{ .yellow } $+$  {{Helm_of_Death}} **Helm of Death**{ .yellow } $+$ {{Venomous_Touch}} **Venomous Touch** if enemy deals {{Physical}} **Physical**{.yellow} damage;
    * {{Hellfire_Robe}} **Hellfire Robe**{ .magenta } $+$ {{Crown_of_Galaxy}} **Crown of Galaxy**{ .magenta } $+$ {{Venomous_Touch}} **Venomous Touch** if enemy deals {{Magical}} **Magical**{.magenta} damage.

    {{Weapon}} **Weapon** can be either {{Evil_Dragons_Blade}} **Evil Dragon's Blade**{.yellow} or {{Travel_Gods_Friend}} **Travel God's Friend**{.magenta} regardless of damage type character deals, since its value is in the {{CritDMG}}  **Crit DMG** only.

    {{Gloves}} **Gloves** have no impact on the character aside from Options (Substats), so using any is fine. 

    !!! question "Wouldn't {{Charming_Gaze}} **Charming Gaze** be a better {{Accessory}} Accessory?"
        {{Charming_Gaze}} **Charming Gaze** indeed provides both {{HP}} **HP** and {{CritDMG}} **Crit DMG**, however, due to diminishing returns, impact on {{HP}} **HP** is usually less compared to {{CritDMG}} **Crit DMG**.
        
        That means unless you have some heavy bonuses to {{CritDMG}} **Crit DMG** *(for example, Night of Death Mamonir self-buff combined with Red Riding Hood Rou and The Gluttonous Refithea for tremendous $+725\%$ {{CritDMG}} **Crit DMG**)*, {{Venomous_Touch}} **Venomous Touch** is simply better. 


=== "Enemy HP-reliant DPS"
    Since this type of DPS relies on the enemy, there's nothing else to raise except {{CritDMG}} **Crit DMG** to gain extra damage. 

    Thus, build consists of:

    * {{Evil_Dragons_Blade}} **Evil Dragon's Blade**{.yellow} $+$ {{Venomous_Touch}} **Venomous Touch**;
    * {{Travel_Gods_Friend}} **Travel God's Friend**{.magenta} $+$ {{Venomous_Touch}} **Venomous Touch**.

    There is no difference which {{Weapon}} **Weapon** out of the two listed above you use, since the characters do not scale from {{ATK}} **ATK**{.yellow} or {{MATK}} **MATK**{.magenta}.

    {{Gloves}} **Gloves** have no impact on the character except Options (Substats), and neither do {{Armor}} **Armor** and {{Helmet}} **Helmet**. Follow advice from [Standard DPS](#__tabbed_1_1) tab regarding armor. 

=== "Stat-Dependent Supports"

    These supports scale their buff depending on their own stats.

    Currently there are only 2 examples of this in the game:

    1. **Anti-Dystopia Diana**, which generates **Energy Guard** based on own {{MATK}} **MATK**{.magenta};
    2. **Red Riding Hood Rou**, which generates **Energy Guard** based on own {{HP}} **HP**.

    It is not hard to figure out the builds for either of them: 

    * {{Demons_Forbidden_Book}} **Demon's Forbidden Book**{.magenta} $+$ {{Dragon_Scales_Protection}} **Dragon Scales Protection**{.magenta} for **Diana**;
    * {{Immortal_Golden_Armor}} **Immortal Golden Armor**{ .yellow } $+$  {{Helm_of_Death}} **Helm of Death**{ .yellow } $+$ {{Charming_Gaze}} **Charming Gaze** if enemy deals {{Physical}} **Physical**{.yellow} damage for **Rou**;
    * {{Hellfire_Robe}} **Hellfire Robe**{ .magenta } $+$ {{Crown_of_Galaxy}} **Crown of Galaxy**{ .magenta } $+$ {{Charming_Gaze}} **Charming Gaze** if enemy deals {{Magical}} **Magical**{.magenta} damage for **Rou**.

=== "Other Supports"
    
    Most supports **do not** scale with gear. That means their main job is to survive rather than deal some damage.

    Overall, their build is similar to [Standard DPS](#__tabbed_1_1), with sole exception that both offensive and defensive gear equipped can be worse compared to the rest of the team.

!!! question "What about {{CritRate}} Crit Rate? Is it useless?"
    In PvE, yes. There are plenty of supports making your crit rate high enough, and game modes like **Fiend Hunter** have easy conditions to achieve 100% Crit.

    The only PvE usage for {{CritRate}} **Crit Rate** is Floors 41-50 of the ![Tower of Jealousy Icon](../assets/images/evil-castle/icon_devilcastle_4.avif){.icon} [**Tower of Jealousy**](../content-packs/evil-castle.md#tower-of-jealousy) and the ![Tower Of Wrath Icon](../assets/images/evil-castle/icon_devilcastle_3.avif "Tower of Wrath"){.icon} [**Tower of Wrath**](../content-packs/evil-castle.md#tower-of-wrath).

!!! question "What about Substats (Options)? Which do I want?"
    Generally speaking, it, again, depends on the type of character you're building.

    * **Standard DPS** benefit from {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} and {{CritDMG}} **Crit DMG** split;
    * **Fixed Damage DPS** solely benefit from {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta};
    * **HP-reliant DPS** rely on {{HP}} **HP** and {{CritDMG}} **Crit DMG**;
    * **Enemy HP-reliant DPS** want only {{CritDMG}} **Crit DMG**;
    * **Stat-Dependent Supports** want corresponding stat;
    * **Other Supports** are fine with whatever.

    As for the split (ratio) of said Options, it's better to use [Gear Calculator](#gear-calculator) **if you want the precise answer**.
    
    If you, however, are fine with rough advice, setting up {{CritDMG}} **Crit DMG** on pieces that are swappable between DPS (mostly {{Armor}} **Armor**, {{Helmet}} **Helmet** and specifically {{Venomous_Touch}} **Venomous Touch**) and filling the remaining Options with another stat isn't a bad choice.

    Alternatively, use [Character Builds](https://dotgg.gg/brown-dust-2/characters/) made <u>**only**</u> by **IceKane**.
</div>
## Gear Calculator 
To use the Gear Calculator, use the [Souseha's Database](https://browndust2-wiki.souseha.com/en/option-calculator).

This calculator is made to calculate the most efficient Options (substats), although it can somewhat work for general gear as well. 

![Gear Calculator](../assets/images/gear-system/gear_calc.avif)

To do the calculations, do the following steps:

1. Select the necessary character;
2. Choose specific Gear in case you want to make some of them fixed;
3. Choose different Gear Grade, if necessary;
4. Pick External buffs, including {{CritDMG}} Crit DMG and **Property DMG**;
5. Press Auto Calculate.

??? image "Image Guide"
    ![Gear Calculator Guide](../assets/images/gear-system/gear_calc_guide.avif)

You will receive a table with builds, sorted by best damage dealt with **Advantage**.
In this table, you can see the gear, [bond](../character-progression/potential-liberation.md), substat amount for each stat and finalized stats. 

It is worth mentioning that **Damage** isn't the actual Damage you will deal in-game but rather a metric to determine how good a build is.

![Gear Calculator Results](../assets/images/gear-system/gear_calc_results.avif)

---

## Crafting Resources Farm

* {{Refining_Powder}} **Refining Powder**: **Events**, **Event Shop**, ![Dismantle Icon](../assets/images/gear-system/icons/icon_decomposition.avif){.icon} **Dismantling Gear** *(mostly {{N_Grade}} Grade)*.
    * Use [**Powder Calculator**](https://browndust2-wiki.souseha.com/en/powder-calculator) to calculate the most efficient way to grind the {{Refining_Powder}} **Refining Powder**.
* {{Refining_Crystal}} **Refining Crystal**: **Event Shop**, **Golden Colloseum Shop**, ![Tower Of Salvation Icon](../assets/images/evil-castle/icon_roguelike.avif){ .icon } [**Tower of Salvation**](../content-packs/evil-castle.md#tower-of-salvation), ![Dismantle Icon](../assets/images/gear-system/icons/icon_decomposition.avif){.icon} Dismantling {{SR_Grade}} and {{UR_Grade}} Gear.
* {{Ancient_Crystal}} **Ancient Crystals**: **Events**, **Event Shop**, **Golden Colosseum Shop**, ![Tower Of Salvation Icon](../assets/images/evil-castle/icon_roguelike.avif){ .icon } [**Tower of Salvation**](../content-packs/evil-castle.md#tower-of-salvation), ![Tower Of Pride Icon](../assets/images/evil-castle/icon_devilcastle_2.avif){ .icon } [**Tower of Pride**](../content-packs/evil-castle.md#tower-of-pride), **Last Night**.
* {{Gold_Ore}} **Gold Ore**: **Hunting Grounds**, **Map Absorption**, **Events**.
* {{Hardwood}} **Hardwood**: **Hunting Grounds**, **Map Absorption**, **Events**.


---

## Related Links

* [Option Calculator — Brown Dust 2 Database by <u>souseha</u>](https://browndust2-wiki.souseha.com/en/option-calculator)
* [Official Probabilities Gitbook](https://browndust2.gitbook.io/probabilitydetails_en/other-probabilities/gear-crafting-and-refining)
* [Brown Dust II Sheets by <u>BotAn</u>](https://docs.google.com/spreadsheets/d/14S1ry3hblNeOZgmkk3VLdjNv8LERnrdzQ26V-ecc5Yk/edit?usp=sharing)
* [Brown Dust II Sheets by <u>CatlessCat</u>](https://docs.google.com/spreadsheets/d/1m9PI5N6a_iHl1LM0Agub0L9i0BrlXeFE0k2_M7vQQC0/edit?usp=sharing)
* [Gear — Brown Dust 2 Wiki](https://browndust2.miraheze.org/wiki/Gear)
* [Powder Calculator — Brown Dust 2 Database by <u>souseha</u>](https://browndust2-wiki.souseha.com/en/powder-calculator)
* [Character Builds — dotgg.gg](https://dotgg.gg/brown-dust-2/characters/)
* [Alternative Gear Calculator by <u>Kane</u>](https://docs.google.com/spreadsheets/d/1-NAV4NWIWbzjgljz04iG1i8AETjU_S9YPm4QzJ_NRCY/edit?usp=sharing) *(no longer maintained)*
* [BD2 - The Tourist's Sheet](https://docs.google.com/spreadsheets/d/1E8eaUt-rgjAdunxYQPMDgqdI3-vE1S3MGfg0e_uNFc0/edit?usp=sharing) *(no longer maintained)*
* [Official Brown Dust II Discord](https://discord.gg/browndust2)

<!--
Weapons: 
{{Evil_Dragons_Blade}} {{Hammer_of_Thunder}} {{Peerless_Javelin}} {{Travel_Gods_Friend}} {{Eye_of_the_Destroyer}} {{Demons_Forbidden_Book}} 
Armor: 
{{Invulnerable_Armor}} {{Scale_of_the_Sea_God}} {{Immortal_Golden_Armor}} {{Fiend_Guard}} {{Deaths_Shroud}} {{Hellfire_Robe}} 
Helmet:
{{Helm_of_Carnage}} {{Undefeated_Glory}} {{Helm_of_Death}} {{Radiant_Wisdom}} {{Solar_Brilliance}} {{Crown_of_Galaxy}}
Accessory:
{{Warmth_of_the_Brazier}} {{Pinnacle_of_Aesthetics}} {{Promise_of_Harmony}} {{Venomous_Touch}} {{Ring_of_the_Lake}} {{Charming_Gaze}}
Gloves:
{{God_Kings_Silver_Arm}} {{Rebellion}} {{Prime_Authority}} {{Ring_of_Fury}} {{Dragon_Scales_Protection}} {{Shackle_of_Treachery}}
 -->