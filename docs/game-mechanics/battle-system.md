---
description: Brown Dust II Battle System Overview
---
# **Battle System**

Brown Dust II is a turn-based strategy in which you have ability to position your characters, as well as choose character's skills in order to defeat the enemies.

![Battle](../assets/images/battle-system/battle_system_1.avif){ loading="eager" }

---

## **Basics**

!!! example "Turns mechanic"
    * For all PvE content, you attack on **odd turns (1, 3, 5, ...)**, while enemy attacks on **even turns (2, 4, 6, ...)**.
    * During turns, you don't have to do anything; characters use skills automatically; **all preparation (positioning, skills choices) must be made pre-turn**.
    * You can make those preparations only **pre-turns**. Enemy turn is followed instantly after yours.
    * Turn progression only goes after you confirm your choices with "Turn X Battle" button in the bottom right corner of the battle screen.

---

## **Battlefield**

!!! absract "Grid System"
    * In general content (such a Story or [Evil Castle Towers](../content-packs/evil-castle.md)), you have ability to use **5 characters** on the field.
    * Field is a <u>**3x4 rectangular grid**</u>, in which you can place your characters however you like.
        * To swap character positioning, click and drag the chibi model of a character to the needed tile.
    !!! warning ""
        **Guild Raid** offers **5x5 square grid** and 7 characters, while **Fiend Hunter** uses **irregular grid**, but same 5 characters per team.<br>Golden Colosseum, on the other hand, has field changing depending on season from **3x3 square** to **5x5 square** with different amount of characters allowed.
    ??? note "3x4 Grid Image"
        ![3x4 Grid Image](../assets/images/battle-system/3x4_field.avif)

!!! abstact "Targetting Logic"
    Before understanding where would your character attack land, you need to understand how character targets the enemy.

    * Each costume has own **Range** — tiles that are affected by the action of the costume. 
    * For each costume (except supports with ![All icon](../assets/images/battle-system/icons/icon_all.avif "ALL Range"){.icon} Range), there is **Main Target** which is displayed by ![Main Target Icon](../assets/images/battle-system/icons/icon_main_target.avif "Main Target Icon"){.icon} down arrowhead.<br>**Main target is the one that actually gets targeted by your character, and rest AoE impact is calculated based on position of that Main Target.**

    ---

    As for Main Target, there are two main types of determining one.

    * First is **Very Front**, meaning your character will target the closest enemy in the same column.
    * Second is **Vault**, meaning your character will target **second** closest enemy in the same column, "vaulting" over first one. 
        * If there's only one enemy in the column, it will be targeted instead.

    You can check Target type and Costumes AoE either in Compainion tab or directly in the battle by clicking the character card. 

    ??? note "Image Guide"
        ![Main Target & AoE](../assets/images/battle-system/target_aoe.avif)

!!! question "Advanced Targetting Logic"
    There are few ways one can change their targetting logic from "normal" one.

    * Having **Taunt** or **Concentrated Fire** status effects make you attack the enemy with that status effect regardless of your attack type (Very Front, Vault).
    * **Target Avoidance** status effect makes your enemy to not target your character if there are other options on the field.

    * **If there is no enemy in the same column as your character, column on the right (to the character) takes priority instead. Thus, it is possible to attack the enemy on the most right column from the most left one.**
        * If there is no enemy in the right column either, left one takes priority.  
    ??? note "Showcase Image"
        ![Targetting Logic](../assets/images/battle-system/targetting.avif)


!!! example "Chain Mechanic"
    **Every time the enemy or boss tile is hit, 1 chain stack is applied.** Chains increase damage by 10% per each chain stacked on enemy. So, attack on enemy with 1 chain will have 110% damage compared to attack with no chains beforehand, and enemy with 5 chains will have 150% damage compared to no chains beforehand.<br>**Chains are very important for content such as Fiend Hunter and Guild Raid.**

    * Poolside Guardian Zenith increases those 10% to maximum of 20% for the single tile.
    * Chains last for 1 turn and are reset after, except some seasons of [**Golden Colosseum**](../content-packs/golden-colosseum.md).
    * Chains have cap of 100, except [**Last Night**](../content-packs/last-night.md).
    * Chains increases are added into same multiplier, thus it is a buff with diminishing returns.<br><br>
    * Effect called **Chain Reiforcement** <u>**adds +1 chain per hit**</u>. 
    !!! question "Example"
        * **The Cursed Celia** without any buffs **hits 7 times** and **provides 7 chains**.
        * **The Cursed Celia** with buff from **Masquerade Bunny Celia** (1 Chain Reinforcement) **provides 14 chains** instead.
        * **The Cursed Celia** with buffs from **Masquerade Bunny Celia** and **Pure White Blessing Refithea** (2 Chain Reinforcement) **provides 21 chains** instead.

---

## Team Setup

As said above, you can freely change positioning of characters and their order before your turn. These are important features to maximize your damage while minimizing enemy one.

* To change the position, drag chibi model of a character to desired tile.
* To change the order of characters, use [Swap Order]( #__tabbed_2_2 ) feature or it's quick ![Replace Shorcut Icon](../assets/images/battle-system/icons/icon_change_shortcut.avif "Replace Shortcut"){ .icon } shortcut

!!! question "Why does it matter?"
    * Some supports have **limited Range / Aura**, meaning you need to fit other units within that range to recieve buff *(like Medical Club Teresse, Adventure of the Unknown Diana, Refithea)*
    * Enemy layout can require DPS on different column for better AoE coverage
    * Enemy can be too strong for some characters to survive but fine for others within same team.
    
    ---

    * Usually supports should go before DPS to maximize your damage, however not every support is *just* a support, meaning order sometimes is required to be changed.
    * Some unique conditional abilities such as of Laid-Back Lifeguard Nebris require fine tuning the team order to receive better buff.

---

## In-Battle Information
In the battle, you can obtain a lot of information about your units and enemies. Moreover, there are a lot of small QoL features which ease your understanding of the battle, as well as mechanics which may be useful for completing the stages overall.
!!! abstract "Character / Enemy skills, stats and status effects"
    * To access the information about **skills**, press on either chibi model or card, and press the skills under "Basic Attack" and "Knockback" options to learn more about them on top of the screen.<br>When you do so, you can view **raw damage** (with no calculated impact from actions in the turn) and highlighted **area of effect** on the field.

        * If, instead of damage, K.O is displayed, it means raw damage is enough to kill the opponent.
        * {{ Magical }} Magic Damage is displayed in **magenta**{ .magenta } color and {{Physical}} Physical is displayed in **yellow**{ .yellow }. 

        * <u>**This way, you can switch actions for your characters as well.**</u>

    ??? note "Skills screenshot"
        ![Skills screenshot](../assets/images/battle-system/skills_view.avif)

    !!! warning "Skills Cooldown"
        Each costume has some cooldown, **during which you cannot use it again**. Cooldown for any costume is displayed in its description, and active cooldown is displayed in place of a costume button, covering it. 
        ??? note "Image Display"
            ![Cooldown Display](../assets/images/battle-system/Cooldown.avif)

    * To access the information about **stats**, press on the chibi / card, then press ![Plus Icon](../assets/images/battle-system/icons/icon_plus2.avif "Detailed Character information"){.icon} plus icon in the top corner of the screen *(left for your units, right for enemies)*.<br>Displayed information includes all stats **at the given moment** (with all **current** buffs applied), gear and [bond](../character-info/potential-liberation.md).
    ??? note "Stats screenshot"
        ![Stats screenshot](../assets/images/battle-system/stats_window.avif)
    * To access the information about **status effects**, do the same thing except instead of clicking on the plus, click on the icons right below, such as ![Taunt Icon](../assets/images/battle-system/icons/bufficon_26.avif "Taunt Status Effect"){ .icon } (which is the Taunt effect) or others.
    ??? note "Status Effects screenshot"
        ![Status Effects](../assets/images/battle-system/status_effects.avif)

!!! example "Property"
    Property is displayed in 3 ways.

    * First, it is shown **near character name as a icon** *(![Water](../assets/images/battle-system/icons/elementicon1_1.avif){.icon} Water, ![Fire](../assets/images/battle-system/icons/elementicon2_2.avif){.icon} Fire, ![Wind](../assets/images/battle-system/icons/elementicon3_3.avif){.icon} Wind, ![Light](../assets/images/battle-system/icons/elementicon4_4.avif){.icon} Light, ![Darkness](../assets/images/battle-system/icons/elementicon5_5.avif){.icon} Darkness and ![Neutral](../assets/images/battle-system/icons/elementicon6_6.avif){.icon} Neutral)*. 
    * Second, it is displayed as a **light tint on the character's card**. According to the property, tint is changed to resemble main color of the property.
    ??? note "Tint display: All 5 properties on our side and Water & Fire on the enemy"
        ![Tint Display](../assets/images/battle-system/property-tint.avif)
    * Third, it is displayed **as glow under character / enemy** whenever **they are going to use the ability (skill)**. Similar to tint in cards, this glow also changes the color depending on property, but is more bright in a sense. 
    ??? note "Glow display: Light, Water, Fire and Darkness"
        ![Glow Display](../assets/images/battle-system/glow_effect.avif)
    
    ---

    * Property **advantage / disadvantage** also is displayed **during skill / damage preview**, and are shown as ![Property Advantage](../assets/images/battle-system/icons/prop_adv.avif "Property Advantage"){.icon} and ![Property Disadvantage](../assets/images/battle-system/icons/prop_disadv.avif "Propety Disadvantage"){.icon} accordingly. If you have neither advantage nor disadvantage, no icon will show up, similar to attacking neutral character.
    ??? note "Advantage, disadvantage and basic damage display"
        ![Adv_Disadv display](../assets/images/battle-system/property-preview.avif)

!!! tip "Knockback"
    Knockback is one of possible actions for a character for a turn. It exists in some skills, but, generally speaking, every character has a knockback option regardless. **It allows you to move enemy on the battlefield to create more comfortable setup for your DPS.**<br>There are few rules to it:
    
    * Each **character** has different knockback for 1 tile and applied to 1 enemy. Furthermore, there are some **costumes** that can target more enemies or have bigger distance.
    * Knockback **always** deal 1 DMG to the Main Target no matter the buffs applied.
    * If the tile to which you try to knockback into is occupied by enemy or tombstone, knockback will not take effect.
    * If the basic knockback results in an enemy colliding with another, latter one recieves damage equal to 25% Max HP of **knocked back enemy**. Different costumes which utilize knockback will have greater numbers.
    * Knockback shares the same **damage type** as character; meaning, **Diana** will have {{ Magical }} **Magical Damage** from knockback, and **Teresse** will have {{ Physical }} **Physical Damage**.
    * Knockback damage <u>**(for the one bumped INTO)**</u> **is affected by Crit (Rate / DMG), Property (dis)advantage (DMG / Resist), DEF/MRES, Augmentation / Enemy Vulnerability, Chains and Weak Point bonuses**.
    * Knockback damage <u>**(for the one bumped INTO)**</u>, as any other HP-related skill, has 50k cap taken before applying any other buffs. Means, if knocked back enemy's HP is 2,000,000, only 50k will be taken into calculations instead of expected 2m.
    * Knockback adds Chain to main target, similar to basic attack, although the one bumped into DOES NOT recieve a chain stack.
    * Knockback damage <u>**(for the one bumped INTO)**</u> cannot be evaded. However, Main Target with Evade active **cannot** be knocked back. 
    * In Fiend Hunter / Guild Raid, you cannot knockback (move) boss tiles. Also, some enemies have knockback immune which negates knockback action on them completely.
    ??? note "Knockback showcase"
        ![Knockback screenshot](../assets/images/battle-system/knockback.avif)
        !!! question "Knockback damage"
            **62,500 damage in the first image is shown due to cap of 50k HP, mentioned above, mulitplied by 125% (Teresse Skill %)**.<br>
            $50 000 \times 1.25 = 62 500$

!!! abstract "Targetting Lines" 
    Pretty small and slightly underappreciated feature that tells you who is given character targets and by whom they are targeted.

    * **Green lines** are related to actions from **teammates / your characters**, aka supports. 
    * **Red lines** are related to **enemies who will hit your character** with their skill in the following round
    * **Colorful lines** are related to **main target of an attack**. Their color depends on property (see above).
    ??? note "Targetting Lines display"
        ![Targetting Lines display](../assets/images/battle-system/target_lines.avif) 

!!! example "Tombstones"
    **Tombstone is created when character on the field dies (becomes fatigued) in a place of that character.**

    * Tombstones are created only for initial units on the battlefield. That means that summons do not create tombstones.
        * The only exception for this rule are explosives which do not leave tombstone upon being destroyed.
    * Self-destruct skills, as well as death from counter creates the tombstone on the place of where character was last pre action.
    * Tombstone cannot be knocked back.
    * Tombstones prevents enemies to pass through them (with knockback skills)
    * Tombstones do not suffer damage / deal damage to knocked enemies. 
    ??? note "Tombstones on the field"
        ![Tombstones](../assets/images/battle-system/tombstones.avif) 

---

## **Battle UI**
![Top Part of UI](../assets/images/battle-system/UI_top.avif)
<div class="tab-align" markdown>
=== "![Environmental Icon](../assets/images/battle-system/icons/icon_environment.avif){ .icon-list }"
    ### **Environmental Effects** { #__tabbed_1_1 }
    This icon itself does not mean anything, but next to this icon all **environmental effects** are listed. They can be (but not limited to): 

    * ![Collection Bonus Icon](../assets/images/battle-system/icons/bufficon_1000.avif){ .icon } **Collection Bonus**
    * ![Death Time Icon](../assets/images/battle-system/icons/bufficon_72.avif){ .icon } **Death Time Effect**
    * ![Evil Castle Environmental Effects](../assets/images/battle-system/icons/bufficon_81.avif){ .icon } **[Evil Castle](../content-packs/evil-castle.md) Environmental effects**

=== "![Auto Skill Icon](../assets/images/battle-system/icons/icon_autoskill.avif){ .icon-list }"
    ### **Auto Skill** { #__tabbed_1_2 }
    This features automatically picks the costume to activate in the following turn.

    !!! example ""
        * **It tries to activate costumes in order of characters in a team (from first to the last).**
            * It also tries to activate costumes shown in Compainion / Pre-battle screens first, meaning it will keep turn 1 settings almost every time.
        * **If you do not have enough SP, skill (costume) will be not picked.**
        * **If you do have SP but for cheaper costume only, that costume will be picked instead.**

    To reselect costume choice, simply click on the character and choose different costume. 

    Overall this feature is considered to be a time-saver, since setting up skills yourself is way bigger hustle. Aside of that, it is flexible feature which doesn't lock your selected skill order, so you should have no issues.

=== "![Auto Battle Icon](../assets/images/battle-system/icons/icon_autobattle.avif){ .icon-list }"
    ### **Auto Battle Feature** { #__tabbed_1_3 }
    This feature allows you to complete battles automatically. 

    !!! example ""
        * **It locks your input from the battle completely, so in case you want to change anything, you must disable auto-battle first.**
        * It uses initial positioning and Auto Skill Feature.
        * It has a small countdown before launching the battle. 
    It is **NOT** recommended to use Auto Battle, because 

    * It takes longer time than actually just pressing battle button with no preparation
    * It does not care about the enemy and positioning, meaning you will likely run into issues sooner or later.
    * <u>**Auto Battle does not teach you how to be a good playere.**</u>

=== "![Game Speed Icon](../assets/images/battle-system/icons/icon_speed.avif){ .icon-list }"
    ### **Game Speed Feature** { #__tabbed_1_4 }
    With that button, you can change the speed your battles are going at.<br>**Minimum is x1, maximum is x3**.
    
    To switch, simply press the button few times.

=== "![Autofeed Icon](../assets/images/battle-system/icons/icon_autofood.avif){ .icon-list }"
    ### **Autofeed Feature** { #__tabbed_1_5 }
    This feature allows to heal minor damage by consuming cooked (and raw) food

    While it sounds good on paper and no longer requires people go to the Inn, it is simply not worth the result. 

=== "![Pause Icon](../assets/images/battle-system/icons/icon_pause.avif){ .icon-list }"
    ### **Pause Feature** { #__tabbed_1_6 }
    Quite self-explanatory feature allowing to make a pause during your battle.

    Here, you can:

    * Adjust Skill cutscenes display
    * Change Volume settings
    * Check ![Statistics Icon](../assets/images/battle-system/icons/icon_conditions.avif){ .icon } Battle Statistics
    * **Restart the battle or previous turn**
        * *You cannot rollback to previous turn in [**Tower of Salvation**](../content-packs/evil-castle.md#tower-of-salvation).*
    * Run away from the battle.

    ??? note "Pause Menu Image"
        ![Pause Menu Image](../assets/images/battle-system/pause_menu.avif) 
---

![Bottom Part of UI](../assets/images/battle-system/UI_bottom.avif)
<div class="tab-align" markdown>
=== "![Replace](../assets/images/battle-system/icons/icon_pictorialbook1.avif){ .icon-list }"
    ### **Replace Feature** { #__tabbed_2_1 }
    Feauture allowing you to replace your characters during battle preparation.
    
    To replace a character, pick it from the list and tap on the character you want to replace.
    ??? note "Image Guide"
        ![Replace Guide](../assets/images/battle-system/replace_guide.avif)
    !!! example ""
        * You can **filter characters** to find the needed ones faster by using **Property Filter** on top or filter button on the top as well.
        * In case you need **specific knockback**, you can check it via icon ({{ Knockback }}) on each character.
        * You can also **add characters instead of replacing** in case you do not have max amount on the field. In this case, **click on empty grid cell** with chosen character to place them.
        * **You cannot replace characters on Turn 3 onwards, except [Tower of Salvation](../content-packs/evil-castle.md#tower-of-salvation).**
    ### **Borrow Feature** { #__tabbed_2_1 }
    In some fights, you can use your Friend Support units to help you beat the fight.<br>
    The idea is completely the same with the exception of pressing one more button (![Support Character Icon](../assets/images/battle-system/icons/icon_mercenary.avif "Support Character"){.icon}).
    ??? note "Image Guide" 
        ![Friend Support Replace Guide](../assets/images/battle-system/friend_support_guide.avif)
    !!! example ""
        * Borrow is limited to **3 borrows per day <u>per friend</u>**. That means if you have maximum friends (30), you can borrow up to 90 times per day.
        * **Borrow is available in:**
            * Normal Difficulty, Hard Difficulty, NPC Quests of Story Packs
            * Hard Difficulty of Character & Event Packs          
            * Normal & Challenge Battles in Season Events
            * Hunting Grounds & [Path of Adventure Content Pack](../content-packs/path-of-adventure.md) battles.
        * You **cannot** have **2 same characters** in a team.
        * You can borrow **only 1 character per fight**.

=== "![SwapOrder](../assets/images/battle-system/icons/icon_sequence1.avif){ .icon-list }"
    ### **Swap Order Feature** { #__tabbed_2_2 }
    This feature allows you to adjust the order in which your characters act.<br>It has 2 modes: ![Insert Icon](../assets/images/battle-system/icons/icon_insert.avif "Insert"){.icon} **Insert** and ![Replace Icon](../assets/images/battle-system/icons/icon_change.avif "Replace"){.icon} **Replace**.
    
    * ![Insert Icon](../assets/images/battle-system/icons/icon_insert.avif "Insert"){.icon} **Insert mode** allows you to alter your order by inserting desired character in a sequence. To do that, drag character on others.
        * If you drag **from bottom to top**, you will put chosen character **before** the character you drag onto.
        ??? note "Image Guide"
            ![Insert from below](../assets/images/battle-system/insert_below.avif)
        * If you drag **from top to bottom**, you will put chosen character **after** the character you drag onto.
        ??? note "Image Guide"
            ![Insert from above](../assets/images/battle-system/insert_above.avif)

    * ![Replace Icon](../assets/images/battle-system/icons/icon_change.avif "Replace"){.icon} **Replace mode** allows you to change order of 2 costumes.<br>To do that, simply drag a character onto another to switch the order.
    ??? note "Image Guide"
        ![Replace Feature](../assets/images/battle-system/Replace.avif)
    
    !!! tip "Replace Shortcut"
        ![Replace Shorcut Icon](../assets/images/battle-system/icons/icon_replace_shortcut.avif){ align=right }
        In order to save time, you can access to **Replace** feature from main battle menu via icon next to the right of the character cards.<br>It functions completely identical to the feature explained above.
        ??? note "Image Guide"
            ![Replace Shortcut Guide](../assets/images/battle-system/replace_shortcut.avif)

=== "![Preset](../assets/images/battle-system/icons/icon_preset.avif){ .icon-list }"
    ### **Preset Feature** { #__tabbed_2_3 }
    This feature allows you to quick load pre-saved teams.
    !!! example ""
        * **This includes characters, gear, order and positioning.**
        * If preset gear was used by different characters, activating a preset will unequip those gear pieces and equip on your team.
        * Preset name and icon can be customized for your needs.
        * You can delete or rewrite old presets in case you do not need them anymore.
        * There are total of 12 preset slots.
    In addition to presets, you can use **own recently used teams** in the second tab of preset menu.

    ---

    ![Preset Screen](../assets/images/battle-system/preset_screen.avif)
=== "![SP](../assets/images/battle-system/icons/icon_sp.avif){ .icon-list }"
    ### **SP Bar** { #__tabbed_2_4}
    SP bar displays your Skill Points which you use for using costumes' abilities.

    !!! example ""
        ![SP Label](../assets/images/battle-system/sp_info.avif)
        
        ---

        * ![Avaiable SP](../assets/images/battle-system/icons/icon_free_sp.avif "Available SP"){.icon} are available Skill Points.
        * ![Used SP](../assets/images/battle-system/icons/icon_used_sp.avif "Used SP"){.icon} are Skill Points which will be used in the following turn, if you press Battle.
        * ![Missing SP](../assets/images/battle-system/icons/icon_missing_sp.avif "Missing SP"){.icon} are Skill Points which are not available for use, or, in other words, you do not have them.
=== "![Rotate View](../assets/images/battle-system/icons/icon_rotateview.avif){ .icon-list }"
    ### **Rotate View Feature** { #__tabbed_2_5 }
    This feature allows you to change battlefield view to the top one and replacing surrounding backgrounds, allowing you to easily distinguish otherwise grouped enemies or allies.<br>In this mode, your units are always on the left side, while enemy is on the right.
            
    ---

    ![Rotate View Feature Showcase](../assets/images/battle-system/rotate_view.avif) 
        
    ---

    To go back to original view, simply press the same button once again.
=== "![Rotate](../assets/images/battle-system/icons/icon_rotate.avif){ .icon-list }"
    ### **Rotate Feature** { #__tabbed_2_6 }
    This feature allows you rotate the field, changing your and enemy visual positioning while keeping aethetics of surroundings. This can be useful for distinguishing grouped enemies, but [**Rotate View**]( #__tabbed_2_5 ) is better for this matter.<br>You cannot rotate the field with special bosses on it like Fiend Hunter or Guild Raid ones.
    ??? note "Feature Showcase"
        ![Rotate Feature Showcase](../assets/images/battle-system/rotation_comparison.avif)
</div>

---

## **More Advanced Battle Features**
### ![Death Time icon](../assets/images/battle-system/icons/bufficon_72.avif){.icon-header} **Death Time**
Death Time is a feature that should prevent the game from having extremely long battles. 

It appears **after 10th Turn** in **Story, Normal / Challenge Battles of Event, Mirror Wars and Evil Castle**. It also appears on **different turn** in **Golden Colosseum** (depending on rule), and does **NOT** appear in **Fiend Hunter and Guild Raid**.

Every 2 turns, every unit on the battlefield recieves **+100% ATK / MATK increase**, as well as **DEF / MRES descrease by 100%** and **Incoming Damage increase by 50%**. This means that characters like Gynt and Remnunt will no longer be effective to lock down enemy with their ATK reduction.

Death Time can be accumulated with no limits on its amount, meaning in case of "0 DMG Bug", you can reach as many Turns as you want, although it's quite pointless.
??? note "Death Time showcase"
    ![Death Time](../assets/images/battle-system/death_time.avif)

### ![Set Costume order icon](../assets/images/battle-system/icons/icon_setting_costume_active.avif){.icon-header} **Set Costume order**
Set Costume order is a feature that allows you to make pre-determined skill order activation. This is useful when you're setting up [Mirror Wars](../content-packs/mirror-wars.md) or repetive fights in gamemodes as Fiend Hunter. If you have feature active, you will see ![Set Costume order icon](../assets/images/battle-system/icons/icon_setting_costume_active.avif "Set Costume order"){.icon} icon in the character's card.

To use it, press on the chibi character **before turn 1** and press **Set Costume order** button in the bottom part of the screen.
??? note "Image Guide"
    ![Set Order Guide](../assets/images/battle-system/set_costume_order_guide.avif)

In opened menu, you will see 10 slots, corresponding to each of your Turns (up to 19th Turn) where you can put any of skills, basic attack or knockback.

* Selection will override your manual attempts to choose different skill during given turn. 
* Selection will oblige to game rules, meaning it won't activate the skill if you don't have enough SP or it's on cooldown.
* **Selection can loop**, meaning that for example putting **Robin Hood Zenith** and **Poolside Guardian Zenith** in first two slots will provide you repeated usage until the last turn.
??? note "Set Costume order UI Image"
    ![Set Costume order UI](../assets/images/battle-system/set_costume_order_guide2.avif)

### Status Effects
Characters and enemies can have different status effects, which enhance, dimish or modify character impact in a battle. <br>
Most common status effects (in a Story Packs) are **Taunt**, **Counter**, **Evade**, **Energy Guard** and **Immunity**.

* ![Taunt](../assets/images/battle-system/icons/bufficon_26.avif "Taunt"){.icon} **Taunt** makes your incoming attacks ignore target logic and attack that specific enemy. Is removable by dispel units (Scheherazade, Yuri, Eleanner), unless enemy has immunity.
* ![Counter](../assets/images/battle-system/icons/bufficon_39.avif "Counter"){.icon} **Counter** makes your units recieve damage when attacking the enemy. Often paired with **Taunt**. There are a lot of types of Counter, so read ability to understand what type of it you're facing. Also dispellable by dispel units, unless enemy has immunity. 
* ![Evade](../assets/images/battle-system/icons/bufficon_62.avif "Evade"){.icon} **Evade** completely disregards your attacks onto enemy. That means that any effects taking place with attacks *(such as Dispel, DoT etc)* **will not work** on enemy evading. To bypass the Evade, use **Self-Destruction** skills (Wiggle, Morpeah's summons).
* ![Energy Guard](../assets/images/battle-system/icons/bufficon_38.avif "Energy Guard"){.icon} **Energy Guard** acts as a shield, increasing current character's HP on top of cap. To bypass it, either use Dispel, deal True Damage or just deal enough DMG to remove it.
* ![Immunity](../assets/images/battle-system/icons/bufficon_61.avif "Immunity"){.icon} **Immunity** tells that character has immunity to some sort of actions, such as Weakness, Buff Removal, Knockback etc.

### Different Damage Types
There are few types of unique damage in the game.

* <u>**Fixed DMG**</u> **cannot crit**. It is not affected by **DEF**, **Magic Resist** and **DMG Taken Reduction / Increase**, but affected by **Property DMG**, **Chain Effect**, **DMG Dealt Increase / Reduction** and **Death Time Effect**.
* <u>**Consumed DMG**</u> also **cannot crit**. It is not affected by **DEF**, **Magic Resist**, **DMG Taken Reduction / Increase** and <u>**Energy Guard**</u>, but affected by **Property DMG**, **Chain Effect**, **DMG Dealt Increase / Reduction** and **Death Time Effect**.
* <u>**Pure DMG**</u> is not affected by **DEF**, **Magic Resist**, **DMG Taken Reduction / Increase** and **Energy Guard**, but affected by <u>**Critical Hit**</u>, **Property DMG**, **Chain Effect**, **DMG Dealt Increase / Reduction** and **Death Time Effect**.

<!--Brown Dust II is a turn-based strategy game, where you use your characters in order to defeat the enemy. 
Most common ways to start the battle are either activating it via quests or touching the enemy in the battle zones of packs.
Your team usually consists of 5 characters, which you can change pre-battle. Once you press “Battle”, you won’t be able to change your team. 
Battle goes by turns, as you could already guess, enabling your actions on odd turns and enemies’ on even ones. 
Each your turn, you can swap positions of your characters on the field by dragging them to needed spot and choose to either use a costume skill, knockback attack or just perform a basic hit. To do that, you need to press the character or their corresponding panel on the left and pick your desired action. Aside of that, you’re free to change the order in which they move. To do that, hold and drag green arrows on the right of character tiles. 
After confirming your choice, characters will automatically attack enemies based on your set actions. Usually characters attack opposing enemy (e.g. in the same column). However, if there is no enemy on the same column, expect to hit the column to the right instead. So, it’s possible to attack the furthermost right column from the furthermost left one. 
When you press the character, sometimes you can see quite a lot of lines connecting your characters and enemies. These are meant to help you understand who will be affected by the skill and who will target that character in the next turn. 
In addition to this, you can see a knockback direction or the damage that your character will inflict by their attack. If your damage is enough to kill the enemy, K.O. will be shown instead. Please keep in mind that this damage is shown without calculating the impact of other characters you use in the same turn so often those numbers will be much higher once you launch an attack. 
To keep the game somewhat fair, costumes activations rely on Skill Points (SP) — so you can’t blast expensive costumes together on the turn 1. Each basic attack or knockback gives you 1 SP, as well as some costumes can increase the amount of SP you have. A few costumes, however, drain additional SP from your team, so be aware of that! 
On turn 10, to prevent the game from having infinite battles, Death Time is introduced. It doesn’t mean that you’ve lost; instead, some adjustments are made. Each turn forward on, attack will be increased, def reduced, and incoming dmg increased. This can be helpful versus some tough opponents. You actually don’t have any limit afterwards, so if you can survive for long enough, you can deal insane damage with just basic attack.
When your character’s hp reach 0, they become fatigued and can’t continue to fight. In a battle, a tombstone is created in the character's place which can’t be moved by any knockback. To recover the character’s hp, use Inn in Safe Zones of pack or use Revive ability skill.-->