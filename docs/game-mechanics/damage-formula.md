# Damage Formula — Brown Dust II

!!! abstract "Tl;dr"
    WIP

## Damage Formula
$\small\text{Damage} = \\\\ \text{\textcolor{ffe8aa}{ATK}}^{\textcolor{AFDBF5}{[1,2]}} \\\\
\times \; \text{Skill\%} \\\\
\times \; (100\% + \text{\textcolor{ffe8aa}{ATK\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{\textcolor{ffe8aa}{ATK\%} Debuffs})^{\textcolor{AFDBF5}{[3]}} \\\\
\times \; (100\% + \text{\textcolor{white}{CDMG\%}} + \text{\textcolor{white}{CDMG\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{\textcolor{white}{CDMG\%} Debuffs})^{\textcolor{AFDBF5}{[4]}} \\
\times \; (100\% + (10\% + \text{Increase Chain DMG\%}) \times \text{Chains}) \\\\
\times \; (100\% + \text{Target's Vulnerability Debuffs\%} + \text{DMG Increase\% Buffs}) \\\\
\times \; (100\% + \text{\textcolor{8A9A5B}{Property Damage\%}} + \text{Season Buff\%} + \text{\textcolor{8A9A5B}{Property Damage\%} Buffs} \times [100\% - \text{Pressure\%}]  )^\text{[5]} \\\\
\times \; (100\% - (\text{Target's \textcolor{ffe8aa}{DEF\%}} + \text{Target's \textcolor{ffe8aa}{DEF\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{Target's \textcolor{ffe8aa}{DEF\%} Debuffs}))^{\textcolor{AFDBF5}{[6,7]}} \\\\  
\times \; (100\% - \text{Target's DMG Reduction\% Buffs}) \\\\
\times \; (100\% - \text{Target's \textcolor{8A9A5B}{Property Resist\%}})^\text{[6]} \\\\
\times \; (100\% + \text{Weak Point\%}) \\\\
\times \; (100\% + \text{Support Bonus\%})$

??? example "Formula Notes"
    ${\textcolor{AFDBF5}{[1]}}$: Whenever {{HP}} **HP**{.orange} is used (either own or enemy's), there is a cap of $\text{50,000}$ for the value. In other words, if you use Angelica's skill on the enemy with $\text{2,000,000}$ {{HP}} **HP**{.orange}, only $\text{50,000}$ will be put as the value.

    ${\textcolor{AFDBF5}{[2]}}$: **Energy Guard** damage (from Boo Ghost Grandhildr) counts as {{HP}} **HP**{.orange} damage, but **has no cap value**.

    ${\textcolor{AFDBF5}{[3]}}$: {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Buffs are **irrelevant** when character deals damage based on **own / enemy** {{HP}} **HP**{.orange}.

    Buffs are **relevant** if character uses **enemy** {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} to deal damage.

    ${\textcolor{AFDBF5}{[4]}}$: Applied only when character **crits**. Characters with [**Fixed Damage**](../game-mechanics/battle-system.md#different-damage-types) cannot crit, making this multiplier equal to $1$.

???+ example "Pure Math Formula"
    WIP

    $\text{Damage} = 
    \max \left[ \vec{\text{v}}
    \odot \vec{\text{SM}}
    \odot \left(1 + \left(\displaystyle \sum_{i=1}^{n} \vec{\text{b}_\text{i}} \times \left[1 - \min\left(\text{Pr},1\right) \right] \right) 
    - \left(\displaystyle \sum_{j=1}^{m}\vec{\text{d}_\text{j}}\right) \right)  \vec{\text{s}}^\text{T}
    , 1\right]$

    $\vec{\text{v}} = \begin{bmatrix}\text{\textcolor{ffe8aa}{ATK}}_\text{self} & \text{\textcolor{ffa6ff}{MATK}}_\text{self} & \text{\textcolor{orange}{HP}}_\text{self} & \text{\textcolor{white}{EG}}_\text{self} & \text{\textcolor{ffe8aa}{ATK}}_\text{enemy} & \text{\textcolor{ffa6ff}{MATK}}_\text{enemy} & \text{\textcolor{orange}{HP}}_\text{enemy} \end{bmatrix} \\
    \vec{\text{s}} = \begin{bmatrix}\delta\text{\textcolor{ffe8aa}{ATK}}_\text{self} & \delta\text{\textcolor{ffa6ff}{MATK}}_\text{self} & \delta\text{\textcolor{orange}{HP}}_\text{self} & \delta\text{\textcolor{white}{EG}}_\text{self} & \delta\text{\textcolor{ffe8aa}{ATK}}_\text{enemy} & \delta\text{\textcolor{ffa6ff}{MATK}}_\text{enemy} & \delta\text{\textcolor{orange}{HP}}_\text{enemy} \end{bmatrix} \\\\
    \vec{\text{b}_\text{i}} = \begin{bmatrix}\text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{self}} & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{self}} & \text{b}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{self}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{white}{EG}}_\text{self}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{enemy}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{enemy}} \equiv 0 & \text{b}_{\text{i}}^{\text{\textcolor{orange}{HP}}_\text{enemy}} \equiv 0 \end{bmatrix} \\
    \vec{\text{d}_\text{j}} = \begin{bmatrix}\text{d}_{\text{j}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{self}} & \text{d}_{\text{j}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{self}} & \text{d}_{\text{j}}^{\text{\textcolor{orange}{HP}}_\text{self}} \equiv 0 & \text{d}_{\text{j}}^{\text{\textcolor{white}{EG}}_\text{self}} \equiv 0 & \text{d}_{\text{j}}^{\text{\textcolor{ffe8aa}{ATK}}_\text{enemy}} \equiv 0 & \text{d}_{\text{j}}^{\text{\textcolor{ffa6ff}{MATK}}_\text{enemy}} \equiv 0 & \text{d}_{\text{j}}^{\text{\textcolor{orange}{HP}}_\text{enemy}} \equiv 0 \end{bmatrix} \\\\$



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
    \times \; ( 1 + \text{Parameter\% from Gear} \\\\
    + \; \text{Parameter\% from Potential} \\\\
    + \; \text{Parameter\% from Collection})$

    ---

=== "$\text{Skill\%}$"

    The Skill% mostly represents the percent (%) mentioned in the Skill Description. 

    ??? image "Image Showcase"
        ![Skill% Showcase](../assets/images/damage-formula/skill_desc.avif)
    
    There are some conditional $\text{Skill\%}$ values, meaning they are achievable, only when some conditions are met.

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
                ![Onsen Swordfighter Blade](../assets/images/damage-formula/illust_inven_char003303_149.avif){.icon-portrait}
                </td>
                <td><strong>Onsen Swordfighter<br>Blade</strong></td>
                <td>$[350\% \sim 600\%] + [70\% \sim 120\%] \times \text{Defuffs Applied on enemy}$</td>
            </tr>
        </tbody>
    </table>

=== "$\text{\textcolor{ffe8aa}{ATK\%} Buffs}$"

    {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} buff is the most common type of buff. It directly increases the character stat.

    These buffs are **additive**, if coming from different sources (parts of the skills or different skills): 

    $\text{\textcolor{ffe8aa}{ATK\%} Total Buff = \textcolor{ffe8aa}{ATK\%} Buff 1 + \textcolor{ffe8aa}{ATK\%} Buff 2} + \dots $

    If you apply the same buff from the same source before previous one is expired, it will **refresh** the buff duration and will **not** make two instances of the buff. 

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
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td rowspan="2" align="center">
                    ![Homunculus Lathel](../assets/images/damage-formula/illust_inven_char000103_59.avif){.icon-portrait}
                    </td>
                    <td rowspan="2"><strong>Homunculus Lathel</strong></td>
                    <td>$60\% \sim 90\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center" rowspan="2">$1 \sim 2$</td>
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
                    <td align="center">$1 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Priest of Vitality Arines](../assets/images/damage-formula/illust_inven_char103701_36.avif){.icon-portrait}
                    </td>
                    <td><strong>Priest of Vitality Arines</strong></td>
                    <td>$25\% \sim 80\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$20\% \sim 60\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Kind Student Samay](../assets/images/damage-formula/illust_inven_char101402_16.avif){.icon-portrait}
                    </td>
                    <td><strong>Kind Student Samay</strong></td>
                    <td>$20\% \sim 50\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$0 \sim 2$</td>
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
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td rowspan="2" align="center">
                    ![Queen of Gluttis Granadair](../assets/images/damage-formula/illust_inven_char067702_194.avif){.icon-portrait}
                    </td>
                    <td rowspan="2"><strong>Queen of Gluttis Granadair</strong></td>
                    <td>$50\% \sim 80\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center" rowspan="2">$1 \sim 2$</td>
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
                    <td align="center">$1 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Retired Legend Olivier](../assets/images/damage-formula/illust_inven_char003604_196.avif){.icon-portrait}
                    </td>
                    <td><strong>Retired Legend Olivier</strong></td>
                    <td>$60\% \sim 100\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$20\% \sim 60\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{AFDBF5}{[Domain]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Kind Student Samay](../assets/images/damage-formula/illust_inven_char101402_16.avif){.icon-portrait}
                    </td>
                    <td><strong>Kind Student Samay</strong></td>
                    <td>$20\% \sim 50\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$0 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Hand of Salvation Elpis](../assets/images/damage-formula/illust_inven_char003101_122.avif){.icon-portrait}
                    </td>
                    <td><strong>Hand of Salvation Elpis</strong></td>
                    <td>$25\% \sim 80\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 3$</td>
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
                    <td align="center">$2 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Lonely Survivor Lathel](../assets/images/damage-formula/illust_inven_char000102_44.avif){.icon-portrait}
                    </td>
                    <td><strong>Lonely Survivor<br>Lathel</strong></td>
                    <td>$50\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$2 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Maid Name C Rubia](../assets/images/damage-formula/illust_inven_char000806_116.avif){.icon-portrait}
                    </td>
                    <td><strong>Maid Name C<br>Rubia</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$2 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Noble Flame Ikaruga](../assets/images/damage-formula/illust_inven_char021001_198.avif){.icon-portrait}
                    </td>
                    <td><strong>Noble Flame<br>Ikaruga</strong></td>
                    <td>$60\% \sim 100\%$</td>
                    <td>$\infty \newline \text{3 stacks MAX} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Laid-back Lifeguard Nebris](../assets/images/damage-formula/illust_inven_char003302_130.avif){.icon-portrait}
                    </td>
                    <td><strong>Laid-back Lifeguard<br>Nebris</strong></td>
                    <td>$50\%$</td>
                    <td>$6 \sim 10 \text{ Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Justia](../assets/images/damage-formula/illust_inven_char000206_91.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party<br>Justia</strong></td>
                    <td>$150\% \sim 300\%$</td>
                    <td>$8 \sim 12 \text{ Turns}$</td>
                    <td align="center">$1 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Comeback Idol Ventana](../assets/images/damage-formula/illust_inven_char067003_111.avif){.icon-portrait}
                    </td>
                    <td><strong>Comeback Idol<br>Ventana</strong></td>
                    <td>$50\% \sim 125\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Whitebolt Yuri](../assets/images/damage-formula/illust_inven_char065102_105.avif){.icon-portrait}
                    </td>
                    <td><strong>Whitebolt<br>Yuri</strong></td>
                    <td>$150\% \sim 160\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Haggard Delinquent Emma](../assets/images/damage-formula/illust_inven_char101301_61.avif){.icon-portrait}
                    </td>
                    <td><strong>Haggard Delinquent<br>Emma</strong></td>
                    <td>$200\% \sim 500\%$</td>
                    <td>$6 \text{ Turns}$</td>
                    <td align="center">$1 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$25\% \sim 40\%$</td>
                    <td>$10 \text{ Turns}$</td>
                    <td align="center">$4 \sim 6$</td>
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
                    <td align="center">$4 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Beachside Justice Michaela](../assets/images/damage-formula/illust_inven_char067401_137.avif){.icon-portrait}
                    </td>
                    <td><strong>Beachside Justice<br>Michaela</strong></td>
                    <td>$200\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$4 \sim 5$</td>
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
    Pressure is a debuff that reduces stat-boosting buff efficiency. **It does not affect initial character stats, buffs only.**
    
    It affects such stats as:

    * {{HP}} **HP%**{.orange}
    * {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta}
    * {{CritRate}} **Crit Rate**
    * {{CritDMG}} **Crit Damage**
    * {{DEF}} **DEF%**{.yellow} / {{MRES}} **MRES%**{.magenta}
    * **Property Damage**

    !!! example "Example"
        Maxed **Medical Club Teresse, which would give $120\%$ {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} buff, would only apply $60\%$ instead. 

        On the countrary, her **Beachside Angel** costume will still give 200% Augmentation Buff as if it's not considered a stat-boosting buff.

=== "$\text{\textcolor{ffe8aa}{ATK\%} Debuffs}$"

    {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Debuffs are straightforward: they reduce character's {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta}. 

    Because it stacks with buffs additively, it is more or less not important unless you are in a fight where boss doesn't gain any buffs.

    This debuff is considered as Weakening, so any enemy with **Immune to Weakening** Status Effect will ignore the reduction. 

    Additionally, despite {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Debuffs, damage will always be $\ge 1$ even with 0 {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} on the enemy.

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
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Sage of Blue Clouds Olstein](../assets/images/damage-formula/illust_inven_char000604_72.avif){.icon-portrait}
                    </td>
                    <td><strong>Sage of Blue Clouds<br>Olstein</strong></td>
                    <td>$70\%$</td>
                    <td>$2 \sim 4 \text{ Turns}$</td>
                    <td align="center">$1 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Lugo Hunter Gynt](../assets/images/damage-formula/illust_inven_char100101_4.avif){.icon-portrait}
                    </td>
                    <td><strong>Lugo Hunter<br>Gynt</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![The Curse Celia](../assets/images/damage-formula/illust_inven_char101601_78.avif){.icon-portrait}
                    </td>
                    <td><strong>The Curse<br>Celia</strong></td>
                    <td>$35\% \sim 65 \%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 5$</td>
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
                    <td align="center">$1 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Descendant of the Great Witch Celia](../assets/images/damage-formula/illust_inven_char060402_28.avif){.icon-portrait}
                    </td>
                    <td><strong>Descendant of the Great Witch<br>Celia</strong></td>
                    <td>$35\% \sim 65 \%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$4 \sim 5$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{\textcolor{white}{CDMG\%}}$"

    {{CritDMG}} **Crit Damage** matters when character **crits**, meaning it is essential to have high {{CritRate}} **Crit Rate** or guarantee it via other methods.

    !!! example "{{CritRate}} Crit Rate"
        {{CritRate}} **Crit Rate** is additive, similar to other buffs within same multiplier: 

        $\text{\textcolor{white}{Crit Rate\%} Total Buff =  \textcolor{white}{Crit Rate\%} Inherent + \textcolor{white}{Crit Rate\%} Gear} + [\text{\textcolor{white}{Crit Rate\%} Buff 1} + \dots] \times [100\% - \text{Pressure\%}] $

        Here **Inherent {{CritRate}} Crit Rate** means the one from character itself. It varies from $0\%$ to $20\%$, depending on the character. Characters with $0\%$ {{CritRate}} Crit Rate **cannot crit**.

    ---

    $\text{\textcolor{white}{CDMG\%}}$ addend refers to sum of inherent, gear and bonding {{CritDMG}} **Crit Damage**:
    
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
                    <td align="center">$1 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Adventurer of the Unknown Diana](../assets/images/damage-formula/illust_inven_char002401_58.avif){.icon-portrait}
                    </td>
                    <td><strong>Adventurer of the Unknown Diana</strong></td>
                    <td>$20\% \sim 30\%$</td>
                    <td>$\text{8 Turns} \newline \text{\textcolor{AFDBF5}{[Aura]}}$</td>
                    <td align="center">$2 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![B-Rank Idol Helena](../assets/images/damage-formula/illust_inven_char061002_26.avif){.icon-portrait}
                    </td>
                    <td><strong>B-Rank Idol Helena</strong></td>
                    <td>$25\% \sim 50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$1 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Priest of Vitality Arines](../assets/images/damage-formula/illust_inven_char103701_36.avif){.icon-portrait}
                    </td>
                    <td><strong>Priest of Vitality Arines</strong></td>
                    <td>$30\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Red Riding Hood Rou](../assets/images/damage-formula/illust_inven_char000502_98.avif){.icon-portrait}
                    </td>
                    <td><strong>Red Riding Hood Rou</strong></td>
                    <td>$30\% \sim 50\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Hand of Salvation Elpis](../assets/images/damage-formula/illust_inven_char003101_122.avif){.icon-portrait}
                    </td>
                    <td><strong>Hand of Salvation Elpis</strong></td>
                    <td>$30\% \sim 35\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 3$</td>
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
                    <td align="center">$2 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Red Riding Hood Rou](../assets/images/damage-formula/illust_inven_char000502_98.avif){.icon-portrait}
                    </td>
                    <td><strong>Red Riding Hood Rou</strong></td>
                    <td>$150\% \sim 300\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 4$</td>
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
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Gray](../assets/images/damage-formula/illust_inven_char000406_93.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party Gray</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Daughter of Starwind High Elf Archer](../assets/images/damage-formula/illust_inven_char020801_162.avif){.icon-portrait}
                    </td>
                    <td><strong>Daughter of Starwind<br>High Elf Archer</strong></td>
                    <td>$100\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Stray Cat Rou](../assets/images/damage-formula/illust_inven_char000506_107.avif){.icon-portrait}
                    </td>
                    <td><strong>Stray Cat Rou</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$4 \sim 5$</td>
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
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Gentle Maid Anastasia](../assets/images/damage-formula/illust_inven_char060501_79.avif){.icon-portrait}
                    </td>
                    <td><strong>Gentle Maid Anastasia</strong></td>
                    <td>$200\% \sim 500\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$3 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Fire Graffiti Anastasia](../assets/images/damage-formula/illust_inven_char060502_46.avif){.icon-portrait}
                    </td>
                    <td><strong>Fire Graffiti Anastasia</strong></td>
                    <td>$200\% \sim 500\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Pool Party Gray](../assets/images/damage-formula/illust_inven_char000406_93.avif){.icon-portrait}
                    </td>
                    <td><strong>Pool Party Gray</strong></td>
                    <td>$50\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Labyrinth Gatekeeper Nebris](../assets/images/damage-formula/illust_inven_char003301_146.avif){.icon-portrait}
                    </td>
                    <td><strong>Labyrinth Gatekeeper Nebris</strong></td>
                    <td>$200\% \sim 300\%$</td>
                    <td>$6 \text{ Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Comeback Idol Yuri](../assets/images/damage-formula/illust_inven_char065103_110.avif){.icon-portrait}
                    </td>
                    <td><strong>Comback Idol Yuri</strong></td>
                    <td>$150\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Acting Archbishop Michaela](../assets/images/damage-formula/illust_inven_char067403_168.avif){.icon-portrait}
                    </td>
                    <td><strong>Acting Archbishop Michaela</strong></td>
                    <td>$300\% \sim 500\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$2 \sim 4$</td>
                </tr>
            </tbody>
        </table>

=== "$\text{Chains}$"
    **Chains** is a mechanic that increases the damage with each repetitive hit on the same tile / enemy.
    
    Generally speaking, each hit generates 1 chain by default, with possibility to increase amount by applying **Chain Reinforcement** status effect:

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
                    <td align="center">$2 \sim 3$</td>
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
                    <td align="center">$2 \sim 4$</td>
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
                    <td align="center">$4 \sim 5$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Masquerade Bunny Celia](../assets/images/damage-formula/illust_inven_char060403_109.avif){.icon-portrait}
                    </td>
                    <td><strong>Masquerade Bunny Celia</strong></td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$3 \sim 4$</td>
                </tr>
            </tbody>
        </table>
</div>




## Additional Effects

Death Time

Enviromental
