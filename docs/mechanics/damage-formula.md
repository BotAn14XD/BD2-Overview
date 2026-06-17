---
comments: true
---
# Damage Formula — Brown Dust II

!!! abstract "TL;DR"
    The Damage Formula consists of a few multipliers, the main of which are {{ATK}} $\text{\textcolor{ffe8aa}{ATK}}$ / {{MATK}} $\text{\textcolor{ffa6ff}{MATK}}$ and its Buffs, {{CritDMG}} $\text{\textcolor{white}{CDMG}}$ and its buffs, $\text{\textcolor{8A9A5B}{Property Damage}}$, $\text{Vulnerability}$ with $\text{DMG Increase}$ Buffs, and, lastly, $\text{Chains}$.

    Within each of these multipliers, buffs are additive, meaning, if you want to reach more damage, you must **use different buff categories**. 

    Stacking a lot of {{ATK}} **ATK**{.yellow} buffs generally loses to a single {{ATK}} **ATK**{.yellow} buff combined with $\text{Vulnerability}$ and some $\text{Chains}$. Keep this in mind when constructing a team.

## Damage Formula
$\small\text{Damage} = \\\\ \text{\textcolor{ffe8aa}{ATK} [\textcolor{ffa6ff}{MATK} / \textcolor{orange}{HP}}^{\textcolor{AFDBF5}{[1]}} \text{/ \textcolor{white}{Energy Guard}}^{\textcolor{AFDBF5}{[2]}}\text{]}^{\textcolor{AFDBF5}{[3]}}  \\\\
\times \; \text{Skill\%} \\\\
\times \; (100\% + \text{\textcolor{ffe8aa}{ATK\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{\textcolor{ffe8aa}{ATK\%} Debuffs})^{\textcolor{AFDBF5}{[4]}} \\\\
\times \; (100\% + \text{\textcolor{white}{CDMG\%}} + \text{\textcolor{white}{CDMG\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{\textcolor{white}{CDMG\%} Debuffs})^{\textcolor{AFDBF5}{[5]}} \\
\times \; (100\% + (10\% + \text{Increase Chain DMG\%}) \times \text{Chains})^{\textcolor{AFDBD5}{[6]}} \\\\
\times \; (100\% + \text{Target's Vulnerability Debuffs\%} + \text{DMG Increase\% Buffs}) \\\\
\times \; (100\% + \text{\textcolor{8A9A5B}{Property Damage\%}} + \text{Season Buff\%}^{\textcolor{AFDBD5}{[7]}} + \text{\textcolor{8A9A5B}{Property Damage\%} Buffs} \times [100\% - \text{Pressure\%}]  )^\text{\textcolor{AFDBF5}{[8]}} \\\\
\times \; (100\% - (\text{Target's \textcolor{ffe8aa}{DEF\%}} + \text{Target's \textcolor{ffe8aa}{DEF\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{Target's \textcolor{ffe8aa}{DEF\%} Debuffs}))^\text{\textcolor{AFDBF5}{[9]}} \\\\  
\times \; (100\% - \text{Target's DMG Reduction\% Buffs}) \\\\
\times \; (100\% - \text{Target's \textcolor{8A9A5B}{Property Resist\%}})^\text{\textcolor{AFDBF5}{[10]}} \\\\
\times \; (100\% + \text{Weak Point\%})^\text{\textcolor{AFDBF5}{[11]}} \\\\
\times \; (100\% + \text{Support Bonus\%})^\text{\textcolor{AFDBF5}{[12]}}$

!!! example "Formula Notes"
    ${\textcolor{AFDBF5}{[1]}}$: Whenever {{HP}} **HP**{.orange} is used (either your own or the enemy's), there is a cap of $\text{50,000}$ for the value. In other words, if you use Angelica's skill on the enemy with $\text{2,000,000}$ {{HP}} **HP**{.orange}, only $\text{50,000}$ will be put as the value.

    ${\textcolor{AFDBF5}{[2]}}$: **Energy Guard** damage (from Boo Ghost Granhildr) counts as {{HP}} **HP**{.orange} damage, but **has no cap value**.

    ${\textcolor{AFDBF5}{[3]}}$: The necessary attribute depends on the Costume ability. Refer to [this](#__tabbed_1_1) section to learn more.

    ${\textcolor{AFDBF5}{[4]}}$: {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Buffs are **irrelevant** when a character deals damage based on their **own / the enemy's** {{HP}} **HP**{.orange}.

    Buffs are **relevant** if a character uses **enemy** {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} to deal damage.

    ${\textcolor{AFDBF5}{[5]}}$: Applied only when a character **crits**. Characters with [**Fixed Damage**](../mechanics/battle.md#different-damage-types) cannot crit, making this multiplier equal to $1$.

    ${\textcolor{AFDBF5}{[6]}}$: Unless the fight disables the chain mechanic (some Story Pack bosses).

    ${\textcolor{AFDBF5}{[7]}}$: Currently applicable only to [Evil Castle](../content-packs/evil-castle.md) battles.

    ${\textcolor{AFDBF5}{[8]}}$: Mutually exclusive to $\text{Property Resist\%}$ multiplier.

    ${\textcolor{AFDBF5}{[9]}}$: Ignored when unit deals **Pure**, **Consumed** or **Fixed** Damage.

    ${\textcolor{AFDBF5}{[10]}}$: Mutually exclusive to $\text{Property Damage\%}$ multiplier.

    ${\textcolor{AFDBF5}{[11]}}$: Exclusive to Fiend Hunter and Guild Raid.

    ${\textcolor{AFDBF5}{[12]}}$: Exclusive to Last Night.

??? example "Pure Math Formula (FOR MATH NERDS ONLY)"
    $\text{Damage} = 
    \max \left(\left\lfloor\text{Damage}_{\; \text{Total}}\right\rfloor, 1\right)$

    ---

    $\text{Damage}_{\; \text{Total}} = \\\\
    \left[\min \left(\vec{c}_\text{max}^\text{v}, \vec{\text{v}} \odot \left[1 + \displaystyle \sum_{i=1}^{n^{(1)}} \vec{\text{b}}_\text{i}^{\text{(off)}} \times \left[1 - \min\left(\text{P},1\right) \right] - \displaystyle \sum_{i=1}^{n^{(2)}}\vec{\text{d}}_\text{i}^{\text{(off)}}\right] \right) \odot \vec{\text{SM}} \right] \vec{\text{s}}^{\top} \times \\\\
    \times \left[ \min \left(1, \max \left(0.1, \left[ 1 - \left(1-\delta_{\text{pfc}}\right) \times \left(\vec{\tilde{\text{v}}} + \displaystyle \sum_{i=1}^{n^{(3)}} \vec{\text{b}}_\text{i}^{\text{(def)}} \times \left[1 - \min\left(\text{P},1\right) \right] - \displaystyle \sum_{i=1}^{n^{(4)}}\vec{\text{d}}_\text{i}^{\text{(def)}}\right) \right]\right) \right) \right] \vec{\tilde{\text{s}}}^{\top} \times \\\\
    \times \Bigg[ \max \Biggl(1,\Bigg[ 1 + \left(\left(1-\delta_{\text{fc}} \right) \times \mathcal{H}\left(\text{v}^{\text{cr}} + \displaystyle \sum_{i=1}^{n^{(5)}} \text{b}_\text{i}^{\text{(cr)}} \times \left[1 - \min\left(\text{P},1\right) \right] - \displaystyle \sum_{i=1}^{n^{(6)}}\text{d}_\text{i}^{\text{(cr)}}- \mathcal{U}\left(0,1\right) \right) \right) \times \\\\ 
    \times \min\left(10^4, 10^{-3} \times \left\lfloor 10^3 \times \left(1+ \text{v}^{\text{(cdmg)}} + \displaystyle \sum_{i=1}^{n^{(7)}} \text{b}_\text{i}^{\text{(cdmg)}} \times \left[1 - \min\left(\text{P},1\right) \right] - \displaystyle \sum_{i=1}^{n^{(8)}}\text{d}_\text{i}^{\text{(cdmg)}}\right)\right\rfloor\right) \Bigg]\Bigg)\Bigg] \times \\\\
    \times \Bigg[1+\max \left(0, \vec{\text{pr}}^\text{(off)} \times \text{PR} \times \left(\vec{\text{pr}}^\text{(def)}\right)^{\top}\right) \times \left( \vec{\text{v}}_{\text{pr}}^{\text{(off)}} + \displaystyle \sum_{i=1}^{n^{(9)}} \vec{\text{b}}_\text{i}^{\text{(pr\_off)}} \times \left[1 - \min\left(\text{P},1\right) \right] - \displaystyle \sum_{i=1}^{n^{(10)}} \vec{\text{d}}_\text{i}^{\text{(pr)}}\right)+\\\\
    +\min \left(0, \vec{\text{pr}}^\text{(off)} \times \text{PR} \times \left(\vec{\text{pr}}^\text{(def)}\right)^{\top}\right) \times \left( \vec{\text{v}}_{\text{pr}}^{\text{(def)}} + \displaystyle \sum_{i=1}^{n^{(11)}} \vec{\text{b}}_\text{i}^{\text{(pr\_def)}} \times \left[1 - \min\left(\text{P},1\right) \right] - \displaystyle \sum_{i=1}^{n^{(12)}} \vec{\text{d}}_\text{i}^{\text{(pr)}}\right) + \\\\
    + \delta_{\text{EC}} \times \text{b}^{\text{EC}} \Bigg] \times \\\\
    \times \left[1 + \delta_{\text{chains}} \times \left(0.1 + \displaystyle \sum_{i=1}^{n^{(13)}} \text{b}_\text{i}^{\text{(chains)}} \right) \times \left[\left(1-\delta_\text{ln}\right) \times \min \left(100, \text{v}^{\text{(chains)}}\right) + \delta_\text{ln} \text{v}^{\text{(chains)}} \right] \right] \times \\\\
    \times \Bigg[1 + \displaystyle \sum_{i=1}^{n^{(14)}} \text{b}_\text{i}^{\text{(aug)}} + \displaystyle \sum_{i=1}^{n^{(15)}} \text{b}_\text{i}^{\text{(vuln\_gen)}} + \displaystyle \sum_{i=1}^{n^{(16)}} \vec{\text{b}}_\text{i}^{\text{(vuln\_dt)}} \times \vec{\tilde{\text{s}}}^{\top} + \displaystyle \sum_{i=1}^{n^{(17)}} \vec{\text{b}}_\text{i}^{\text{(vuln\_pr)}} \times  \left(\vec{\text{pr}}^\text{(off)}\right)^{\top} + \\\\
    + \delta_{\text{DoT}} \times \displaystyle \sum_{i=1}^{n^{(18)}} \vec{\text{b}}_\text{i}^{\text{(vuln\_dot)}} + \delta_{\text{summons}} \times \displaystyle \sum_{i=1}^{n^{(19)}} \vec{\text{b}}_\text{i}^{\text{(vuln\_summons)}}  \Bigg] \times \\\\
    \times \left(1-\delta_{\text{pf}}\right) \times \displaystyle \prod_{i=1}^{n^{(20)}}  \left[1 - \vec{\text{b}}_\text{i}^{\text{(dmg\_red)}} \right] \vec{\tilde{\text{s}}}^{\top}  \times \\\\
    \times \left[1 + \delta_{\text{fh/gr}} \times \text{b}_{\text{weak}} \right] \times \\\\
    \times \left[1 + \delta_\text{ln} \times \text{b}_{\text{supp}} \right] \times \\\\
    \times \left[1-\delta_{\text{kb}}\right]$    
    

    ---

    $\vec{\text{c}}^\text{v}_\text{max} = \begin{pmatrix} 10^5 & 10^5 & 5 \cdot 10^4 & \infty & 10^5 & 10^5 & 5 \cdot 10^4 \end{pmatrix}$

    $\vec{\text{v}} = \begin{pmatrix}\text{\textcolor{ffe8aa}{ATK}}_\text{self} & \text{\textcolor{ffa6ff}{MATK}}_\text{self} & \text{\textcolor{orange}{HP}}_\text{self} & \text{\textcolor{white}{EG}}_\text{self} & \text{\textcolor{ffe8aa}{ATK}}_\text{enemy} & \text{\textcolor{ffa6ff}{MATK}}_\text{enemy} & \text{\textcolor{orange}{HP}}_\text{enemy} \end{pmatrix}$

    $\text{SM} = \begin{pmatrix}\text{SM}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{self}} & \text{SM}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{self}} & \text{SM}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{self}} & \text{SM}_{\text{i}}^{\text{\textcolor{white}{EG}}_\text{self}}& \text{SM}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{enemy}}& \text{SM}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{enemy}} & \text{SM}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{enemy}} \end{pmatrix}$

    $\vec{\text{s}} = \begin{pmatrix}\delta\text{\textcolor{ffe8aa}{ATK}}_\text{self} & \delta\text{\textcolor{ffa6ff}{MATK}}_\text{self} & \delta\text{\textcolor{orange}{HP}}_\text{self} & \delta\text{\textcolor{white}{EG}}_\text{self} & \delta\text{\textcolor{ffe8aa}{ATK}}_\text{enemy} & \delta\text{\textcolor{ffa6ff}{MATK}}_\text{enemy} & \delta\text{\textcolor{orange}{HP}}_\text{enemy} \end{pmatrix}$

    $\vec{\text{b}}_\text{i}^{\text{(off)}} = \begin{pmatrix}\text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{self}} & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{self}} & \text{b}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{self}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{white}{EG}}_\text{self}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{enemy}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{enemy}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{enemy}} \equiv 0 \end{pmatrix}$

    $\vec{\text{d}}_\text{i}^{\text{(off)}} = \begin{pmatrix}\text{d}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{self}} & \text{d}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{self}} & \text{d}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{self}} \equiv 0 & \text{d}_{\text{i}}^{\text{\textcolor{white}{EG}}_\text{self}} \equiv 0 & \text{d}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{enemy}} \equiv 0 & \text{d}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{enemy}} \equiv 0 & \text{d}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{enemy}} \equiv 0 \end{pmatrix}$

    $\vec{\tilde{\text{v}}} = \begin{pmatrix}\text{\textcolor{ffe8aa}{DEF}} & \text{\textcolor{ffa6ff}{MRES}} \end{pmatrix}$

    $\vec{\tilde{\text{s}}} = \begin{pmatrix}\delta\text{\textcolor{ffe8aa}{Physical}} & \delta\text{\textcolor{ffa6ff}{Magical}} \end{pmatrix}$

    $\vec{\text{b}}_\text{i}^{\text{(def)}} = \begin{pmatrix}\text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{DEF}}} & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{MRES}}}\end{pmatrix}$

    $\vec{\text{d}}_\text{i}^{\text{(def)}} = \begin{pmatrix}\text{d}_{\text{i}}^{\text{\textcolor{ffe8aa}{DEF}}} & \text{d}_{\text{i}}^{\text{\textcolor{ffa6ff}{MRES}}}\end{pmatrix}$

    $\delta_{\text{pfc}} = \begin{pmatrix}\delta\text{Pure} & \delta\text{Fixed} & \delta\text{Consumed}\end{pmatrix} \cdot \begin{pmatrix}1 & 1 & 1\end{pmatrix}^{\top}$
    
    $\delta_{\text{fc}} = \begin{pmatrix}\delta\text{Fixed} & \delta\text{Consumed}\end{pmatrix} \cdot \begin{pmatrix}1 & 1\end{pmatrix}^{\top}$ 

    $\text{PR} = \begin{pmatrix}0 & 1 & -1 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0\end{pmatrix}$
    
    $\vec{\text{pr}}^\text{(off)} = \begin{pmatrix}\delta\text{Water} & \delta\text{Fire} & \delta\text{Wind} & \delta\text{Light} & \delta\text{Darkness} & \delta\text{Neutral}\end{pmatrix} \\\\
    \vec{\text{pr}}^\text{(def)} = \begin{pmatrix}\delta\text{Water} & \delta\text{Fire} & \delta\text{Wind} & \delta\text{Light} & \delta\text{Darkness} & \delta\text{Neutral}\end{pmatrix}$

    $\vec{\text{b}}_\text{i}^{\text{(pr)}} = \begin{pmatrix}\text{b}_{\text{i}}^{\text{Water}} & \text{b}_{\text{i}}^{\text{Fire}} & \text{b}_{\text{i}}^{\text{Wind}} & \text{b}_{\text{i}}^{\text{Light}} & \text{b}_{\text{i}}^{\text{Darkness}} & \text{b}_{\text{i}}^{\text{Neutral}} \equiv 0 \end{pmatrix}$

    $\vec{\text{d}}_\text{i}^{\text{(pr)}} = \begin{pmatrix}\text{d}_{\text{i}}^{\text{Water}} & \text{d}_{\text{i}}^{\text{Fire}} & \text{d}_{\text{i}}^{\text{Wind}} & \text{d}_{\text{i}}^{\text{Light}} & \text{d}_{\text{i}}^{\text{Darkness}} & \text{d}_{\text{i}}^{\text{Neutral}} \equiv 0 \end{pmatrix}$

    $\vec{\text{v}}_\text{(pr)}^{\text{j}} = \begin{pmatrix}\text{v}_{\text{pr}}^{\text{j\_Water}} & \text{v}_{\text{pr}}^{\text{j\_Fire}} & \text{v}_{\text{pr}}^{\text{j\_Wind}} & \text{v}_{\text{pr}}^{\text{j\_Light}} & \text{v}_{\text{pr}}^{\text{j\_Darkness}} & \text{v}_{\text{pr}}^{\text{j\_Neutral}} \equiv 0 \end{pmatrix}$

    $\vec{\text{b}}_\text{i}^{\text{(vuln\_dt)}} = \begin{pmatrix}\text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{Vuln\_Physical}}} & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{Vuln\_Magical}}} \end{pmatrix}$

    $\vec{\text{b}}_\text{i}^{\text{(vuln\_pr)}} = \begin{pmatrix}\text{b}_{\text{i}}^{\text{Vuln\_Water}} & \text{b}_{\text{i}}^{\text{Vuln\_Fire}} & \text{b}_{\text{i}}^{\text{Vuln\_Wind}} & \text{b}_{\text{i}}^{\text{Vuln\_Light}} & \text{b}_{\text{i}}^{\text{Vuln\_Darkness}} & \text{b}_{\text{i}}^{\text{Vuln\_Neutral}} \end{pmatrix}$

    $\vec{\text{b}}_\text{i}^{\text{(dmg\_red)}} = \begin{pmatrix}\text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{dmg\_red\_Physical}}} & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{dmg\_red\_Magical}}} \end{pmatrix}$

    $\delta_{\text{fh/gr}} = \begin{pmatrix}\delta\text{Fiend Hunter} & \delta\text{Guild Raid}\end{pmatrix} \cdot \begin{pmatrix}1 & 1\end{pmatrix}^{\top}$ 

<div class="tab-align" markdown>
=== "$\text{\textcolor{ffe8aa}{ATK}}$"

    This corresponds to the character's {{ATK}} **ATK**{.yellow}, {{MATK}} **MATK**{.magenta}, own or enemy {{HP}} **HP**{.orange}, or, rarely, enemy {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta}. To understand what's being used in each case, find words like "**of your** **ATK**{.yellow}" in the costume skill description.  
    ??? image "Image Showcase"
        ![Base stat dependency Showcase](../assets/images/damage-formula/based_of_desc.avif)

    Formula for calculating {{ATK}} **ATK**{.yellow}, {{MATK}} **MATK**{.magenta} or {{HP}} **HP**{.orange} of a character:

    $\text{Parameter} = [\text{\textcolor{ffe8aa}{ATK} / \textcolor{ffa6ff}{MATK} / \textcolor{f89c22}{HP}}] = \\\\
    (\text{Character's Base Parameter} \\\\
    + \; \text{Parameter from Gear} \\\\
    + \; \text{Parameter from Potential}) \\\\
    \times \; ( 100\% + \text{Parameter\% from Gear} \\\\
    + \; \text{Parameter\% from Potential} \\\\
    + \; \text{Parameter\% from Collection})$

    ---

=== "$\text{Skill\%}$"

    The Skill% mostly represents the percent (%) mentioned in the Skill Description. 

    ??? image "Image Showcase"
        ![Skill% Showcase](../assets/images/damage-formula/skill_desc.avif)
    
    There are some conditional $\text{Skill\%}$ values, meaning they are achievable only when some conditions are met.

    <table class="data-table">
        <thead>
            <tr>
                <th></th>
                <th>Costume</th>
                <th>Skill%</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center">
                ![Respected Master Roxy](../assets/images/damage-formula/illust_inven_char020101_125.avif){.icon-portrait}
                </td>
                <td><strong>Respected Master<br>Roxy</strong></td>
                <td>$\textcolor{white}{300\% \sim 600\% \text{ to the Main Target}} \newline 140\% \sim 300\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Prophetic Dream Darian](../assets/images/damage-formula/illust_inven_char004001_181.avif){.icon-portrait}
                </td>
                <td><strong>Prophetic Dream<br>Darian</strong></td>
                <td>$\textcolor{white}{775\% \sim 1300\% \text{ to the Main Target}} \newline 500\% \sim 900\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Bittersweet Bunny Darian](../assets/images/damage-formula/illust_inven_char004002_185.avif){.icon-portrait}
                </td>
                <td><strong>Bittersweet Bunny<br>Darian</strong></td>
                <td>$\textcolor{white}{400\% \sim 600\% \text{ if enemy is under DoT effects}} \newline 200\% \sim 400\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Maid Name R Liatris](../assets/images/damage-formula/illust_inven_char001207_114.avif){.icon-portrait}
                </td>
                <td><strong>Maid Name R<br>Liatris</strong></td>
                <td>$\textcolor{white}{500\% \sim 850\% \text{ if enemy is under DoT effects}} \newline 400\% \sim 550\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Celebrity Bunny Loen](../assets/images/damage-formula/illust_inven_char003203_153.avif){.icon-portrait}
                </td>
                <td><strong>Celebrity Bunny<br>Loen</strong></td>
                <td>$50\% + [75\% \sim 175\%] \times \text{Targets affected}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Esteemed Adventurer Eris](../assets/images/damage-formula/illust_inven_char020001_124.avif){.icon-portrait}
                </td>
                <td><strong>Esteemed Adventurer<br>Eris</strong></td>
                <td>$\textcolor{white}{600\% \sim 1100\% \newline \text{if Chain count after the attack is} \le 7} \newline 300\% \sim 650\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Night of Jealousy Levia](../assets/images/damage-formula/illust_inven_char067302_139.avif){.icon-portrait}
                </td>
                <td><strong>Night of Jealousy<br>Levia</strong></td>
                <td>$\textcolor{white}{80\% \sim 300\% \text{ to the Main Target}} \newline 30\% \sim 90\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Overheat Levia](../assets/images/damage-formula/illust_inven_char067303_154.avif){.icon-portrait}
                </td>
                <td><strong>Overheat<br>Levia</strong></td>
                <td>$\textcolor{white}{550\% \sim 1000\% \newline \text{if enemy is in Vulnerability state}} \newline 200\% \sim 350\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![New Hire Nebris](../assets/images/damage-formula/illust_inven_char003303_149.avif){.icon-portrait}
                </td>
                <td><strong>New Hire<br>Nebris</strong></td>
                <td>$[40\% \sim 80\%] + [15\% \sim 30\%] \times \text{Buffs Applied}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Innocent Bunny Tyr](../assets/images/damage-formula/illust_inven_char004102_186.avif){.icon-portrait}
                </td>
                <td><strong>Innocent Bunny<br>Tyr</strong></td>
                <td>$[125\% \sim 300\%] + [100\% \sim 180\%] \times \text{SP Consumed}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Snow White Ventana](../assets/images/damage-formula/illust_inven_char067002_99.avif){.icon-portrait}
                </td>
                <td><strong>Snow White<br>Ventana</strong></td>
                <td>$\textcolor{white}{600\% \sim 1300\% \newline \text{if enemy is in Taunt or Concentrated Fire state}} \newline 200\% \sim 450\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Reclaimed Destiny Sacred Justia](../assets/images/damage-formula/illust_inven_char003501_131.avif){.icon-portrait}
                </td>
                <td><strong>Reclaimed Destiny<br>Sacred Justia</strong></td>
                <td>$[150\% \sim 300\%] + [50\% \sim 100\%] \times \text{Targets affected}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Fallen Wings Olivier](../assets/images/damage-formula/illust_inven_char003603_175.avif){.icon-portrait}
                </td>
                <td><strong>Fallen Wings<br>Olivier</strong></td>
                <td>$[150\% \sim 250\%] + [60\% \sim 100\%] \times \text{Additional SP Consumed}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Faithful Wings Olivier](../assets/images/damage-formula/illust_inven_char003601_138.avif){.icon-portrait}
                </td>
                <td><strong>Faithful Wings<br>Olivier</strong></td>
                <td>$[150\% \sim 250\%] + [30\% \sim 50\%] \times \text{Targets affected}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Anonymous Sage Nartas](../assets/images/damage-formula/illust_inven_char065802_103.avif){.icon-portrait}
                </td>
                <td><strong>Anonymous Sage<br>Nartas</strong></td>
                <td>$\textcolor{white}{400\% \sim 1050\% \newline \text{if enemy is a Physical Type}} \newline 300\% \sim 450\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Deal Snatcher Luvencia](../assets/images/damage-formula/illust_inven_char067502_148.avif){.icon-portrait}
                </td>
                <td><strong>Deal Snatcher<br>Luvencia</strong></td>
                <td>$\textcolor{white}{[80\% \sim 160\%] \times (100\% - 5\% \times \text{Targets Affected}) \newline \text{ to the Main Target}} \newline [60\% \sim 80\%] \times (100\% - 5\% \times \text{Targets Affected}) \newline \text{otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Wild Dog Luvencia](../assets/images/damage-formula/illust_inven_char067503_155.avif){.icon-portrait}
                </td>
                <td><strong>Wild Dog<br>Luvencia</strong></td>
                <td>$\textcolor{white}{40\% \sim 160\% \newline \text{if enemy Chain count is a multiple of 3}} \newline 30\% \sim 80\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Onsen Swordfighter Blade](../assets/images/damage-formula/illust_inven_char003702_158.avif){.icon-portrait}
                </td>
                <td><strong>Onsen Swordfighter<br>Blade</strong></td>
                <td>$[350\% \sim 600\%] + [70\% \sim 120\%] \times \text{Debuffs Applied on enemy}$</td>
            </tr>
        </tbody>
    </table>

=== "$\text{\textcolor{ffe8aa}{ATK\%} Buffs}$"

    The {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} buff is the most common type of buff. It directly increases the character's stat.

    These buffs are **additive** if coming from different sources (parts of the skills or different skills): 

    $\text{\textcolor{ffe8aa}{ATK\%} Total Buff = \textcolor{ffe8aa}{ATK\%} Buff 1 + \textcolor{ffe8aa}{ATK\%} Buff 2} + \dots $

    If you apply the same buff from the same source before the previous one has expired, it will **refresh** the buff duration and will **not** make two instances of the buff. 

    ---

    Costumes providing {{ATK}} $\text{\textcolor{ffe8aa}{ATK\%}}$ buffs **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Medical Club Teresse](../assets/images/damage-formula/illust_inven_char001106_117.avif){.icon-portrait}
                    </td>
                    <td><strong>Medical Club Teresse</strong></td>
                    <td>$50\% \sim 120\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td rowspan="2" align="center">
                    ![Homunculus Lathel](../assets/images/damage-formula/illust_inven_char000103_59.avif){.icon-portrait}
                    </td>
                    <td rowspan="2"><strong>Homunculus Lathel</strong></td>
                    <td>$60\% \sim 90\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center" rowspan="2">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td>$25\% \sim 70\%$</td>
                    <td>$\text{2 Turns}$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Dark Saintess Liberta](../assets/images/damage-formula/illust_inven_char003801_164.avif){.icon-portrait}
                    </td>
                    <td><strong>Dark Saintess Liberta</strong></td>
                    <td>$35\% \sim 115\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Priest of Vitality Arines](../assets/images/damage-formula/illust_inven_char103701_36.avif){.icon-portrait}
                    </td>
                    <td><strong>Priest of Vitality Arines</strong></td>
                    <td>$25\% \sim 80\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$20\% \sim 60\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Kind Student Samay](../assets/images/damage-formula/illust_inven_char101402_16.avif){.icon-portrait}
                    </td>
                    <td><strong>Kind Student Samay</strong></td>
                    <td>$20\% \sim 50\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$2 \sim 0$</td>
                </tr>
            </tbody>
        </table>
    
    ---
    
    Costumes providing {{MATK}} $\text{\textcolor{ffa6ff}{MATK\%}}$ buffs **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Medical Club Teresse](../assets/images/damage-formula/illust_inven_char001106_117.avif){.icon-portrait}
                    </td>
                    <td><strong>Medical Club Teresse</strong></td>
                    <td>$50\% \sim 120\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td rowspan="2" align="center">
                    ![Queen of Gluttis Granadair](../assets/images/damage-formula/illust_inven_char067702_194.avif){.icon-portrait}
                    </td>
                    <td rowspan="2"><strong>Queen of Gluttis Granadair</strong></td>
                    <td>$50\% \sim 80\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center" rowspan="2">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td>$45\% \sim 70\%$</td>
                    <td>$\text{2 Turns}$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![B-Rank Idol Helena](../assets/images/damage-formula/illust_inven_char061002_26.avif){.icon-portrait}
                    </td>
                    <td><strong>B-Rank Idol Helena</strong></td>
                    <td>$35\% \sim 115\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Retired Legend Olivier](../assets/images/damage-formula/illust_inven_char003604_196.avif){.icon-portrait}
                    </td>
                    <td><strong>Retired Legend Olivier</strong></td>
                    <td>$60\% \sim 100\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$20\% \sim 60\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Kind Student Samay](../assets/images/damage-formula/illust_inven_char101402_16.avif){.icon-portrait}
                    </td>
                    <td><strong>Kind Student Samay</strong></td>
                    <td>$20\% \sim 50\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$2 \sim 0$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Hand of Salvation Elpis](../assets/images/damage-formula/illust_inven_char003101_122.avif){.icon-portrait}
                    </td>
                    <td><strong>Hand of Salvation Elpis</strong></td>
                    <td>$25\% \sim 80\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---
        
    Costumes providing {{ATK}} $\text{\textcolor{ffe8aa}{ATK\%}}$ buffs to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![The Sword Queen Sylvia](../assets/images/damage-formula/illust_inven_char001002_102.avif){.icon-portrait}
                    </td>
                    <td><strong>The Sword Queen<br>Sylvia</strong></td>
                    <td>$100\% \sim 225\%$</td>
                    <td>$2 \sim 6 \text{ Turns}$</td>
                    <td align="center">1</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Herb Tracker Lathel](../assets/images/damage-formula/illust_inven_char000101_1.avif){.icon-portrait}
                    </td>
                    <td><strong>Herb Tracker<br>Lathel</strong></td>
                    <td>$50\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Lonely Survivor Lathel](../assets/images/damage-formula/illust_inven_char000102_44.avif){.icon-portrait}
                    </td>
                    <td><strong>Lonely Survivor<br>Lathel</strong></td>
                    <td>$50\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Promise of Vengeance Lathel](../assets/images/damage-formula/illust_inven_char000105_42.avif){.icon-portrait}
                    </td>
                    <td><strong>Promise of Vengeance<br>Lathel</strong></td>
                    <td>$50\% \sim 60\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Maid Name C Rubia](../assets/images/damage-formula/illust_inven_char000806_116.avif){.icon-portrait}
                    </td>
                    <td><strong>Maid Name C<br>Rubia</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Noble Flame Ikaruga](../assets/images/damage-formula/illust_inven_char021001_198.avif){.icon-portrait}
                    </td>
                    <td><strong>Noble Flame<br>Ikaruga</strong></td>
                    <td>$60\% \sim 100\%$</td>
                    <td>$\infty \newline \text{3 stacks MAX} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Laid-back Lifeguard Nebris](../assets/images/damage-formula/illust_inven_char003302_130.avif){.icon-portrait}
                    </td>
                    <td><strong>Laid-back Lifeguard<br>Nebris</strong></td>
                    <td>$50\%$</td>
                    <td>$6 \sim 10 \text{ Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Justia](../assets/images/damage-formula/illust_inven_char000206_91.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party<br>Justia</strong></td>
                    <td>$150\% \sim 300\%$</td>
                    <td>$8 \sim 12 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Comeback Idol Ventana](../assets/images/damage-formula/illust_inven_char067003_111.avif){.icon-portrait}
                    </td>
                    <td><strong>Comeback Idol<br>Ventana</strong></td>
                    <td>$50\% \sim 125\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Whitebolt Yuri](../assets/images/damage-formula/illust_inven_char065102_105.avif){.icon-portrait}
                    </td>
                    <td><strong>Whitebolt<br>Yuri</strong></td>
                    <td>$150\% \sim 160\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Haggard Delinquent Emma](../assets/images/damage-formula/illust_inven_char101301_61.avif){.icon-portrait}
                    </td>
                    <td><strong>Haggard Delinquent<br>Emma</strong></td>
                    <td>$200\% \sim 500\%$</td>
                    <td>$6 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$25\% \sim 40\%$</td>
                    <td>$10 \text{ Turns}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
            </tbody>
        </table>

    ---
        
    Costumes providing {{MATK}} $\text{\textcolor{ffa6ff}{MATK\%}}$ buffs to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Track and Field Team Loen](../assets/images/damage-formula/illust_inven_char003202_133.avif){.icon-portrait}
                    </td>
                    <td><strong>Track and Field Team<br>Loen</strong></td>
                    <td>$40\% \sim 80\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Beachside Justice Michaela](../assets/images/damage-formula/illust_inven_char067401_137.avif){.icon-portrait}
                    </td>
                    <td><strong>Beachside Justice<br>Michaela</strong></td>
                    <td>$200\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Apostle Olivier](../assets/images/damage-formula/illust_inven_char003602_176.avif){.icon-portrait}
                    </td>
                    <td><strong>Apostle<br>Olivier</strong></td>
                    <td>$50\% \sim 80\%$</td>
                    <td>$8 \sim 10 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{Pressure}$"
    Pressure is a debuff that reduces stat-boosting buff efficiency. **It does not affect initial character stats, only buffs.**
    
    It affects such stats as:

    * {{HP}} **HP%**{.orange}
    * {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta}
    * {{CritRate}} **Crit Rate**
    * {{CritDMG}} **Crit Damage**
    * {{DEF}} **DEF%**{.yellow} / {{MRES}} **MRES%**{.magenta}
    * **Property Damage**

    !!! example "Example"
        Maxed **Medical Club Teresse**, which would give $120\%$ {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} buff, would only apply $60\%$ instead. 

        On the contrary, her **Beachside Angel** costume will still give 200% Augmentation Buff as if it's not considered a stat-boosting buff.

    ??? image "Pressure Effect in a fight"
        ![Pressure Effect in a fight](../assets/images/damage-formula/pressure.avif)
=== "$\text{\textcolor{ffe8aa}{ATK\%} Debuffs}$"

    {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Debuffs are straightforward: they reduce character's {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta}. 

    Because it stacks with buffs additively, it is more or less not important unless you are in a fight where the boss doesn't gain any buffs.

    This debuff is considered Weakening, so any enemy with **Immune to Weakening** Status Effect will ignore the reduction. 

    Additionally, despite {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Debuffs, damage will always be $\ge 1$ even with 0 {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} on the enemy.

    ---
    As mentioned above, these debuffs are not very widely used, especially since a lot of bosses have Weakening immunity or you can sustain just fine, while in PvP there are buffs pretty much nullifying your debuffs. 

    However, it is worth mentioning that there are Story Pack fights such as **Partan** (Story Pack 11) and **Nox** (Story Pack 12), where you can use **Gynt** and **Remnunt** to extend fight to the Death Time, where you will deal increased damage to the boss.

    ---
        
    Costumes providing {{ATK}} $\text{\textcolor{ffe8aa}{ATK\%}}$ debuffs:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Debuff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Combat Doctor Remnunt](../assets/images/damage-formula/illust_inven_char100401_8.avif){.icon-portrait}
                    </td>
                    <td><strong>Combat Doctor<br>Remnunt</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Sage of Blue Clouds Olstein](../assets/images/damage-formula/illust_inven_char000604_72.avif){.icon-portrait}
                    </td>
                    <td><strong>Sage of Blue Clouds<br>Olstein</strong></td>
                    <td>$70\%$</td>
                    <td>$2 \sim 4 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Lugo Hunter Gynt](../assets/images/damage-formula/illust_inven_char100101_4.avif){.icon-portrait}
                    </td>
                    <td><strong>Lugo Hunter<br>Gynt</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![The Curse Celia](../assets/images/damage-formula/illust_inven_char101601_78.avif){.icon-portrait}
                    </td>
                    <td><strong>The Curse<br>Celia</strong></td>
                    <td>$35\% \sim 65 \%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>

    ---
        
    Costumes providing {{MATK}} $\text{\textcolor{ffa6ff}{MATK\%}}$ debuffs:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Debuff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Sage of Blue Clouds Olstein](../assets/images/damage-formula/illust_inven_char000604_72.avif){.icon-portrait}
                    </td>
                    <td><strong>Sage of Blue Clouds<br>Olstein</strong></td>
                    <td>$70\%$</td>
                    <td>$2 \sim 4 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Descendant of the Great Witch Celia](../assets/images/damage-formula/illust_inven_char060402_28.avif){.icon-portrait}
                    </td>
                    <td><strong>Descendant of the Great Witch<br>Celia</strong></td>
                    <td>$35\% \sim 65 \%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{\textcolor{white}{CDMG}}$"

    {{CritDMG}} **Crit Damage** matters when a character **crits**, meaning it is essential to have high {{CritRate}} **Crit Rate** or guarantee it via other methods.

    !!! example "{{CritRate}} Crit Rate"
        {{CritRate}} **Crit Rate** is additive, similar to other buffs within same multiplier: 

        $\text{\textcolor{white}{Crit Rate\%} Total Buff =  \textcolor{white}{Crit Rate\%} Inherent + \textcolor{white}{Crit Rate\%} Gear} + [\text{\textcolor{white}{Crit Rate\%} Buff 1} + \dots] \times [100\% - \text{Pressure\%}] $

        Here **Inherent {{CritRate}} Crit Rate** means the one from the character itself. It varies from $0\%$ to $20\%$, depending on the character. Characters with $0\%$ {{CritRate}} Crit Rate **cannot crit**.

    ---

    $\text{\textcolor{white}{CDMG\%}}$ addend refers to the sum of inherent, gear and bonding {{CritDMG}} **Crit Damage**:
    
    $\text{\textcolor{white}{CDMG\%}} = \text{Character's Base \textcolor{white}{CDMG\%}} + \text{Gear \textcolor{white}{CDMG\%}} + \text{ Potential \textcolor{white}{CDMG\%}}$

    ---

    Costumes providing {{CritRate}} $\text{\textcolor{white}{Crit Rate\%}}$ buffs **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Dark Saintess Liberta](../assets/images/damage-formula/illust_inven_char003801_164.avif){.icon-portrait}
                    </td>
                    <td><strong>Dark Saintess Liberta</strong></td>
                    <td>$25\% \sim 50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Adventurer of the Unknown Diana](../assets/images/damage-formula/illust_inven_char002401_58.avif){.icon-portrait}
                    </td>
                    <td><strong>Adventurer of the Unknown Diana</strong></td>
                    <td>$20\% \sim 30\%$</td>
                    <td>$\text{8 Turns} \newline \text{\textcolor{AFDBF5}{[Aura]}}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![B-Rank Idol Helena](../assets/images/damage-formula/illust_inven_char061002_26.avif){.icon-portrait}
                    </td>
                    <td><strong>B-Rank Idol Helena</strong></td>
                    <td>$25\% \sim 50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Priest of Vitality Arines](../assets/images/damage-formula/illust_inven_char103701_36.avif){.icon-portrait}
                    </td>
                    <td><strong>Priest of Vitality Arines</strong></td>
                    <td>$30\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Red Riding Hood Rou](../assets/images/damage-formula/illust_inven_char000502_98.avif){.icon-portrait}
                    </td>
                    <td><strong>Red Riding Hood Rou</strong></td>
                    <td>$30\% \sim 50\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Hand of Salvation Elpis](../assets/images/damage-formula/illust_inven_char003101_122.avif){.icon-portrait}
                    </td>
                    <td><strong>Hand of Salvation Elpis</strong></td>
                    <td>$30\% \sim 35\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing {{CritDMG}} $\text{\textcolor{white}{Crit DMG\%}}$ buffs **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![The Gluttonous Refithea](../assets/images/damage-formula/illust_inven_char066801_120.avif){.icon-portrait}
                    </td>
                    <td><strong>The Gluttonous Refithea</strong></td>
                    <td>$50\% \sim 125\%$</td>
                    <td>$\text{6 Turns} \newline \text{\textcolor{AFDBF5}{[Aura]}}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Red Riding Hood Rou](../assets/images/damage-formula/illust_inven_char000502_98.avif){.icon-portrait}
                    </td>
                    <td><strong>Red Riding Hood Rou</strong></td>
                    <td>$150\% \sim 300\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing {{CritRate}} $\text{\textcolor{white}{Crit Rate\%}}$ buffs to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Pool Party Lathel](../assets/images/damage-formula/illust_inven_char000106_90.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party Lathel</strong></td>
                    <td>$100\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Miracle Rose Liberta](../assets/images/damage-formula/illust_inven_char003803_201.avif){.icon-portrait}
                    </td>
                    <td><strong>Miracle Rose Liberta</strong></td>
                    <td>$40 \sim 100\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Gray](../assets/images/damage-formula/illust_inven_char000406_93.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party Gray</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Daughter of Starwind High Elf Archer](../assets/images/damage-formula/illust_inven_char020801_162.avif){.icon-portrait}
                    </td>
                    <td><strong>Daughter of Starwind<br>High Elf Archer</strong></td>
                    <td>$100\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Haggard Delinquent Emma](../assets/images/damage-formula/illust_inven_char101301_61.avif){.icon-portrait}
                    </td>
                    <td><strong>Haggard Delinquent<br>Emma</strong></td>
                    <td>$30\%$</td>
                    <td>$6 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Stray Cat Rou](../assets/images/damage-formula/illust_inven_char000506_107.avif){.icon-portrait}
                    </td>
                    <td><strong>Stray Cat Rou</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing {{CritDMG}} $\text{\textcolor{white}{Crit DMG\%}}$ buffs to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Night of Death Mamonir](../assets/images/damage-formula/illust_inven_char067801_192.avif){.icon-portrait}
                    </td>
                    <td><strong>Night of Death Mamonir</strong></td>
                    <td>$200\% \sim 300\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Gentle Maid Anastasia](../assets/images/damage-formula/illust_inven_char060501_79.avif){.icon-portrait}
                    </td>
                    <td><strong>Gentle Maid Anastasia</strong></td>
                    <td>$200\% \sim 500\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Fire Graffiti Anastasia](../assets/images/damage-formula/illust_inven_char060502_46.avif){.icon-portrait}
                    </td>
                    <td><strong>Fire Graffiti Anastasia</strong></td>
                    <td>$200\% \sim 500\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Gray](../assets/images/damage-formula/illust_inven_char000406_93.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party Gray</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Labyrinth Gatekeeper Nebris](../assets/images/damage-formula/illust_inven_char003301_146.avif){.icon-portrait}
                    </td>
                    <td><strong>Labyrinth Gatekeeper Nebris</strong></td>
                    <td>$200\% \sim 300\%$</td>
                    <td>$6 \text{ Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Comeback Idol Yuri](../assets/images/damage-formula/illust_inven_char065103_110.avif){.icon-portrait}
                    </td>
                    <td><strong>Comeback Idol Yuri</strong></td>
                    <td>$150\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Acting Archbishop Michaela](../assets/images/damage-formula/illust_inven_char067403_168.avif){.icon-portrait}
                    </td>
                    <td><strong>Acting Archbishop Michaela</strong></td>
                    <td>$300\% \sim 500\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{Chains}$"
    The **Chain** system is a mechanic that increases damage with each repetitive hit on the same tile / enemy.
    
    Generally speaking, each hit generates 1 chain by default, with the possibility to increase the amount by applying **Chain Reinforcement** status effect:

    $\text{Chain Per Hit} = 1 + \text{Amount of Applied Chain Reinforcements}$

    ---

    Each **Chain** increases damage by 10% by default, however there is an effect called **Increased Chain DMG**, which increases that value more.

    ---

    Costumes providing **Chain Reinforcement** buff **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Pure White Blessing Refithea](../assets/images/damage-formula/illust_inven_char066802_121.avif){.icon-portrait}
                    </td>
                    <td><strong>Pure White Blessing Refithea</strong></td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing $\text{Increased Chain DMG\%}$:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Poolside Guardian Zenith](../assets/images/damage-formula/illust_inven_char061404_172.avif){.icon-portrait}
                    </td>
                    <td><strong>Poolside Guardian Zenith</strong></td>
                    <td>$5\% \sim 10\%$</td>
                    <td>$2 \sim 4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing **Chain Reinforcement** buff to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Water Park Queen Wilhelmina](../assets/images/damage-formula/illust_inven_char067603_171.avif){.icon-portrait}
                    </td>
                    <td><strong>Water Park Queen Wilhelmina</strong></td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Masquerade Bunny Celia](../assets/images/damage-formula/illust_inven_char060403_109.avif){.icon-portrait}
                    </td>
                    <td><strong>Masquerade Bunny Celia</strong></td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{Vulnerability}$"
    Vulnerability is a **debuff** that increases damage received by the enemy. There are 5 types of Vulnerability: 

    * **General**, which increases damage in every instance
    * **Damage Type-related**, which increases damage only to the {{Physical}} **Physical**{.yellow} or {{Magical}} **Magical**{.magenta} damage type. 
        * {{Physical}} **Physical**{.yellow} Vulnerability is described as **Vulnerability (Physical)**
        * {{Magical}} **Magical**{.magenta} Vulnerability is described as **Vulnerability (Magic)**
    * **Property-related**, that increases damage if only a specific property deals damage
    * **Summons-related**, that increases damage dealt by summons

    ---

    Similar to any other buff from the same multiplier, different Vulnerabilities stack additively:

    $\text{Total Vulnerability} = \text{Vulnerability 1} + \text{Vulnerability 2} + \dots$

    ---

    Costumes providing **General Vulnerability**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Vulnerability Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Robin Hood Zenith](../assets/images/damage-formula/illust_inven_char061402_101.avif){.icon-portrait}
                    </td>
                    <td><strong>Robin Hood Zenith</strong></td>
                    <td>$20\% \sim 100\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$2 \sim 0$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$30\% \sim 50\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadowed Dream Sonya](../assets/images/damage-formula/illust_inven_char003901_180.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadowed Dream Sonya</strong></td>
                    <td>$55\% \sim 125\%$</td>
                    <td>$\text{4 Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing {{Physical}} **Physical**{.yellow} **Vulnerability**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Vulnerability Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Game Club Rafina](../assets/images/damage-formula/illust_inven_char060706_118.avif){.icon-portrait}
                    </td>
                    <td><strong>Game Club Rafina</strong></td>
                    <td>$50\% \sim 100\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Your Very Own Cat Eris](../assets/images/damage-formula/illust_inven_char020002_127.avif){.icon-portrait}
                    </td>
                    <td><strong>Your Very Own Cat Eris</strong></td>
                    <td>$100\% \sim 150\% \newline \text{\textcolor{AFDBF5}{[Main Target]}}$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Young Lady Blade](../assets/images/damage-formula/illust_inven_char003703_166.avif){.icon-portrait}
                    </td>
                    <td><strong>Young Lady Blade</strong></td>
                    <td>$100\% \sim 150\% \newline \text{\textcolor{AFDBF5}{[Main Target]}}$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing {{Magical}} **Magical**{.magenta} **Vulnerability**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Vulnerability Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Track and Field Captain Levia](../assets/images/damage-formula/illust_inven_char067301_132.avif){.icon-portrait}
                    </td>
                    <td><strong>Track and Field Captain Levia</strong></td>
                    <td>$60\% \sim 120\% \newline \text{\textcolor{AFDBF5}{[Main Target]}} \newline 40\% \sim 100\% \newline \text{\textcolor{AFDBF5}{[Otherwise]}}$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Earth Mother Believer Priestess](../assets/images/damage-formula/illust_inven_char020701_161.avif){.icon-portrait}
                    </td>
                    <td><strong>Earth Mother Believer Priestess</strong></td>
                    <td>$50\% \sim 75\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing **DoT Vulnerability**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Vulnerability Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Maid Bikini Rubia](../assets/images/damage-formula/illust_inven_char000807_178.avif){.icon-portrait}
                    </td>
                    <td><strong>Maid Bikini Rubia</strong></td>
                    <td>$150\% \sim 300\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing **Summons Vulnerability**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Vulnerability Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Apostle Morpeah](../assets/images/damage-formula/illust_inven_char003403_169.avif){.icon-portrait}
                    </td>
                    <td><strong>Apostle Morpeah</strong></td>
                    <td>$100\% \sim 180\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing **Property Vulnerability**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Vulnerability Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Wind Dancer Venaka](../assets/images/damage-formula/illust_inven_char067202_147.avif){.icon-portrait}
                    </td>
                    <td><strong>Wind Dancer Venaka</strong></td>
                    <td>$75\% \sim 150\% \newline \text{\textcolor{AFDBF5}{[Wind]}}$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Onsen Practitioner Ventana](../assets/images/damage-formula/illust_inven_char067004_157.avif){.icon-portrait}
                    </td>
                    <td><strong>Onsen Practitioner Ventana</strong></td>
                    <td>$100\% \sim 200\% \newline \text{\textcolor{AFDBF5}{[Light]}}$</td>
                    <td>$6 \sim 10 \text{ Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadowed Dream Sonya](../assets/images/damage-formula/illust_inven_char003901_180.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadowed Dream Sonya</strong></td>
                    <td>$75\% \sim 175\% \newline \text{\textcolor{AFDBF5}{[Darkness]}}$</td>
                    <td>$\text{4 Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{DMG Increase\%}$"

    $\text{DMG Increase\%}$ Buffs are buffs that technically act as reverse [**Vulnerability**](#__tabbed_1_8), increasing **your own characters'** damage instead of forcing the enemy to take more damage.

    So far, all these buffs are called **Augmentation**, which you can think of as a buff with conditions. The condition can be either related to chains, times getting hit or the amount of debuffs being removed from allies. 

    In other words, it is similar to Conditional [$\text{Skill\%}$](#__tabbed_1_2) in a way.

    ---

    As always, this type of buffs from different sources is additive:

    $ \text{Total DMG Increase\%} = \text{DMG Increase\% 1} + \text{DMG Increase\% 2} + \dots$

    ---

    However, since these buffs belong to the same bracket as **Vulnerability**, note that high Vulnerability will decrease efficiency of these buffs. 

    ---

    Costumes providing $\text{DMG Increase\%}$ Buffs **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Beachside Angel Teresse](../assets/images/damage-formula/illust_inven_char001107_135.avif){.icon-portrait}
                    </td>
                    <td><strong>Beachside Angel<br>Teresse</strong></td>
                    <td>$100\% \sim 200\% \newline \text{\textcolor{AFDBF5}{[When attacking enemy}} \newline \text{\textcolor{AFDBF5}{with a Chain count 5 or less]}}$</td>
                    <td>$4 \sim 8 \text{ Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center" rowspan="2">
                    ![Shrine Maiden of Purification Granadair](../assets/images/damage-formula/illust_inven_char067701_193.avif){.icon-portrait}
                    </td>
                    <td rowspan="2"><strong>Shrine Maiden<br>of Purification<br>Granadair</strong></td>
                    <td>$75\% \sim 120\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center" rowspan="2">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td>$10\% \times \text{\textcolor{AFDBF5}{Debuffs Absorbed}}$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Onsen Manager Liberta](../assets/images/damage-formula/illust_inven_char003802_159.avif){.icon-portrait}
                    </td>
                    <td><strong>Onsen Manager<br>Liberta</strong></td>
                    <td>$80\% \sim 130\% \newline \text{\textcolor{AFDBF5}{[When attacking enemy}} \newline \text{\textcolor{AFDBF5}{with 10 Chains or more]}}$</td>
                    <td>$6 \sim 4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![New Hire Seir](../assets/images/damage-formula/illust_inven_char101103_150.avif){.icon-portrait}
                    </td>
                    <td><strong>New Hire<br>Seir</strong></td>
                    <td>$10\% \sim 22\% \times \newline \text{\textcolor{AFDBF5}{[Amount of times}} \newline \text{\textcolor{AFDBF5}{Seir gets hit]}}$</td>
                    <td>$6 \sim 8 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing $\text{DMG Increase\%}$ Buffs to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Labyrinth Gatekeeper Nebris](../assets/images/damage-formula/illust_inven_char003301_146.avif){.icon-portrait}
                    </td>
                    <td><strong>Labyrinth Gatekeeper<br>Nebris</strong></td>
                    <td>$100\% \sim 150\% \newline \text{\textcolor{AFDBF5}{[If no Augmentation}} \newline \text{\textcolor{AFDBF5}{Status Effect]}}$</td>
                    <td>$6 \text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Fist of Conviction Yozakura](../assets/images/damage-formula/illust_inven_char020301_141.avif){.icon-portrait}
                    </td>
                    <td><strong>Fist of Conviction<br>Yozakura</strong></td>
                    <td>$400\% \sim 1200\% \newline \text{\textcolor{AFDBF5}{[For 1 next}} \newline  \text{\textcolor{AFDBF5}{Basic Attack]}}$</td>
                    <td>$\text{Until} \newline \text{Basic Attack}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{\textcolor{8A9A5B}{Property}}$"
    Property is another aspect of any character. There are a total of 6 Properties: ![Water](../assets/images/battle-system/icons/elementicon1_1.avif){.icon} Water, ![Fire](../assets/images/battle-system/icons/elementicon2_2.avif){.icon} Fire, ![Wind](../assets/images/battle-system/icons/elementicon3_3.avif){.icon} Wind, ![Light](../assets/images/battle-system/icons/elementicon4_4.avif){.icon} Light, ![Darkness](../assets/images/battle-system/icons/elementicon5_5.avif){.icon} Darkness and ![Neutral](../assets/images/battle-system/icons/elementicon6_6.avif){.icon} Neutral.

    Depending on the opponent, there can be 3 outcomes: 

    * You gain **Property Advantage**, dealing **extra damage** due to a superior Property
    * You neither deal more nor deal less damage, due to a Neutral enemy or cases like Light -> Water. 
    * You deal **less damage** due to **Property Disadvantage**.

    ---

    Similar to any other buff, $\text{Property Damage\% Buffs}$ stack additively: 
    $\text{\textcolor{8A9A5B}{Property Damage\%} Total Buffs} = \text{\textcolor{8A9A5B}{Property Damage\%} Buff 1} + \text{\textcolor{8A9A5B}{Property Damage\%} Buff 2} + \dots$

    ---

    $\text{\textcolor{8A9A5B}{Property Damage\%}}$ in the formula refers to the **character's own** Property Damage. Usually it consists of the initial, awakening and [bond](../progression/potentials.md) ones:

    $\text{\textcolor{8A9A5B}{Property Damage\%}} = 50\% + \text{\textcolor{8A9A5B}{Property Damage\%} from Awakening} + \text{\textcolor{8A9A5B}{Property Damage\%} from Bond}$

    ---

    Costumes providing $\text{Property Damage\%}$ buffs **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Adventurer of the Unknown Diana](../assets/images/damage-formula/illust_inven_char002401_58.avif){.icon-portrait}
                    </td>
                    <td><strong>Adventurer of the Unknown<br>Diana</strong></td>
                    <td>$100\% \sim 220\%$</td>
                    <td>$\text{8 Turns} \newline \text{\textcolor{AFDBF5}{[Aura]}}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Magical Innovator Diana](../assets/images/damage-formula/illust_inven_char002403_195.avif){.icon-portrait}
                    </td>
                    <td><strong>Magical Innovator<br>Diana</strong></td>
                    <td>$25\% \sim 200\% \newline \text{\textcolor{AFDBF5}{[Per Summon]}}$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 3 + 1 \text{ per activation}$</td>
                </tr>                
                <tr>
                    <td align="center">
                    ![Pure White Blessing Refithea](../assets/images/damage-formula/illust_inven_char066802_121.avif){.icon-portrait}
                    </td>
                    <td><strong>Pure White Blessing<Br>Refithea</strong></td>
                    <td>$40\% \sim 100\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Poolside Fairy Refithea](../assets/images/damage-formula/illust_inven_char066803_173.avif){.icon-portrait}
                    </td>
                    <td><strong>Poolside Fairy<br>Refithea</strong></td>
                    <td>$\newline 50\% \sim 100\% \newline \text{\textcolor{AFDBF5}{[if Light Property]}} \newline 25\% \sim 50\% \newline \text{\textcolor{AFDBF5}{[otherwise]}}$</td>
                    <td>$\text{8 Turns}$</td>
                    <td align="center">$7 \sim 6$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing $\text{Property Damage\%}$ buffs to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Frozen Queen Wilhelmina](../assets/images/damage-formula/illust_inven_char067604_189.avif){.icon-portrait}
                    </td>
                    <td><strong>Frozen Queen<br>Wilhelmina</strong></td>
                    <td>$30\% \sim 60\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Laid-back Lifeguard Nebris](../assets/images/damage-formula/illust_inven_char003302_130.avif){.icon-portrait}
                    </td>
                    <td><strong>Laid-back Lifeguard<br>Nebris</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{2 Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Blood Glutton Justia](../assets/images/damage-formula/illust_inven_char000203_41.avif){.icon-portrait}
                    </td>
                    <td><strong>Blood Glutton<br>Justia</strong></td>
                    <td>$200\% \sim 400\%$</td>
                    <td>$\text{8 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{\textcolor{ffe8aa}{DEF}}$"
    {{DEF}} $\text{\textcolor{ffe8aa}{DEF}}$ / {{MRES}} $\text{\textcolor{ffa6ff}{MRES}}$ are two main stats of a character. They reduce damage from the enemy. 

    * $\text{\textcolor{ffe8aa}{DEF}}$ decreases all incoming {{Physical}} **Physical**{.yellow} Damage.
    * $\text{\textcolor{ffa6ff}{MRES}}$ decreases all incoming {{Magical}} **Magical**{.magenta} Damage.

    ---

    During calculations, $\text{\textcolor{ffe8aa}{DEF}}$ / $\text{\textcolor{ffa6ff}{MRES}}$ are capped at $90\%$. That means no matter how high the stat is, only a maximum of $90\%$ will be used. This, however, does not actually remove anything above that mark, meaning going above can be useful when facing $\text{\textcolor{ffe8aa}{DEF}}$ / $\text{\textcolor{ffa6ff}{MRES}}$ **Reduction**.

    ---

    **Fixed**, **Consumed** and **Pure** Damage ignores $\text{\textcolor{ffe8aa}{DEF}}$ / $\text{\textcolor{ffa6ff}{MRES}}$ completely.

    ---
    
    Costumes providing {{DEF}} $\text{\textcolor{ffe8aa}{DEF\%}}$ reduction:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Debuff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Code Name A Rafina](../assets/images/damage-formula/illust_inven_char060702_49.avif){.icon-portrait}
                    </td>
                    <td><strong>Code Name A<br>Rafina</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Empress of the Ocean Rubia](../assets/images/damage-formula/illust_inven_char000804_74.avif){.icon-portrait}
                    </td>
                    <td><strong>Empress of the Ocean<br>Rubia</strong></td>
                    <td>$25\% \sim 45\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Lovely Lady Elise](../assets/images/damage-formula/illust_inven_char060801_82.avif){.icon-portrait}
                    </td>
                    <td><strong>Lovely Lady<br>Elise</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \sim 6\text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![B-Rank Manager Gray](../assets/images/damage-formula/illust_inven_char000402_24.avif){.icon-portrait}
                    </td>
                    <td><strong>B-Rank Manager<br>Gray</strong></td>
                    <td>$50\%$</td>
                    <td>$2\text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Nature's Claw Rou](../assets/images/damage-formula/illust_inven_char000504_71.avif){.icon-portrait}
                    </td>
                    <td><strong>Nature's Claw<br>Rou</strong></td>
                    <td>$20\%$</td>
                    <td>$2\text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![The Curse Celia](../assets/images/damage-formula/illust_inven_char101601_78.avif){.icon-portrait}
                    </td>
                    <td><strong>The Curse<br>Celia</strong></td>
                    <td>$10\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![B-Rank Idol Eleaneer](../assets/images/damage-formula/illust_inven_char061102_27.avif){.icon-portrait}
                    </td>
                    <td><strong>B-Rank Idol<br>Eleaneer</strong></td>
                    <td>$20\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Liberated Marauder Kry](../assets/images/damage-formula/illust_inven_char101501_65.avif){.icon-portrait}
                    </td>
                    <td><strong>Liberated Marauder<br>Kry</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>

    ---
    
    Costumes providing {{MRES}} $\text{\textcolor{ffa6ff}{MRES\%}}$ reduction:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Debuff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Magic School Professor Scheherazade](../assets/images/damage-formula/illust_inven_char000303_43.avif){.icon-portrait}
                    </td>
                    <td><strong>Magic School Professor<br>Scheherazade</strong></td>
                    <td>$15\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Daydream Bunny Morpeah](../assets/images/damage-formula/illust_inven_char003402_152.avif){.icon-portrait}
                    </td>
                    <td><strong>Daydream Bunny<br>Morpeah</strong></td>
                    <td>$30\% \newline \text{\textcolor{AFDBF5}{[Summon]}}$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Lovely Lady Elise](../assets/images/damage-formula/illust_inven_char060801_82.avif){.icon-portrait}
                    </td>
                    <td><strong>Lovely Lady<br>Elise</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \sim 6\text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![DJ Venaka](../assets/images/damage-formula/illust_inven_char067201_129.avif){.icon-portrait}
                    </td>
                    <td><strong>DJ<br>Venaka</strong></td>
                    <td>$50\%$</td>
                    <td>$4\text{ Turns}$</td>
                    <td align="center">$4 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Nightmare Bunny Eclipse](../assets/images/damage-formula/illust_inven_char000706_106.avif){.icon-portrait}
                    </td>
                    <td><strong>Nightmare Bunny<br>Eclipse</strong></td>
                    <td>$15\% \sim 20\%$</td>
                    <td>$4\text{ Turns}$</td>
                    <td align="center">$3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Descendant of the Great Witch Celia](../assets/images/damage-formula/illust_inven_char060402_28.avif){.icon-portrait}
                    </td>
                    <td><strong>Descendant of the Great Witch<br>Celia</strong></td>
                    <td>$10\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Kind Liberator Samay](../assets/images/damage-formula/illust_inven_char101401_66.avif){.icon-portrait}
                    </td>
                    <td><strong>Kind Liberator<br>Samay</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes decreasing **own** {{DEF}} $\text{\textcolor{ffe8aa}{DEF}}$ / {{MRES}} $\text{\textcolor{ffa6ff}{MRES}}$:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Debuff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Acting Archbishop Michaela](../assets/images/damage-formula/illust_inven_char067403_168.avif){.icon-portrait}
                    </td>
                    <td><strong>Acting Archbishop Michaela</strong></td>
                    <td>$90\% \newline \text{\textcolor{ffe8aa}{DEF} \& \textcolor{ffa6ff}{MRES}}$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{DMG Reduction}$"
    $\text{DMG Reduction}$ is a separate buff that decreases incoming damage, similar to {{DEF}} $\text{\textcolor{ffe8aa}{DEF}}$ and {{MRES}} $\text{\textcolor{ffa6ff}{MRES}}$, but working in a different way.

    It's more known as a **Barrier** buff, being part of the skillset for multiple costumes in the game.

    ---

    Barriers from different sources stack differently compared to other buffs.
    Instead of being additive, they are multiplicative:

    $(100\% - \text{Target's DMG Reduction\% Buffs Total}) = \\\\
    = (100\% - \text{Target's DMG Reduction\% Buff 1}) \times \\\\
    \times \; (100\% - \text{Target's DMG Reduction\% Buff 2}) \times \dots$

    For example, combining 2 Barriers of $70\%$ and $50\%$ will essentially give you $85\%$ Barrier.

    This system ensures that a barrier can never achieve $100\%$, meaning some damage will go through anyway. 

    ---

    Similar to **Vulnerability**, Barriers *can* be {{Physical}} **Physical**{.yellow} or {{Magical}} **Magical**{.magenta}, meaning they will reduce incoming damage from only one damage type. 

    ---

    Costumes providing **Barrier** buff **to allies**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Top Idol Helena](../assets/images/damage-formula/illust_inven_char061001_83.avif){.icon-portrait}
                    </td>
                    <td><strong>Top Idol<br>Helena</strong></td>
                    <td>$30\% \sim 70\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![The Gluttonous Refithea](../assets/images/damage-formula/illust_inven_char066801_120.avif){.icon-portrait}
                    </td>
                    <td><strong>The Gluttonous<br>Refithea</strong></td>
                    <td>$25\% \sim 50\%$</td>
                    <td>$\text{6 Turns} \newline \text{\textcolor{AFDBF5}{[Aura]}}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
            </tbody>
        </table>

    ---

    Costumes providing **Barrier** buff to **themselves only**:
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Buff Value</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Desert Flower Sylvia](../assets/images/damage-formula/illust_inven_char001001_22.avif){.icon-portrait}
                    </td>
                    <td><strong>Desert Flower<br>Sylvia</strong></td>
                    <td>$50\% \sim 75\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$4 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Disciplinary Committee Glacia](../assets/images/damage-formula/illust_inven_char066906_119.avif){.icon-portrait}
                    </td>
                    <td><strong>Disciplinary Committee<br>Glacia</strong></td>
                    <td>$50\% \newline \text{\textcolor{ffa6ff}{[Magic]}}$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Beach Vacation Morpeah](../assets/images/damage-formula/illust_inven_char003401_136.avif){.icon-portrait}
                    </td>
                    <td><strong>Beach Vacation<br>Morpeah</strong></td>
                    <td>$30\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$6 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Mercenary Knight Carlson](../assets/images/damage-formula/illust_inven_char103201_31.avif){.icon-portrait}
                    </td>
                    <td><strong>Mercenary Knight<br>Carlson</strong></td>
                    <td>$35\% \sim 65\% \newline \text{\textcolor{ffe8aa}{[Physical]}}$</td>
                    <td>$2 \sim 4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Dark Knight Lathel](../assets/images/damage-formula/illust_inven_char000104_69.avif){.icon-portrait}
                    </td>
                    <td><strong>Dark Knight<br>Lathel</strong></td>
                    <td>$50\% \sim 65\% \newline \text{\textcolor{ffe8aa}{[Physical]}}$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Orcbolg Goblin Slayer](../assets/images/damage-formula/illust_inven_char020601_160.avif){.icon-portrait}
                    </td>
                    <td><strong>Orcbolg<br>Goblin Slayer</strong></td>
                    <td>$50\% \sim 75\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Killer Doll Lecliss](../assets/images/damage-formula/illust_inven_char060601_80.avif){.icon-portrait}
                    </td>
                    <td><strong>Killer Doll<br>Lecliss</strong></td>
                    <td>$45\% \sim 85\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Magical Innovator Diana](../assets/images/damage-formula/illust_inven_char002403_195.avif){.icon-portrait}
                    </td>
                    <td><strong>Magical Innovator<br>Diana</strong></td>
                    <td>$20\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Angelica](../assets/images/damage-formula/illust_inven_char066402_95.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party<br>Angelica</strong></td>
                    <td>$75\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Neon Savior Angelica](../assets/images/damage-formula/illust_inven_char066403_96.avif){.icon-portrait}
                    </td>
                    <td><strong>Neon Savior<br>Angelica</strong></td>
                    <td>$75\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$6 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![The Fallen Angelica](../assets/images/damage-formula/illust_inven_char066401_94.avif){.icon-portrait}
                    </td>
                    <td><strong>The Fallen<br>Angelica</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Beautiful Girl Devotee Jayden](../assets/images/damage-formula/illust_inven_char101201_75.avif){.icon-portrait}
                    </td>
                    <td><strong>Beautiful Girl Devotee<br>Jayden</strong></td>
                    <td>$50\% \sim 75\% \newline \text{\textcolor{ffa6ff}{[Magic]}}$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Demon's Daughter Seir](../assets/images/damage-formula/illust_inven_char101101_67.avif){.icon-portrait}
                    </td>
                    <td><strong>Demon's Daughter<br>Seir</strong></td>
                    <td>$40\% \sim 85\%$</td>
                    <td>$4 \sim 6\text{ Turns}$</td>
                    <td align="center">$3 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![B-Rank Idol Seir](../assets/images/damage-formula/illust_inven_char101102_25.avif){.icon-portrait}
                    </td>
                    <td><strong>B-Rank Idol<br>Seir</strong></td>
                    <td>$40\% \sim 85\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$2 \sim 1$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Anonymous Sage Nartas](../assets/images/damage-formula/illust_inven_char065802_103.avif){.icon-portrait}
                    </td>
                    <td><strong>Anonymous Sage<br>Nartas</strong></td>
                    <td>$75\% \newline \text{\textcolor{ffa6ff}{[Magic]}}$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>
</div>

## The Example
As an example, let's take this fight.
![Fight Screenshot](../assets/images/damage-formula/fight_1.avif)

All Costumes are upgraded to the max. 

!!! abstract "Blade's Stats"

    * **Hit Multiplier**: $150\%$
    * {{ATK}} **ATK**: $2950$
    * {{CritDMG}} **Crit DMG**: $734.44\%$
    * **Darkness DMG**: $60\%$

!!! abstract "Enemy Stats"

    * {{DEF}} **DEF**: $25\%$

Liberta increases {{ATK}} **ATK** by $115\%$, Lathel increases {{ATK}} **ATK** by $160\%$, and Teresse increases **DMG Dealt** by $200\%$.

Putting that into the equation:

$\text{Damage} = \underbrace{2950}_\text{ATK} \times \underbrace{150\%}_\text{Skill Multiplier} \times \underbrace{(100\% + \overbrace{115\%}^\text{Liberta} + \overbrace{160\%}^\text{Lathel})}_\text{ATK Buffs} \times \underbrace{(100\% + \overbrace{200\%}^\text{Teresse})}_\text{DMG Increase} \times \underbrace{(100\% + 734.4\%)}_\text{Crit DMG} \times \underbrace{(100\% + 60\%)}_\text{Property} \times \underbrace{(100\% - 25\%)}_\text{Enemy DEF}$

$\text{Damage} = 2950 \times 1.5 \times 3.75 \times 3 \times 8.344 \times 1.6 \times 0.75 = 498449.7$

That confirms the received damage by the enemy in-game: 

![Fight Screenshot №2](../assets/images/damage-formula/fight_2.avif)

## Stat Limits
During calculations, some numbers have a cap to avoid weird bugs or mechanics.

* {{ATK}} **ATK**{.yellow} and {{MATK}} **MATK**{.magenta} are capped at $100,000$.
* {{HP}} **HP**{.orange} is capped at $50,000$.
* {{CritRate}} **Crit Rate**{.white} is capped at $100\%$.
* {{CritDMG}} **Crit DMG**{.white} is capped at $10,000$

* Chains are capped at $100$, except in the Last Night, where they have no cap.

## Additional Effects

### Death Time
Starting from Turn 11 in different modes, Death Time is introduced. 

Each 2 turns, each side receives 

* $100\%$ {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} **Buff**
* $100\%$ {{DEF}} **DEF**{.yellow} / {{MRES}} **MRES**{.magenta} **Debuffs**
* $50\%$ Damage Increase **Buff**

These (de)buffs follow the exact rules as described above, going into each of the brackets seamlessly.

### Environmental Effects
In [**Evil Castle**](../content-packs/evil-castle.md), especially **Tower of Jealousy** and **Tower of Wrath**, there are effects taking place that affect some stats, such as  **Pressure**, {{CritRate}} **Crit Rate** and more. 

Refer to the [**Evil Castle**](../content-packs/evil-castle.md) page for more detailed explanation.
