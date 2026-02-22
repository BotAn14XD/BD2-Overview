---
description: Brown Dust II Battle System Overview
---
# Battle System
Brown Dust II is a turn-based strategy in which you have ability to position your characters, as well as choose character's skills in order to defeat the enemies.

![Battle](../assets/images/battle-system/battle_system_1.webp)

!!! example "Turns mechanic"
    * For all PvE content, you attack on **odd turns (1, 3, 5, ...)**, while enemy attacks on **even turns (2, 4, 6, ...)**.
    * During turns, you don't have to do anything; characters use skills automatically; **all preparation (positioning, skills choices) must be made pre-turn**.
    * You can make those preparations only **pre-turns**. Enemy turn is followed instantly after yours.
    * Turn progression only goes after you confirm your choices with "Turn X Battle" button in the bottom right corner of the battle screen.

## General Content


In general content (such a Story, Towers), you have ability to use **5 characters** on the field.

Field is a **3x4 rectangular grid**, in which you can place your characters however you like.

## Battle UI
![Bottom Part of UI](../assets/images/battle-system/UI_bottom.webp)
<div class="tab-align" markdown>
=== "![Replace](../assets/images/battle-system/icons/icon_pictorialbook1.webp){ .icon-list }"
    ### Replace Feature { #__tabbed_1_1 }
    Feauture allowing you to replace your characters during battle preparation.
    
    To replace a character, pick it from the list and tap on the character you want to replace.
    ??? note "Image Guide"
        ![Replace Guide](../assets/images/battle-system/replace_guide.webp)
    !!! example ""
        * You can **filter characters** to find the needed ones faster by using **Property Filter** on top or filter button on the top as well.
        * In case you need **specific knockback**, you can check it via icon ({{ Knockback }}) on each character.
        * You can also **add characters instead of replacing** in case you do not have max amount on the field. In this case, **click on empty grid cell** with chosen character to place them.
        * **You cannot replace characters on Turn 3 onwards, except [Tower of Salvation](../content-packs/evil-castle.md#tower-of-salvation).**
    ### Borrow Feature { #__tabbed_1_1 }
    In some fights, you can use your Friend Support units to help you beat the fight.<br>
    The idea is completely the same with the exception of pressing one more button (![Support Character Icon](../assets/images/battle-system/icons/icon_mercenary.webp "Support Character"){.icon}).
    ??? note "Image Guide" 
        ![Friend Support Replace Guide](../assets/images/battle-system/friend_support_guide.webp)
    !!! example ""
        * Borrow is limited to **3 borrows per day <u>per friend</u>**. That means if you have maximum friends (30), you can borrow up to 90 times per day.
        * **Borrow is available in:**
            * Normal Difficulty, Hard Difficulty, NPC Quests of Story Packs
            * Hard Difficulty of Character & Event Packs          
            * Normal & Challenge Battles in Season Events
            * Hunting Grounds & [Path of Adventure Content Pack](../content-packs/path-of-adventure.md) battles.
        * You **cannot** have **2 same characters** in a team.
        * You can borrow **only 1 character per fight**.

=== "![SwapOrder](../assets/images/battle-system/icons/icon_sequence1.png){ .icon-list }"
    ### Swap Order Feature { #__tabbed_1_2 }
    This feature allows you to adjust the order in which your characters act.<br>It has 2 modes: ![Insert Icon](../assets/images/battle-system/icons/icon_insert.webp "Insert"){.icon} **Insert** and ![Replace Icon](../assets/images/battle-system/icons/icon_change.webp "Replace"){.icon} **Replace**.
    
    * ![Insert Icon](../assets/images/battle-system/icons/icon_insert.webp "Insert"){.icon} **Insert mode** allows you to alter your order by inserting desired character in a sequence. To do that, drag character on others.
        * If you drag **from bottom to top**, you will put chosen character **before** the character you drag onto.
        ??? note "Image Guide"
            ![Insert from below](../assets/images/battle-system/insert_below.webp)
        * If you drag **from top to bottom**, you will put chosen character **after** the character you drag onto.
        ??? note "Image Guide"
            ![Insert from above](../assets/images/battle-system/insert_above.webp)

    * ![Replace Icon](../assets/images/battle-system/icons/icon_change.webp "Replace"){.icon} **Replace** mode allows you to change order of 2 costumes.<br>To do that, simply drag a character onto another to switch the order.
    ??? note "Image Guide"
        ![Replace Feature](../assets/images/battle-system/Replace.webp)
    
    !!! tip "Replace Shortcut"
        ![Replace Shorcut Icon](../assets/images/battle-system/icons/icon_replace_shortcut.webp){ align=right }
        In order to save time, you can access to **Replace** feature from main battle menu via icon next to the right of the character cards.<br>It functions completely identical to the feature explained above.
        ??? note "Image Guide"
            ![Replace Shortcut Guide](../assets/images/battle-system/replace_shortcut.webp)

=== "![Preset](../assets/images/battle-system/icons/icon_preset.png){ .icon-list }"
    ### Preset Feature { #__tabbed_1_3 }
    This feature allows you to quick load pre-saved teams.
    !!! example ""
        * **This includes characters, gear, order and positioning.**
        * If preset gear was used by different characters, activating a preset will unequip those gear pieces and equip on your team.
        * Preset name and icon can be customized for your needs.
        * You can delete or rewrite old presets in case you do not need them anymore.
        * There are total of 12 preset slots.
    In addition to presets, you can use **own recently used teams** in the second tab of preset menu.
    ![Preset Screen](../assets/images/battle-system/preset_screen.webp)
=== "![SP](../assets/images/battle-system/icons/icon_sp.webp){ .icon-list }"
    SP bar displays your Skill Points which you use for using costumes' abilities.

    !!! example ""
        ![SP Label](../assets/images/battle-system/sp_info.webp)
        
        * ![Avaiable SP](../assets/images/battle-system/icons/icon_free_sp.webp "Available SP"){.icon} are available Skill Points.
        * ![Used SP](../assets/images/battle-system/icons/icon_used_sp.webp "Used SP"){.icon} are Skill Points which will be used in the following turn, if you press Battle.
        * ![Missing SP](../assets/images/battle-system/icons/icon_missing_sp.webp "Missing SP"){.icon} are Skill Points which are not available for use, or, in other words, you do not have them.
=== "![Rotate View](../assets/images/battle-system/icons/icon_rotateview.webp){ .icon-list }"

=== "![Rotate](../assets/images/battle-system/icons/icon_rotate.webp){ .icon-list }"
</div>
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