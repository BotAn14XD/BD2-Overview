---
comments: true
image: assets/images/site-assets/guild-raid-banner.png
hero: assets/images/site-assets/index-pc-nav-35.avif
icon: material/robot

---

![Guild Raid](../assets/images/site-assets/index-pc-nav-35.avif){: .card-header-img fetchpriority=high loading=eager }
# Guild Raid {: .sr-only }

**Guild Raid** is seasonal content that revolves around defeating a Boss that grows stronger with each level. Defeating the Boss grants {{Mercenary_Alliance_Deed}} **Mercenary Alliance Deed** and other minor rewards, most notably {{Dia}} **Dia**.

To access the game mode, press the **Enter Guild Raid** button in the **Guild** menu. 

??? image "Image Guide"
    ![Guild Raid Access](../assets/images/guild-raid/gr-access.avif)

---

!!! image "Guild Raid Menu"
    ![Guild Raid Menu](../assets/images/guild-raid/guild-raid.avif)

---

## Guild Raid Schedule

Guild Raid is a **seasonal** content that occurs **each 4 weeks** and lasts for **1 week**.

On the last day of Guild Raid, a Settlement Period starts at {{ time('15:00') }}, during which you cannot perform an attack on the Boss.

---

## Boss

Each Season you fight a different Boss. Each boss occupies specific tiles within a 5x5 battlefield grid, which is somewhat unique to this specific game mode.

??? image "Example of the tiles that are occupied by the Boss"
    ![Guild Raid Occupied Tiles](../assets/images/guild-raid/occupying-tiles-1.avif)

{{ redirect_btn('mechanics/battle/#grid-system', 'More about Grid System', '#e5b567') }}

Alternatively, inspect the Boss to get the same information.

??? image "Image Guide"
    ![Boss Inspect](../assets/images/guild-raid/occupying-tiles-2.avif)

### Boss Levels

Each Boss has **15 Levels**, with higher level being harder due to scaling {{ HP }} [**HP**{.white}](../misc/slang.md?term=Health) and {{ATK}} [**ATK**{.yellow}](../misc/slang.md?term=Attack) / {{MATK}} [**MATK**{.magenta}](../misc/slang.md?term=Magical Attack).

You can freely choose and attack any level since there is no penalty or limited number of attempts. Only the best attempt (highest successful level clear) is saved.

### Boss Skills

Each boss has three types of skills: **Basic**, **Conditional**, and **Overdrive** Skills. Each Skill is "tied" to a specific body part of the Guild Raid Boss. You can check these skills by inspecting the Boss in the Guild Raid Menu, just like the grid tiles.

??? image "Image Guide"
    ![Guild_Raid_Skills](../assets/images/guild-raid/boss-skills.avif)

* **Basic Skills** are the ones that the Boss will definitely use by default, unless they are overridden by Conditional or Overdrive Skills.
* **Conditional Skills** are actions the Boss will use only if a particular condition is met.
    * Conditional Skills can only be triggered a **fixed number of times per battle**.
    * This type of Skill will be used instead of the next scheduled Basic Skill or Overdrive Skill as soon as its condition is met, delaying the latter.
    * One of the Conditional Skills guarantees a team wipe after a certain Turn. It is possible to prolong this conditional skill under specific circumstances, but, generally speaking, it takes higher priority over other Skills. 
* **Overdrive Skills** are a specific type of Conditional Skills that unlock after reaching a specific HP threshold.

It is essential to understand the Skills to maximize your damage.

### Overdrive

Overdrive is a mechanic that unlocks a specific skill set after reaching a specific {{HP}} **HP** threshold. The threshold Health differs from Boss to Boss, although it usually activates at 50%. 

??? image "Overdrive Notification"
    ![Overdrive Notification](../assets/images/guild-raid/overdrive.avif)

Additionally, you can check the current Boss state below the HP bar.

??? image "Overdrive Indicator"
    ![Overdrive Indicator](../assets/images/guild-raid/overdrive-indicator.avif)

### Weak Points

**Weak Points** are specific body parts that may or may not be present.

Each Weak Point takes additional damage and is displayed as text reading **WEAK** along with a Damage Increase multiplier.

??? image "Weak Points Display"
    ![Weak Points Display](../assets/images/guild-raid/weak-points.avif)

### Break

Break is a mechanic that makes the Boss skip its turn. It is usually obtained by activating [Lancelot](#lancelot)'s Ability; however, some Conditional Skills apply it to the boss as well.

Boss Skills do not get skipped; instead, they are simply delayed until the Break is over.

---

## Battle

For the Battle, you need to set up the team with **7 Characters** (unlike the standard 5-character team format). Unlike the [Fiend Hunter](./fh.md), there are no multiple teams; only one goes throughout the whole battle.

!!! image "Guild Raid Battle" 
    ![Guild Raid Battle](../assets/images/guild-raid/lancelot-charged.avif)

As mentioned earlier, the Boss has a set Skill pattern, which is displayed on the right side of the screen. You can also see the next Skill having the **NEXT** label. Skills are used from top to bottom, except for Conditional Skills.

!!! abstract "Combat Behavior"
    * Boss Tiles cannot be knocked back or silenced.
    * Characters **cannot evade** Boss hits. The only way to not get hit is to position your Companions correctly.

### Overkill

If you successfully defeat **Level 15** of the Guild Raid, any extra damage you dealt on the last Turn is saved in the form of **Overkill**.

Overkill is used as a tiebreaker in case multiple Guilds score the same amount of Points.

The Overkill damage is displayed in the Victory Screen. **You cannot achieve Overkill if you fight any level lower than 15.**

!!! image "Overkill Damage Display"
    ![Overkill Damage Display](../assets/images/guild-raid/overkill.avif)

### Borrowing Characters

You can borrow up to 2 Characters from other players in the Guild to help you in combat.

To do that, press the second tab in the Team Formation Menu, and use the Replace Feature as usual.

??? image "Image Guide"
    ![Borrow Characters](../assets/images/guild-raid/borrow-character.avif)

Note that you have a maximum of **3 borrows per day**, and can place up to **2 borrowed characters in a single battle**. Borrow attempts are only consumed upon victory; if a run goes poorly, abandon the battle to preserve your daily attempts.

Using borrowed Characters slightly reduces your overall score, with each borrow (up to 2) reducing more points.

To put your own Support units, set them in the Guild menu.

??? image "Image Guide"
    ![Borrow Set Up](../assets/images/guild-raid/borrow-set-up.avif)

If your unit is borrowed, you will receive a small amount of {{Gold}} **Gold** after the season ends.

### Practice Battle

Before committing to an official attempt, you can test your formations, skill rotations, and Lancelot timings using **Practice Battle**.

It is accessible from the Guild Raid menu in the second tab.

??? image "Practice Battle Menu"
    ![Practice Battle Menu](../assets/images/guild-raid/practice-battle.avif)

Practice mode does not consume daily character borrow limits, allowing you to freely optimize the turn sequence.

Additionally, any [Burst](../progression/burst.md) will be unlocked automatically to the highest level, which helps to test if anyone is worth investing in for the Raid.

---

## Lancelot

Lancelot is an ally unique to the Guild Raid. It does not occupy a space or a slot in your active party.

It has a separate icon alongside the Characters' cards, which you can interact with.

??? image "Lancelot Button"
    ![Lancelot Button](../assets/images/guild-raid/lancelot_button.avif)

Lancelot is not available during the whole battle; to activate him, you need to deal enough damage to the Boss, after which he is available for 6 Turns.

You do not need to activate Lancelot as soon as he is charged up; however, once you do, you cannot pause the Lancelot countdown.

### Lancelot Skills

Lancelot has 4 Skills. Similar to any other Skill, you can activate only one of them per turn. Each Skill has 0 SP Cost, which means Lancelot does not impact your SP management negatively.

* **Redeeming Strike** puts the Boss into the **Break** state and apply **Vulnerability**. Since it can be used only once, it is usually used for the decisive finishing blow.
* **Arondight Rush** attacks the Boss 9 times in a wide area, which is used mainly to apply extra Chains for increased damage.
* **Radiant Combat Mastery** mainly applies Bleed, which is barely used as of now.
* **Blessing of the Lake** refreshes Characters' Cooldowns and restores 25 SP. It is often used in battles, but can be used only once.

To choose a Skill, press the Lancelot Card and pick the Skill you need.

??? image "Lancelot Skill Choice"
    ![Lancelot Skill Choice](../assets/images/guild-raid/lancelot-skills.avif)

{{ redirect_btn('https://browndust2.miraheze.org/wiki/Guild_Raid#Lancelot', 'Detailed Lancelot Data', '#e5b567') }}

## Scoring & Ranking

**Guild Score** is a sum of individual players within the Guild. Additionally, **Overkill** is counted as the sum of top-10 performers within the Guild (highest Overkill).

**Personal Score** consists of a **Clear Score**, **Turn Bonus** and **Support Character Bonus**.

* **Clear Score** is directly tied to the **Level** you participate in and increases by 500 for each level, up to 7500 for Level 15.
* **Turn Bonus** is a bonus for Turn Clear, with a bigger bonus the faster you defeat the boss.
    * The formula for the Turn Bonus is $80 - 3 \cdot (\text{Turn} - 1)$
* **Support Character Bonus** is a bonus based on the number of borrowed Support Characters used.
    * If no Support Characters were used, you receive **4 points**.
    * If 1 Support Character was used, you receive **3 points**.
    * If 2 Support Characters were used, you receive **0 points**.

**Ranking** is decided by Guild Score, and in case of a tie, by the Overkill.

Similar to [Golden Colosseum](../content-packs/gc.md), Guilds are placed in percentile-based brackets and receive corresponding rewards, with **Within the 0.1%** [of guilds] being the highest place the Guild can achieve.

---

## Rewards

Rewards are divided into **Personal**, **Guild Score**, and **Ranking**.

* Personal rewards are awarded based on a **Boss Level** you clear.
    * You receive 600 {{Mercenary_Alliance_Deed}} **Mercenary Alliance Deed** per Level, resulting in 9000 {{Mercenary_Alliance_Deed}} **Mercenary Alliance Deed** for a **Level 15** Clear.
* Guild Score rewards are awarded based on total Guild Score at the end of the Guild Raid.
    * You can receive up to 9000 {{Mercenary_Alliance_Deed}} **Mercenary Alliance Deed** if your Guild scores 100000 Points (which is a **level 7** clear on average for every person in the guild).
* Ranking Rewards are based on the percentile your Guild achieves at the end of the season.

{{ redirect_btn('https://browndust2.miraheze.org/wiki/Guild_Raid#Ranking_and_rewards', 'Detailed Rewards Data', '#e5b567') }}

To purchase all rewards from the Guild Shop, you need 11750 {{Mercenary_Alliance_Deed}} **Mercenary Alliance Deed**, which can be achieved by a level 6 clear and the Guild reaching 50000 Points within the 50-40% bracket, which is easily achievable.

---

## Guild Raid Guide

Since figuring out the best strategy for Guild Raid can be tricky for the average player, you have a few options:

* **Option 1: Follow YouTube Guides**{.yellow}

    * **Shimonami しもなみ** for commentless solutions.
    * **KingPepeII** for a detailed breakdown of the strategy.

    {{ redirect_btn('https://www.youtube.com/@Shimonami', "Shimonami's YouTube Channel", '#e5b567') }}
        {{ redirect_btn('https://www.youtube.com/@KingPepeIIVT', "KingPepeII's YouTube Channel", '#e5b567') }}

* **Option 2: Follow Souseha's Database Templates**{.yellow}

    It acts as a sort of forum where players can share their clears for the specific Boss.
    
    *(Note that it may be missing solutions.)*
    
    {{ redirect_btn('https://browndust2-db.souseha.com/en/formation/list', "Souseha's Database", '#e5b567') }}

* **Option 3: Follow the Arca Live Forum**{.yellow}

    This option is similar to the second; however, it is a **Korean forum**. Therefore, you should use a translator, but generally speaking, images do not need any translation.
    {{ redirect_btn('https://arca.live/b/browndust2/', "Arca Live Forum", '#e5b567') }}

---

## Related Links

* [Guild Raid | Miraheze Wiki](https://browndust2.miraheze.org/wiki/Guild_Raid)
* [<u>Shimonami しもなみ</u> | YouTube](https://www.youtube.com/@Shimonami)
* [<u>KingPepeII</u> | YouTube](https://www.youtube.com/@KingPepeIIVT)
* [Formation Templates | Brown Dust II Database by <u>Souseha</u>](https://browndust2-db.souseha.com/en/formation/list)
* [Arca Live Forum](https://arca.live/b/browndust2/)