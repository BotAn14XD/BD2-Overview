---
comments: true
hero: assets/images/site-assets/index-pc-nav-3.avif
icon: material/calculator

---

![Damage Formula](../assets/images/site-assets/index-pc-nav-3.avif){: .card-header-img fetchpriority=high loading=eager }
#

!!! abstract "TL;DR"
    The Damage Formula consists of a few multipliers, the main of which are {{ATK}} $\text{\textcolor{ffe8aa}{ATK}}$ / {{MATK}} $\text{\textcolor{ffa6ff}{MATK}}$ and its Buffs, {{CritDMG}} $\text{\textcolor{white}{CDMG}}$ and its buffs, $\text{\textcolor{8A9A5B}{Property Damage}}$, $\text{Vulnerability}$ with $\text{DMG Increase}$ Buffs, and, lastly, $\text{Chains}$.

    Within each of these multipliers, buffs are additive, meaning if you want to reach more damage, you must **use different buff categories**. 

    Stacking a lot of {{ATK}} **ATK**{.yellow} buffs generally loses to a single {{ATK}} **ATK**{.yellow} buff combined with $\text{Vulnerability}$ and some $\text{Chains}$. Keep this in mind when constructing a team.

## Damage Formula
$\small\text{Damage} = \\\\ \text{\textcolor{ffe8aa}{ATK} [\textcolor{ffa6ff}{MATK} / \textcolor{orange}{HP}}^{\textcolor{AFDBF5}{[1]}} \text{/ \textcolor{white}{Energy Guard}}^{\textcolor{AFDBF5}{[2]}}\text{]}^{\textcolor{AFDBF5}{[3]}}  \\\\
\times \; \text{Skill\%} \\\\
\times \; (100\% + \text{\textcolor{ffe8aa}{ATK\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{\textcolor{ffe8aa}{ATK\%} Debuffs})^{\textcolor{AFDBF5}{[4]}} \\\\
\times \; (100\% + \text{\textcolor{white}{CDMG\%}} + \text{\textcolor{white}{CDMG\%} Buffs} \times [100\% - \text{Pressure\%}] - \text{\textcolor{white}{CDMG\%} Debuffs} + 6 \times (\text{\textcolor{white}{Crit Rate\%}} - 100\%)^{\textcolor{AFDBF5}{[13]}})^{\textcolor{AFDBF5}{[5]}} \\
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

    ${\textcolor{AFDBF5}{[3]}}$: The necessary attribute depends on the Costume ability. Refer to [this](#atk) section to learn more.

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

    ${\textcolor{AFDBF5}{[13]}}$: Only when {{CritRate}} **Crit Rate**{.white} is greater than 100%.

??? example "Master Formula"
    $$
    \footnotesize
    \begin{aligned}
    D_{\text{terminal}} = \max \Biggl( 1, \; \Biggl\lfloor & \bigg\lfloor \min_{\circ} \Big( \vec{C}, \; \big\lfloor \vec{v} \circ \max_{\circ} \big( \vec{0}, \; \vec{1} + \sum_j \vec{b}^{(\text{off})}_j \cdot P - \sum_j \vec{d}^{(\text{off})}_j \big) \big\rfloor \Big)^\top \vec{m} \bigg\rfloor \\
    & \cdot \min \bigg( 1, \; \max \Big( 0.1, \; 1 - \gamma_{\text{def}} \Big[ \operatorname{sgn}(v_1) \big( \text{DEF}_{\text{tgt}} + \sum_j b^{(\text{def})}_j \cdot P - \sum_j d^{(\text{def})}_j \big) \\
    & \qquad\qquad\qquad\qquad\qquad\qquad\qquad + \operatorname{sgn}(v_2) \big( \text{MRES}_{\text{tgt}} + \sum_j b^{(\text{mres})}_j \cdot P - \sum_j d^{(\text{mres})}_j \big) \Big] \Big) \bigg) \\
    & \cdot \bigg( 1 + \gamma_{\text{crit}} \max \Big( \mathcal{H}\big( \max(0, v^{(\text{cr})} + \sum_j b^{(\text{cr})}_j \cdot P - \sum_j d^{(\text{cr})}_j) - u \big), \; \gamma_{\text{raid}} \mathcal{H}\big( N^{(\text{weak})}_{\text{chain}} - 3 \big) \Big) \\
    & \qquad\quad \cdot \min \Big( 10^2, \; \max \big( 0, \; v^{(\text{cdmg})} + \sum_j b^{(\text{cdmg})}_j \cdot P - \sum_j d^{(\text{cdmg})}_j \\
    & \qquad\qquad\qquad\qquad\qquad\qquad\quad + 6 \max(0, \; v^{(\text{cr})} + \sum_j b^{(\text{cr})}_j \cdot P - \sum_j d^{(\text{cr})}_j - 1) \big) \Big) \bigg) \\
    & \cdot \max \bigg( 0, \; 1 + \max(0, \mathbf{e}_{\text{src}}^\top \mathbf{A}_{\text{elem}} \mathbf{e}_{\text{tgt}}) \Big( v_{\text{pr}}^{(\text{off})} + \sum_j b_j^{(\text{pr\_off})} \cdot P - \sum_j d_j^{(\text{pr\_off})} + \gamma_{\text{ec}} b^{(\text{pr\_ec})} \Big) \\
    & \qquad\qquad\quad - \max(0, -\mathbf{e}_{\text{src}}^\top \mathbf{A}_{\text{elem}} \mathbf{e}_{\text{tgt}}) \Big( v_{\text{pr}}^{(\text{def})} + \sum_j b_j^{(\text{pr\_def})} \cdot P - \sum_j d_j^{(\text{pr\_def})} \Big) \bigg) \\
    & \cdot \bigg( 1 + \gamma_{\text{chain}} \big( 0.10 + \sum_j b_j^{(\text{chain})} \big) \Big[ (1 - \gamma_{\text{ln}})\min(100, N_{\text{chain}}) + \gamma_{\text{ln}} N_{\text{chain}} \Big] \bigg) \\
    & \cdot \bigg( 1 + \sum_j b_j^{(\text{aug})} + \gamma_{\text{vuln}} \Big[ \sum_j b_j^{(\text{vuln\_gen})} + \operatorname{sgn}(v_1)\sum_j b_j^{(\text{vuln\_phys})} + \operatorname{sgn}(v_2)\sum_j b_j^{(\text{vuln\_mag})} \\
    & \qquad\qquad\qquad\qquad\qquad\quad + \big( \sum_j \vec{\mathbf{b}}_j^{(\text{vuln\_elem})} \big)^\top \mathbf{e}_{\text{src}} + \gamma_{\text{dot}} \sum_j b_j^{(\text{vuln\_dot})} + \gamma_{\text{sum}} \sum_j b_j^{(\text{vuln\_sum})} \Big] \bigg) \\
    & \cdot \prod_k \bigg( 1 - \gamma_{\text{barrier}} \Big[ r_k^{(\text{gen})} + \operatorname{sgn}(v_1) r_k^{(\text{phys})} + \operatorname{sgn}(v_2) r_k^{(\text{mag})} \Big] \bigg) \\
    & \cdot \Big( 1 + \gamma_{\text{raid}} \gamma_{\text{weak}} b_{\text{weak}} \Big) \Big( 1 + \gamma_{\text{ln}} b_{\text{supp}} \Big) \Biggr\rfloor \Biggr)
    \end{aligned}
    $$ 

    {{ redirect_btn('https://github.com/BotAn14XD/BD2-Overview/blob/main/docs/assets/publishings/damage-formula/damage-formula.pdf', 'Formula Breakdown & Testing', '#4caf50') }}
## Damage Formula Details {.tab-align}

=== "<span class="yellow">ATK</span>"
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

=== "Skill%"
    The Skill% mostly represents the percent (%) mentioned in the Skill Description. 

    ??? image "Image Showcase"
        ![Skill% Showcase](../assets/images/damage-formula/skill_desc.avif)
    
    There are some conditional $\text{Skill\%}$ values, meaning they are achievable only when some conditions are met.
    <div class="responsive-table-wrapper">
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
                <td>$\textcolor{white}{775\% \sim 1900\% \text{ to the Main Target}} \newline 500\% \sim 1700\% \text{ otherwise}$</td>
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
                <td>$\textcolor{white}{200\% \sim 420\% \text{ to the Main Target}} \newline 100\% \sim 240\% \text{ otherwise}$</td>
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
                <td>$[40\% \sim 110\%] + [15\% \sim 46\%] \times \text{Buffs Applied}$</td>
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
                <td>$[150\% \sim 300\%] + [80\% \sim 310\%] \times \text{Targets affected}$</td>
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
                <td>$\textcolor{white}{40\% \sim 260\% \newline \text{if enemy Chain count is a multiple of 3}} \newline 30\% \sim 80\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Onsen Swordfighter Blade](../assets/images/damage-formula/illust_inven_char003702_158.avif){.icon-portrait}
                </td>
                <td><strong>Onsen Swordfighter<br>Blade</strong></td>
                <td>$[350\% \sim 600\%] + [70\% \sim 120\%] \times \text{Debuffs Applied on enemy}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Tricky Lover Dalvi](../assets/images/damage-formula/illust_inven_char061306_208.avif){.icon-portrait}
                </td>
                <td><strong>Tricky Lover<br>Dalvi</strong></td>
                <td>$\textcolor{white}{[100\% \sim 300\%] \times \text{Bleed Stacks Applied} \newline \text{if enemy has Bleed Applied}} \newline 100\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Miracle Violet Palette](../assets/images/damage-formula/illust_inven_char004202_200.avif){.icon-portrait}
                </td>
                <td><strong>Miracle Violet<br>Palette</strong></td>
                <td>$\textcolor{white}{110\% \sim 250\% \newline \text{if enemy Debuff count is 7 or more}} \newline 35\% \sim 65\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Gentle Maid Anastasia](../assets/images/damage-formula/illust_inven_char060501_79.avif){.icon-portrait}
                </td>
                <td><strong>Gentle Maid Anastasia</strong></td>
                <td>$\textcolor{white}{250\% \sim 500\% \text{ to the Main Target}} \newline 110\% \sim 210\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Fire Graffiti Anastasia](../assets/images/damage-formula/illust_inven_char060502_46.avif){.icon-portrait}
                </td>
                <td><strong>Fire Graffiti Anastasia</strong></td>
                <td>$\textcolor{white}{55\% \sim 90\% \text{ to the Main Target}} \newline 30\% \sim 50\% \text{ otherwise}$</td>
            </tr>
            <tr>
                <td align="center">
                ![Pool Party Scheherazade](../assets/images/damage-formula/illust_inven_char000306_92.avif){.icon-portrait}
                </td>
                <td><strong>Pool Party Scheherazade</strong></td>
                <td>$\textcolor{white}{140\% \sim 260\% \text{ if Chain Count on the enemy is 15 or more}} \newline 30\% \sim 60\% \text{ otherwise}$</td>
            </tr>
        </tbody>
    </table>
    </div>

    ---

=== "<span class="yellow">ATK%</span> Buffs"
    The {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} buff is the most common type of buff. It directly increases the character's stat.

    These buffs are **additive** if coming from different sources (parts of the skills or different skills): 

    $\text{\textcolor{ffe8aa}{ATK\%} Total Buff = \textcolor{ffe8aa}{ATK\%} Buff 1 + \textcolor{ffe8aa}{ATK\%} Buff 2} + \dots $

    If you apply the same buff from the same source before the previous one has expired, it will **refresh** the buff duration and will **not** make two instances of the buff. 

    ---

    Costumes providing {{ATK}} $\text{\textcolor{ffe8aa}{ATK\%}}$ buffs **to allies**:
    <div class="responsive-table-wrapper">
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
                <td>$60\% \sim 130\%$</td>
                <td>$4 \sim 6 \text{ Turns}$</td>
                <td align="center" rowspan="2">$6 \sim 1$</td>
            </tr>
            <tr>
                <td>$25\% \sim 150\%$</td>
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
    </div>
    
    ---
    
    Costumes providing {{MATK}} $\text{\textcolor{ffa6ff}{MATK\%}}$ buffs **to allies**:
    <div class="responsive-table-wrapper">
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
                <td>$35\% \sim 190\%$</td>
                <td>$\text{4 Turns}$</td>
                <td align="center">$6 \sim 1$</td>
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
    </div>

    ---

    Costumes providing {{ATK}} $\text{\textcolor{ffe8aa}{ATK\%}}$ buffs to **themselves only**:
    <div class="responsive-table-wrapper">
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
                <td>$150\% \sim 400\%$</td>
                <td>$8 \sim 12 \text{ Turns}$</td>
                <td align="center">$5 \sim 1$</td>
            </tr>
            <tr>
                <td align="center">
                ![Comeback Idol Ventana](../assets/images/damage-formula/illust_inven_char067003_111.avif){.icon-portrait}
                </td>
                <td><strong>Comeback Idol<br>Ventana</strong></td>
                <td>$50\% \sim 125\%$</td>
                <td>$6 \text{ Turns}$</td>
                <td align="center">$5 \sim 3$</td>
            </tr>
            <tr>
                <td align="center">
                ![Whitebolt Yuri](../assets/images/damage-formula/illust_inven_char065102_105.avif){.icon-portrait}
                </td>
                <td><strong>Whitebolt<br>Yuri</strong></td>
                <td>$150\% \sim 160\%$</td>
                <td>$6 \text{ Turns}$</td>
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
            <tr>
                <td align="center">
                ![Savage Warrior Aquila](../assets/images/damage-formula/illust_inven_char067901_222.avif){.icon-portrait}
                </td>
                <td><strong>Savage Warrior Aquila</strong></td>
                <td>$15\% \sim 30\%$</td>
                <td>$4 \text{ Turns}\newline \text{99 stacks MAX} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                <td align="center">$5 \sim 4$</td>
            </tr>
            <tr>
                <td align="center">
                ![Ocean Vanguard Luvencia](../assets/images/damage-formula/illust_inven_char067504_205.avif){.icon-portrait}
                </td>
                <td><strong>Ocean Vanguard Luvencia</strong></td>
                <td>$1\% \sim 3\%$</td>
                <td>$6 \text{ Turns}\newline \text{60 stacks MAX} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                <td align="center">$6 \sim 5$</td>
            </tr>
            <tr>
                <td align="center">
                ![Dream Bride Eclipse](../assets/images/damage-formula/illust_inven_char000708_170.avif){.icon-portrait}
                </td>
                <td><strong>Dream Bride Eclipse</strong></td>
                <td>$50\% ~ 100\%$</td>
                <td>$6 \text{ Turns}$</td>
                <td align="center">$5 \sim 4$</td>
            </tr>
            <tr>
                <td align="center">
                ![DJ Venaka](../assets/images/damage-formula/illust_inven_char067201_129.avif){.icon-portrait}
                </td>
                <td><strong>DJ<br>Venaka</strong></td>
                <td>$100\%$</td>
                <td>$4\text{ Turns}$</td>
                <td align="center">$6 \sim 5$</td>
            </tr>
        </tbody>
    </table>
    </div>

    ---
        
    Costumes providing {{MATK}} $\text{\textcolor{ffa6ff}{MATK\%}}$ buffs to **themselves only**:
    <div class="responsive-table-wrapper">
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
                <td>$60\% \sim 100\%$</td>
                <td>$4 \text{ Turns}$</td>
                <td align="center">$5 \sim 4$</td>
            </tr>
            <tr>
                <td align="center">
                ![Beachside Justice Michaela](../assets/images/damage-formula/illust_inven_char067401_137.avif){.icon-portrait}
                </td>
                <td><strong>Beachside Justice<br>Michaela</strong></td>
                <td>$200\% \sim 300\%$</td>
                <td>$2 \sim 4 \text{ Turns}$</td>
                <td align="center">$8 \sim 4$</td>
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
    </div>

=== "Pressure"
    Pressure is a debuff that reduces stat-boosting buff efficiency. **It does not affect initial character stats, only buffs.**

    It affects stats such as:

    * {{HP}} **HP%**{.orange}
    * {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta}
    * {{CritRate}} **Crit Rate**
    * {{CritDMG}} **Crit Damage**
    * {{DEF}} **DEF%**{.yellow} / {{MRES}} **MRES%**{.magenta}
    * **Property Damage**

    !!! example "Example"
        A maxed **Medical Club Teresse**, which would give $120\%$ {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} buff, would only apply $60\%$ instead. 

        On the contrary, her **Beachside Angel** costume will still give a 200% Augmentation Buff as if it's not considered a stat-boosting buff.

    ??? image "Pressure Effect in a fight"
        ![Pressure Effect in a fight](../assets/images/damage-formula/pressure.avif)

=== "<span class="yellow">ATK%</span> Debuffs"
    {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Debuffs are straightforward: they reduce the character's {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta}. 

    Because they stack with buffs additively, it is more or less not important unless you are in a fight where the boss doesn't gain any buffs.

    This debuff is considered Weakening, so any enemy with the **Immune to Weakening** Status Effect will ignore the reduction. 

    Additionally, despite {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Debuffs, damage will always be $\ge 1$ even with 0 {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} on the enemy.

    ---
    As mentioned above, these debuffs are not very widely used, especially since a lot of bosses have Weakening immunity or you can sustain just fine, while in PvP there are buffs pretty much nullifying your debuffs. 

    However, it is worth mentioning that there are Story Pack fights such as **Partan** (Story Pack 11) and **Nox** (Story Pack 12), where you can use **Gynt** and **Remnunt** to extend the fight to Death Time, where you will deal increased damage to the boss.

    ---
        
    Costumes providing {{ATK}} $\text{\textcolor{ffe8aa}{ATK\%}}$ debuffs:
    <div class="responsive-table-wrapper">
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
    </div>
    
    ---
        
    Costumes providing {{MATK}} $\text{\textcolor{ffa6ff}{MATK\%}}$ debuffs:
    <div class="responsive-table-wrapper">
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
    </div>

=== "<span class="white">CDMG</span>"
    {{CritDMG}} **Crit Damage** matters when a character **crits**, meaning it is essential to have a high {{CritRate}} **Crit Rate** or guarantee it via other methods.

    !!! example "{{CritRate}} Crit Rate"
        {{CritRate}} **Crit Rate** is additive, similar to other buffs within the same multiplier: 

        $\text{\textcolor{white}{Crit Rate\%} Total Buff =  \textcolor{white}{Crit Rate\%} Inherent + \textcolor{white}{Crit Rate\%} Gear} + [\text{\textcolor{white}{Crit Rate\%} Buff 1} + \dots] \times [100\% - \text{Pressure\%}] $

        Here **Inherent {{CritRate}} Crit Rate** means the one from the character itself. It varies from $0\%$ to $20\%$, depending on the character. Characters with $0\%$ {{CritRate}} Crit Rate **cannot crit**.

    ---

    $\text{\textcolor{white}{CDMG\%}}$ addend refers to the sum of inherent, gear, and bonding {{CritDMG}} **Crit Damage**:
    
    $\text{\textcolor{white}{CDMG\%}} = \text{Character's Base \textcolor{white}{CDMG\%}} + \text{Gear \textcolor{white}{CDMG\%}} + \text{ Potential \textcolor{white}{CDMG\%}}$

    !!! example "Overflow {{CritRate}} **Crit Rate** Conversion"
        When {{CritRate}} **Crit Rate**{.white} exceeds 100%, extra **Crit Rate**{.white} is converted to {{CritDMG}} **Crit Damage**{.white} at a ratio of 1:6.

        Converted {{CritDMG}} **Crit Damage**{.white} this way **is not affected by Pressure** and is enviromental rule rather than direct buff.

    ---

    Costumes providing {{CritRate}} $\text{\textcolor{white}{Crit Rate\%}}$ buffs **to allies**:
    <div class="responsive-table-wrapper">
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
    </div>

    ---

    Costumes providing {{CritDMG}} $\text{\textcolor{white}{Crit DMG\%}}$ buffs **to allies**:
    <div class="responsive-table-wrapper">
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
    </div>

    ---

    Costumes providing {{CritRate}} $\text{\textcolor{white}{Crit Rate\%}}$ buffs to **themselves only**:
    <div class="responsive-table-wrapper">
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
    </div>

    ---

    Costumes providing {{CritDMG}} $\text{\textcolor{white}{Crit DMG\%}}$ buffs to **themselves only**:
    <div class="responsive-table-wrapper">
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
                    <td>$350\% \sim 600\%$</td>
                    <td>$\text{1 Turn}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Fire Graffiti Anastasia](../assets/images/damage-formula/illust_inven_char060502_46.avif){.icon-portrait}
                    </td>
                    <td><strong>Fire Graffiti Anastasia</strong></td>
                    <td>$350\% \sim 600\%$</td>
                    <td>$1 \sim 3 \text{ Turns}$</td>
                    <td align="center">$7 \sim 6$</td>
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
                    <td>$150\% \sim 300\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$8 \sim 3$</td>
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
                <tr>
                    <td align="center">
                    ![Combat Medic Granhildr](../assets/images/damage-formula/illust_inven_char067104_206.avif){.icon-portrait}
                    </td>
                    <td><strong>Combat Medic Granhildr</strong></td>
                    <td>$100\% \sim 200\%$</td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Bikini Agent Sylvia](../assets/images/damage-formula/illust_inven_char001006_177.avif){.icon-portrait}
                    </td>
                    <td><strong>Bikini Agent Sylvia</strong></td>
                    <td>$200\%$</td>
                    <td>$2 \text{ Turns} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$9 \sim 8$</td>
                </tr>
            </tbody>
        </table>
    </div>

=== "Chains"
    The **Chain** system is a mechanic that increases damage with each repetitive hit on the same tile/enemy.
    
    Generally speaking, each hit generates 1 chain by default, with the possibility to increase the amount by applying the **Chain Reinforcement** status effect:

    $\text{Chain Per Hit} = 1 + \text{Amount of Applied Chain Reinforcements}$

    ---

    Each **Chain** increases damage by 10% by default; however, there is an effect called **Increased Chain DMG**, which increases that value further.

    ---

    **Chain Retention** is an effect that keeps set amount of Chains in-between Turns. If you reach more Chains than Retention can carry over, the maximum amount from Chain Retention will be carried over instead. 

    ---


    **Chain Weakening** is similar to **Chain Reinforcement**, but is applied to the Enemy instead.

    ---

    Costumes providing **Chain Reinforcement** buff **to allies**:
    <div class="responsive-table-wrapper">
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
    </div>

    ---

    Costumes providing $\text{Increased Chain DMG\%}$:
    <div class="responsive-table-wrapper">
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
            <tr>
                <td align="center">
                ![Ocean Vanguard Luvencia](../assets/images/damage-formula/illust_inven_char067504_205.avif){.icon-portrait}
                </td>
                <td><strong>Ocean Vanguard Luvencia</strong></td>
                <td>$6\% \sim 20\%$</td>
                <td>$2 \text{ Turns}\newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                <td align="center">$5 \sim 9$</td>
            </tr>
            <tr>
                <td align="center">
                ![Deadeye Nekyndalia](../assets/images/damage-formula/illust_inven_char004301_214.avif){.icon-portrait}
                </td>
                <td><strong>Deadeye Nekyndalia</strong></td>
                <td>$3\%$</td>
                <td>$4 \text{ Turns}$</td>
                <td align="center">$4 \sim 5$</td>
            </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing **Chain Reinforcement** buff to **themselves only**:
    <div class="responsive-table-wrapper">
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
                <tr>
                    <td align="center">
                    ![Heavenly Guardian Successor Glacia](../assets/images/damage-formula/illust_inven_char066907_209.avif){.icon-portrait}
                    </td>
                    <td><strong>Heavenly Guardian Successor Glacia</strong></td>
                    <td>$2 \text{ Turns}$</td>
                    <td align="center">$8 \sim 7$</td>
                </tr>
                <tr>
                <td align="center">
                ![Pool Party Scheherazade](../assets/images/damage-formula/illust_inven_char000306_92.avif){.icon-portrait}
                </td>
                <td><strong>Pool Party Scheherazade</strong></td>
                <td>$6 \text{ Turns}$</td>
                <td align="center">$7 \sim 6$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing **Chain Retention** debuff to enemy:
    <div class="responsive-table-wrapper">
        <table class="data-table">
            <thead>
                <tr>
                    <th colspan="2">Costume</th>
                    <th>Chains Retained</th>
                    <th>Duration</th>
                    <th>SP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">
                    ![Heavenly Guardian Successor Glacia](../assets/images/damage-formula/illust_inven_char066907_209.avif){.icon-portrait}
                    </td>
                    <td><strong>Heavenly Guardian<br>Successor Glacia</strong></td>
                    <td>$6 \sim 20$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing **Chain Weakening** debuff **to enemies**:
    <div class="responsive-table-wrapper">
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
                    ![Steel Engine Rafina](../assets/images/damage-formula/illust_inven_char060701_81.avif){.icon-portrait}
                    </td>
                    <td><strong>Steel Engine Rafina</strong></td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$7 \sim 6$</td>
                </tr>
            </tbody>
        </table>
    </div>

=== "Vulnerability"
    Vulnerability is a **debuff** that increases damage received by the enemy. There are 5 types of Vulnerability: 

    * **General**, which increases damage in every instance
    * **Damage Type-related**, which increases damage only for the {{Physical}} **Physical**{.yellow} or {{Magical}} **Magical**{.magenta} damage type. 
        * {{Physical}} **Physical**{.yellow} Vulnerability is described as **Vulnerability (Physical)**
        * {{Magical}} **Magical**{.magenta} Vulnerability is described as **Vulnerability (Magic)**
    * **Property-related**, that increases damage only if a specific property deals damage
    * **Summons-related**, that increases damage dealt by summons

    ---

    Similar to any other buff from the same multiplier, different Vulnerabilities stack additively:

    $\text{Total Vulnerability} = \text{Vulnerability 1} + \text{Vulnerability 2} + \dots$

    ---

    Costumes providing **General Vulnerability**:
    <div class="responsive-table-wrapper">
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
                <tr>
                    <td align="center">
                    ![Miracle Marine Mamonir](../assets/images/damage-formula/illust_inven_char067803_199.avif){.icon-portrait}
                    </td>
                    <td><strong>Miracle Marine<br>Mamonir</strong></td>
                    <td>$30\% \sim 80\%$</td>
                    <td>$2 \sim 6 \text{ Turns}\newline \text{\textcolor{AFDBF5}{[Max 8 Stacks]}} \newline \text{\textcolor{AFDBF5}{[Conditional]}}$</td>
                    <td align="center">$6 \sim 5$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing {{Physical}} **Physical**{.yellow} **Vulnerability**:
    <div class="responsive-table-wrapper">
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
                    <td>$100\% \sim 150\% \newline \text{\textcolor{AFDBF5}{[Main Target]}} \newline 75\% \newline \text{\textcolor{AFDBF5}{[All Targets]}}$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$6 \sim 4$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing {{Magical}} **Magical**{.magenta} **Vulnerability**:
    <div class="responsive-table-wrapper">
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
                <tr>
                    <td align="center">
                    ![Night of Jealousy Levia](../assets/images/damage-formula/illust_inven_char067302_139.avif){.icon-portrait}
                    </td>
                    <td><strong>Night of Jealousy<br>Levia</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing **DoT Vulnerability**:
    <div class="responsive-table-wrapper">
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
    </div>

    ---

    Costumes providing **Summons Vulnerability**:
    <div class="responsive-table-wrapper">
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
    </div>

    ---

    Costumes providing **Property Vulnerability**:
    <div class="responsive-table-wrapper">
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
    </div>

=== "DMG Increase%"
    $\text{DMG Increase\%}$ Buffs are buffs that technically act as a reverse [**Vulnerability**](#vulnerability), increasing **your own characters'** damage instead of forcing the enemy to take more damage.

    So far, all these buffs are called **Augmentation**, which you can think of as a buff with conditions. The condition can be either related to chains, the number of times getting hit, or the number of debuffs being removed from allies. 

    In other words, it is similar to Conditional [$\text{Skill\%}$](#skill) in a way.

    ---

    As always, this type of buff from different sources is additive:

    $ \text{Total DMG Increase\%} = \text{DMG Increase\% 1} + \text{DMG Increase\% 2} + \dots$

    ---

    However, since these buffs belong to the same bracket as **Vulnerability**, note that high Vulnerability will decrease the efficiency of these buffs. 

    ---

    Costumes providing $\text{DMG Increase\%}$ Buffs **to allies**:
    <div class="responsive-table-wrapper">
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
                    <td>$80\% \sim 175\% \newline \text{\textcolor{AFDBF5}{[When attacking enemy}} \newline \text{\textcolor{AFDBF5}{with 10 Chains or more]}}$</td>
                    <td>$6 \sim 4 \text{ Turns}$</td>
                    <td align="center">$6 \sim 2$</td>
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
                <tr>
                    <td align="center">
                    ![Sunny Inn Hand Helena](../assets/images/damage-formula/illust_inven_char061003_210.avif){.icon-portrait}
                    </td>
                    <td><strong>Sunny Inn<br>Hand Helena</strong></td>
                    <td>$75\% \sim 280\%$</td>
                    <td>$6 \sim 8 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes providing $\text{DMG Increase\%}$ Buffs to **themselves only**:
    <div class="responsive-table-wrapper">
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
                <tr>
                    <td align="center">
                    ![Naive Lady Elise](../assets/images/damage-formula/illust_inven_char060804_207.avif){.icon-portrait}
                    </td>
                    <td><strong>Naive Lady<br>Elise</strong></td>
                    <td>$70\% \sim 150\% \newline + \; [4\% \sim 10\%] \newline \times \; \text{\textcolor{AFDBF5}{Resonate Stacks}}$</td>
                    <td>$6 \text{ Turns}$</td>
                    <td align="center">$5 \sim 3$</td>
                </tr>
            </tbody>
        </table>
    </div>

=== "Property"
    Property is another aspect of any character. There are a total of 6 Properties: ![Water](../assets/images/battle-system/icons/elementicon1_1.avif){.icon} Water, ![Fire](../assets/images/battle-system/icons/elementicon2_2.avif){.icon} Fire, ![Wind](../assets/images/battle-system/icons/elementicon3_3.avif){.icon} Wind, ![Light](../assets/images/battle-system/icons/elementicon4_4.avif){.icon} Light, ![Darkness](../assets/images/battle-system/icons/elementicon5_5.avif){.icon} Darkness and ![Neutral](../assets/images/battle-system/icons/elementicon6_6.avif){.icon} Neutral.

    Depending on the opponent, there can be 3 outcomes: 

    * You gain **Property Advantage**, dealing **extra damage** due to a superior Property
    * You deal neither more nor less damage, due to a Neutral enemy or cases like Light -> Water. 
    * You deal **less damage** due to **Property Disadvantage**.

    ---

    Similar to any other buff, $\text{Property Damage\% Buffs}$ stack additively: 
    $\text{\textcolor{8A9A5B}{Property Damage\%} Total Buffs} = \text{\textcolor{8A9A5B}{Property Damage\%} Buff 1} + \text{\textcolor{8A9A5B}{Property Damage\%} Buff 2} + \dots$

    ---

    $\text{\textcolor{8A9A5B}{Property Damage\%}}$ in the formula refers to the **character's own** Property Damage. Usually it consists of the initial, awakening, and [bond](../progression/potentials.md) ones:

    $\text{\textcolor{8A9A5B}{Property Damage\%}} = 50\% + \text{\textcolor{8A9A5B}{Property Damage\%} from Awakening} + \text{\textcolor{8A9A5B}{Property Damage\%} from Bond}$

    ---

    Costumes providing $\text{Property Damage\%}$ buffs **to allies**:
    <div class="responsive-table-wrapper">
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
                    <td>$100\% \sim 295\%$</td>
                    <td>$\text{8 Turns} \newline \text{\textcolor{AFDBF5}{[Aura]}}$</td>
                    <td align="center">$6 \sim 2$</td>
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
    </div>

    ---

    Costumes providing $\text{Property Damage\%}$ buffs to **themselves only**:
    <div class="responsive-table-wrapper">
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
                    <td>$30\% \sim 90\%$</td>
                    <td>$4 \sim 6 \text{ Turns}$</td>
                    <td align="center">$8 \sim 3$</td>
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
                <tr>
                    <td align="center">
                    ![The Fallen Angelica](../assets/images/damage-formula/illust_inven_char066401_94.avif){.icon-portrait}
                    </td>
                    <td><strong>The Fallen<br>Angelica</strong></td>
                    <td>$100\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$5 \sim 4$</td>
                </tr>
            </tbody>
        </table>
    </div>

=== "<span class="yellow">DEF</span>"
    {{DEF}} $\text{\textcolor{ffe8aa}{DEF}}$ / {{MRES}} $\text{\textcolor{ffa6ff}{MRES}}$ are two main stats of a character. They reduce damage from the enemy. 

    * $\text{\textcolor{ffe8aa}{DEF}}$ decreases all incoming {{Physical}} **Physical**{.yellow} Damage.
    * $\text{\textcolor{ffa6ff}{MRES}}$ decreases all incoming {{Magical}} **Magical**{.magenta} Damage.

    ---

    During calculations, $\text{\textcolor{ffe8aa}{DEF}}$ / $\text{\textcolor{ffa6ff}{MRES}}$ are capped at $90\%$. That means no matter how high the stat is, only a maximum of $90\%$ will be used. This, however, does not actually remove anything above that mark, meaning going above it can be useful when facing $\text{\textcolor{ffe8aa}{DEF}}$ / $\text{\textcolor{ffa6ff}{MRES}}$ **Reduction**.

    ---

    **Fixed**, **Consumed** and **Pure** Damage ignore $\text{\textcolor{ffe8aa}{DEF}}$ / $\text{\textcolor{ffa6ff}{MRES}}$ completely.

    ---
    
    Costumes providing {{DEF}} $\text{\textcolor{ffe8aa}{DEF\%}}$ reduction:
    <div class="responsive-table-wrapper">
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
    </div>

    ---
    
    Costumes providing {{MRES}} $\text{\textcolor{ffa6ff}{MRES\%}}$ reduction:
    <div class="responsive-table-wrapper">
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
                <tr>
                    <td align="center">
                    ![Miracle Violet Palette](../assets/images/damage-formula/illust_inven_char004202_200.avif){.icon-portrait}
                    </td>
                    <td><strong>Miracle Violet<br>Palette</strong></td>
                    <td>$50\%$</td>
                    <td>$4 \text{ Turns}$</td>
                    <td align="center">$7 \sim 6$</td>
                </tr>
            </tbody>
        </table>
    </div>

    ---

    Costumes decreasing **own** {{DEF}} $\text{\textcolor{ffe8aa}{DEF}}$ / {{MRES}} $\text{\textcolor{ffa6ff}{MRES}}$:
    <div class="responsive-table-wrapper">
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
    </div>

=== "DMG Reduction"
    $\text{DMG Reduction}$ is a separate buff that decreases incoming damage, similar to {{DEF}} $\text{\textcolor{ffe8aa}{DEF}}$ and {{MRES}} $\text{\textcolor{ffa6ff}{MRES}}$, but working differently.

    It's more commonly known as a **Barrier** buff, being part of the skillset for multiple costumes in the game.

    ---

    Barriers from different sources stack differently compared to other buffs.
    Instead of being additive, they are multiplicative:

    $(100\% - \text{Target's DMG Reduction\% Buffs Total}) = \\\\
    = (100\% - \text{Target's DMG Reduction\% Buff 1}) \times \\\\
    \times \; (100\% - \text{Target's DMG Reduction\% Buff 2}) \times \dots$

    For example, combining 2 Barriers of $70\%$ and $50\%$ will essentially give you an $85\%$ Barrier.

    This system ensures that a barrier can never achieve $100\%$, meaning some damage will go through anyway. 

    ---

    Similar to **Vulnerability**, Barriers *can* be {{Physical}} **Physical**{.yellow} or {{Magical}} **Magical**{.magenta}, meaning they will reduce incoming damage from only one damage type. 

    ---

    Costumes providing **Barrier** buff **to allies**:
    <div class="responsive-table-wrapper">
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
    </div>
    
    ---

    Costumes providing **Barrier** buff to **themselves only**:
    <div class="responsive-table-wrapper">
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
                <tr>
                    <td align="center">
                    ![Miracle Marine Mamonir](../assets/images/damage-formula/illust_inven_char067803_199.avif){.icon-portrait}
                    </td>
                    <td><strong>Miracle Marine<br>Mamonir</strong></td>
                    <td>$50\% \sim 70\%$</td>
                    <td>$6 \text{ Turns}$</td>
                    <td align="center">$3 \sim 2$</td>
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
    * {{ATK}} **ATK**: $3133$
    * {{CritRate}} **Crit Rate**: $60\%$
    * {{CritDMG}} **Crit DMG**: $680.44\%$
    * **Darkness DMG**: $60\%$

!!! abstract "Enemy Stats"
    * {{DEF}} **DEF**: $25\%$

Liberta increases {{ATK}} **ATK** by $115\%$ and {{CritRate}} **Crit Rate** by $50\%$, Lathel increases {{ATK}} **ATK** by $240\%$, and Teresse increases **DMG Dealt** by $200\%$.

Putting that into the equation:

$\text{Damage} = \left\lfloor \left\lfloor \underbrace{3133}_\text{ATK} \times \underbrace{(100\% + \overbrace{115\%}^\text{Liberta} + \overbrace{240\%}^\text{Lathel})}_\text{ATK Buffs}\right\rfloor \times \underbrace{150\%}_\text{Skill Multiplier} \right\rfloor \times \underbrace{(100\% - 25\%)}_\text{Enemy DEF} \times \underbrace{(100\% + \overbrace{200\%}^\text{Teresse})}_\text{DMG Increase} \times \underbrace{(100\% + 680.44\% + \overbrace{6 \cdot 10\%}^\text{CRate Overflow})}_\text{Crit DMG} \times \underbrace{(100\% + 60\%)}_\text{Property}$

$\text{Damage} = \lfloor \lfloor 3133 \times 4.55 \rfloor \times 1.5 \rfloor \times \underbrace{0.75 \times 3 \times 8.344 \times 1.6}_{30.25584} = \\
= \lfloor 14255 \times 1.5 \rfloor \times 30.25584 = 21382 \times 30.25584 = 646930.37$

That confirms the damage received by the enemy in-game:

![Fight Screenshot №2](../assets/images/damage-formula/fight_2.avif)

The difference of 1 can be explained with calculations precision.

## Stat Limits
During calculations, some numbers have a cap to avoid weird bugs or mechanics.

* {{ATK}} **ATK**{.yellow} and {{MATK}} **MATK**{.magenta} are capped at $100,000$.
* {{HP}} **HP**{.orange} is capped at $50,000$.
* {{CritRate}} **Crit Rate**{.white} is capped at $100\%$.
* {{CritDMG}} **Crit DMG**{.white} is capped at $10,000$

* Chains are capped at $100$, except in Last Night, where they have no cap.

## Additional Effects

### Death Time
Starting from Turn 11 in different modes, Death Time is introduced. 

Every 2 turns, each side receives

* $100\%$ {{ATK}} **ATK**{.yellow} / {{MATK}} **MATK**{.magenta} **Buff**
* $100\%$ {{DEF}} **DEF**{.yellow} / {{MRES}} **MRES**{.magenta} **Debuffs**
* $50\%$ Damage Increase **Buff**

These (de)buffs follow the exact rules as described above, going into each of the brackets seamlessly.

### Environmental Effects
In [**Evil Castle**](../content-packs/evil-castle.md), especially **Tower of Jealousy** and **Tower of Wrath**, there are effects taking place that affect some stats, such as  **Pressure**, {{CritRate}} **Crit Rate**, and more.

Refer to the [**Evil Castle**](../content-packs/evil-castle.md) page for a more detailed explanation.