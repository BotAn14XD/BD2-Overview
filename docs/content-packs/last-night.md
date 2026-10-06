---
description: Brown Dust II Last Night Overview, Strategy and Tips
comments: true
hero: assets/images/site-assets/index-pc-nav-32.avif
image: assets/images/site-assets/ln-banner.png
icon: fontawesome/solid/dragon
---

![Last Night](../assets/images/site-assets/index-pc-nav-32.avif){: .card-header-img fetchpriority=high loading=eager }
# Last Night {: .sr-only }

Last Night is a [PvE](../misc/slang.md?term=PvE) mode where you are tasked with dealing as much damage to the boss called Seeker of Extinction (Seeker of the End, Atraxus) as possible.

!!! image "Last Night Main Lobby"
    ![Last Night Lobby](../assets/images/last-night/main-lobby.avif)

## Basics

**Last Night** is unlocked upon clearing all **Mist Man** (Story Pack 3) Main Quests.

In this mode, your team consists of **20 (twenty)** costumes instead of usual five.

To access Last Night, select the corresponding **Combat Content Pack** from the list.

??? image "Image Guide"
    ![Access Guide](../assets/images/last-night/access-guide.avif)

Once you deal enough damage, you will start receiving **Daily Rewards**. To claim them, interact with **Isaac** daily in any Pack, except [Golden Colosseum](./gc.md), Glupy Diner, [The Soul Wager](./soul-wager.md), [Fantasia Territory](../life-sim/territory.md), and Fishing Voyage.

??? image "Image Guide"
    ![Isaac Reward](../assets/images/evil-castle/dispatch_guide.avif)

**You do not need to fight every day to get rewards.**

Daily Rewards include {{Gold}} **Gold**, {{Ancient_Crystal}} **Ancient Crystals** and {{Awakening_Elixir}} **Awakening Elixirs**.

## Team

As stated previously, your team consists of 20 **Costumes**, not Characters.

To modify your team, head to the Battle Menu and click the **Replace** button.

??? image "Image Guide"
    ![Access Guide 2](../assets/images/last-night/access-guide-2.avif)

!!! image "Battle & Team Menu"
    ![Battle Menu](../assets/images/last-night/battle-lobby.avif)

In Last Night, **Gear on Characters is saved separately from other content**, so make sure to equip characters and update Gear once you are trying to climb higher.

## Battle Specifics

The Last Night battle is different from other fights in the game. Here, all your 20 Costumes activate their ability based on the order they were set in, after which the battle is over and you gain your damage result.

* Costumes **do not use SP**. All skills are cost-free.

* Seeker of Extinction occupies **only one tile**, which automatically becomes the target for all your attacking units. That also means that any ability with "Main Target" will have this condition satisfied automatically.
* The Boss is **immune to Debuffs**. That also includes **Vulnerability** and **Damage over Time**.
* Seeker of the End has **Neutral** Property.
* Atraxus has both {{Physical}} **Physical**{.yellow} and {{Magical}} **Magical**{.magenta} properties ({{ATK}} **ATK**{.yellow} & {{MATK}} **MATK**{.magenta}).
* The boss also has 0% {{DEF}} **DEF**{.yellow} and 0% {{MRES}} **MRES**{.magenta}.

* In Last Night, **Chains** limit is removed.
* The Battle has a 50% [**Pressure**](../mechanics/damage-formula.md#pressure) effect, reducing any Stat buffs by 50%. This **does not** affect **Chains** and **Augmentation** (for example, fully upgraded [Homunculus Lathel](https://browndust2.miraheze.org/wiki/Homunculus_Lathel)'s Buff will be equal to only 140%, instead of 280%).
* Any Supports with limited AoE will provide the buff to all teammates. Same goes for Supports with **ALL** range by default.
* Self-Buffs are still applied to self only.
* Costumes with unlocked [Burst](../progression/burst.md) will automatically use it at their maximum unlocked level at zero SP cost.

## Support Bonus

**Support Bonus** is an additional damage multiplier unique to the Last Night. It is affected by **all unused Costumes** in the **whole roster**.

You can check your Support Bonus in the Battle Menu.

??? image "Support Bonus Display"
    ![Support Bonus Display](../assets/images/last-night/support-bonus-3.avif)

Support bonus is calculated separately for each Costume and then added together. Support Bonus for an individual Costume is calculated as **(Combat Power / 1000) %**, floored to the nearest 0.01%.

!!! example "Example"

    Angelica has **10983** Combat Power.
    !!! image ""
        ![Support-Bonus-1](../assets/images/last-night/support-bonus-1.avif)

    That means each of her Costumes will grant 10.98% Support Bonus.
    !!! image ""
        ![Support-Bonus-2](../assets/images/last-night/support-bonus-2.avif)

!!! tip "Support Bonus Strategy"
    1. Since Support Bonus affects each Costume based on a **Character's** Combat Power, you should prioritize equipping the Characters with the most Costumes, like [Justia](https://browndust2.miraheze.org/wiki/Justia) and [Lathel](https://browndust2.miraheze.org/wiki/Lathel). This way, the same increase from the Gear gets multiplied by a higher number.
    2. Costumes in the active team **do not provide Support Bonus**. That means you can **ignore Gearing** some characters like [Elpis](https://browndust2.miraheze.org/wiki/Elpis) or [Arines](https://browndust2.miraheze.org/wiki/Arines) who have only one Costume **if you use them in your team**.

## Rewards Milestones

As stated previously, Last Night provides {{Gold}} **Gold**, {{Ancient_Crystal}} **Ancient Crystals** and {{Awakening_Elixir}} **Awakening Elixirs**.

There are two core milestones in the damage: **52M** and **110M**. 

Reaching **52 million** damage awards the maximum **5** {{Ancient_Crystal}} **Ancient Crystals** daily, while **110 million** awards the maximum **5** {{Awakening_Elixir}} **Awakening Elixirs**, completing the daily material cap.

Any higher score provides only a small {{Gold}} **Gold** increase, as well as some titles & stickers on specific thresholds.

## Guide

A proper Last Night team can roughly be divided into three phases: **Supports (Buffers)**, **Chainers**, and **DPS (Damage Dealers)**

!!! image "Rough Last Night Team Composition"
    ![Rough Last Night Team Composition](../assets/images/last-night/ln-teamcomp-breakdown.avif)

* **Supports** buff other Characters / Costumes.
* **Chainers** apply the biggest amount of **Chains**. Because the boss is **neutral** (Property Damage does not apply) and **immune to debuffs** (therefore, Vulnerability), Chains and {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} / **Augmentation** / {{CritRate}} **Crit Rate** and {{CritDMG}} **Crit Damage** Buffs are the primary ways to scale damage.
* **DPS** deal the bulk of the team's total damage, capitalizing on the fully stacked chain multiplier.

!!! warning "Chainers — DPS edge"
    There is no major separation between Chainers and DPS in Last Night. This is mainly because Chainers still have *some* damage and they still contribute to the final score. Yet, you can roughly understand who should be the priority to set up the order.

    Because each hit increases the damage of all subsequent attacks, prioritize high-hit-count skills earlier in the chain, reserving your massive single-hit multipliers for the final slots where the chain bonus is peaked.
    
    This is not always the case, but it could guide you towards a better team composition.

!!! warning "Sunny Inn Hand Helena"
    In the given example, [Sunny Inn Hand Helena](https://browndust2.miraheze.org/wiki/Helena/Sunny_Inn_Hand) is put before Nebris, almost at the end of the team.

    This is **an exception** to Supports, since she buffs the next-attacking ally and is the only Support with such mechanics.

### Buffers

Almost all Buffers are good for the Last Night. However, due to the Pressure effect, the most impactful Buffers are the ones that give Augmentation or any Non-Stat increase.

This mostly includes [Pure White Blessing Refithea](https://browndust2.miraheze.org/wiki/Refithea/Pure_White_Blessing), [Onsen Manager Liberta](https://browndust2.miraheze.org/wiki/Liberta/Onsen_Manager), [Shrine Maiden of Purification Granadair](https://browndust2.miraheze.org/wiki/Granadair/Shrine_Maiden_of_Purification) and [Sunny Inn Hand Helena](https://browndust2.miraheze.org/wiki/Helena/Sunny_Inn_Hand).

It is worth noting that [Beachside Angel Teresse](https://browndust2.miraheze.org/wiki/Teresse/Beachside_Angel) is really ineffective here thanks to her low chain requirement that you cannot preserve.

??? image "List of Usable Supports"
    ![Supports List](../assets/images/last-night/supports-pick.avif)

### Chainers

In the beginning, you can use essentially any units with high chain/hit count, even including [Zenith](https://browndust2.miraheze.org/wiki/Zenith) that cannot apply either Vulnerability or Chain DMG Increase. Towards the end game, it shifts to Costumes with even higher Chain Count, such as [Water Park Wilhelmina](https://browndust2.miraheze.org/wiki/Wilhelmina/Water_Park_Queen) and [Deadeye Nekyndalia](https://browndust2.miraheze.org/wiki/Nekyndalia/Deadeye).

??? image "List of Usable Chainers"
    ![Chainers List](../assets/images/last-night/chainers-pick.avif)

### Damage Dealers

[New Hire Nebris](https://browndust2.miraheze.org/wiki/Nebris/New_Hire) is currently the best DPS for the Last Night thanks to her skill, which increases damage based on the number of buffs. In the best team, you gain ~25 Buffs that translate to **1260%** of ATK per hit for fully upgraded Nebris, or **3780%** total.

DPS Costumes that rely on {{HP}} **Enemy HP**, such as [Nature's Claw Rou](https://browndust2.miraheze.org/wiki/Rou/Nature%27s_Claw) or any [Angelica](https://browndust2.miraheze.org/wiki/Angelica)'s Costume, are quite powerful early on because of big scaling with no investment.

Additionally, [Promise of Vengeance Lathel](https://browndust2.miraheze.org/wiki/Promise_of_Vengeance_Lathel) is also good DPS that you can get for free by completing **Story Pack 7 (Fury Angel)** on each difficulty.

Worth noting that DPS that scale based on the number of enemies, such as [Reclaimed Destiny Sacred Justia](https://browndust2.miraheze.org/wiki/Reclaimed_Destiny_Sacred_Justia), perform worse, since essentially you hit only one tile.

??? image "List of Usable DPS"
    ![DPS List](../assets/images/last-night/dps-pick.avif)