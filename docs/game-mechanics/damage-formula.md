# Damage Formula — Brown Dust II

!!! abstract "Tl;dr"
    WIP

Damage Formula
$\text{Damage} = \\\\ \text{\textcolor{ffe8aa}{ATK}}^{\color{yellow}[1][2]} \\\\
\times \; \text{Skill\%} \\\\
\times \; (100\% + \text{\textcolor{ffe8aa}{ATK\%} Buffs} - \text{\textcolor{ffe8aa}{ATK\%} Debuffs})^{\color{yellow}[3]} \\\\
\times \; (100\% + \text{\textcolor{white}{CDMG\%}} + \text{\textcolor{white}{CDMG\%} Buffs} - \text{\textcolor{white}{CDMG\%} Debuffs}) \\
\times \; (100\% + (10\% + \text{Increase Chain DMG\%}) \times \text{Chains}) \\\\
\times \; (100\% + \text{Target's Vulnerability Debuffs\%} + \text{DMG Increase\% Buffs}) \\\\
\times \; (100\% + \text{\textcolor{lime}{Property Damage\%}} + \text{Season Buff\%} + \text{\textcolor{lime}{Property Damage\%} Buffs})^\text{[3]} \\\\
\times \; (100\% - (\text{Target's \textcolor{ffe8aa}{DEF\%}} + \text{Target's \textcolor{ffe8aa}{DEF\%} Buffs} - \text{Target's \textcolor{ffe8aa}{DEF\%} Debuffs}))^\text{[4,5]} \\\\  
\times \; (100\% - \text{Target's DMG Reduction\% Buffs}) \\\\
\times \; (100\% - \text{Target's \textcolor{lime}{Property Resist\%}})^\text{[6]} \\\\
\times \; (100\% + \text{Weak Point\%}) \\\\
\times \; (100\% + \text{Support Bonus\%})$

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

    ${\color{yellow}[1]}$: Whenever {{HP}} **HP**{.orange} is used (either own or enemy's), there is a cap of $\text{50,000}$ for the value. In other words, if you use Angelica's skill on the enemy with $\text{2,000,000}$ {{HP}} **HP**{.orange}, only $\text{50,000}$ will be put as the value.

    ${\color{yellow}[2]}$: **Energy Guard** damage (from Boo Ghost Grandhildr) counts as {{HP}} **HP**{.orange} damage, but **has no cap value**.

=== "$\text{Skill\%}$"

    The Skill% mostly represents the percent (%) mentioned in the Skill Description. 

    ??? image "Image Showcase"
        ![Skill% Showcase](../assets/images/damage-formula/skill_desc.avif)
    
    There are some conditional $\text{Skill\%}$ values, meaning they are achievable, only when some conditions are met.

    <table class="data-table">
        <thead>
            <tr>
                <th colspan="2">Costume</th>
                <th>Skill%</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center">
                ![New Hire Nebris](../assets/images/damage-formula/illust_inven_char003303_149.avif){.icon-portrait}
                </td>
                <td><strong>New Hire Nebris</strong></td>
                <td>$[40\% \sim 80\%] + [15\% \sim 30\%] \times \text{Buffs Applied}$</td>
            </tr>
        </tbody>
    </table>

=== "$\text{\textcolor{ffe8aa}{ATK\%} Buffs}$"

    {{ATK}} **ATK%**{.yellow} / {{MATK}} **MATK%**{.magenta} Buff is the most common type of buff. It directly increases the character stat.

    These buffs are **additive**, if coming from different sources: 

    $\text{\textcolor{ffe8aa}{ATK\%} Total Buff = \textcolor{ffe8aa}{ATK\%} Buff 1 + \textcolor{ffe8aa}{ATK\%} Buff 2} + \dots $

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
                    ![Kind Student Samay](../assets/images/damage-formula/illust_inven_char101402_16.avif){.icon-portrait}
                    </td>
                    <td><strong>Kind Student Samay</strong></td>
                    <td>$20\% \sim 50\%$</td>
                    <td>$\text{2 Turns}$</td>
                    <td align="center">$0 \sim 2$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$20\% \sim 60\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{yellow}{[Domain]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>
                <tr>
                    <td align="center">
                    ![Medical Club Teresse](../assets/images/damage-formula/illust_inven_char001106_117.avif){.icon-portrait}
                    </td>
                    <td><strong>Medical Club Teresse</strong></td>
                    <td>$50\% \sim 120\%$</td>
                    <td>$\text{4 Turns}$</td>
                    <td align="center">$3 \sim 4$</td>
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
                    ![Hand of Salvation Elpis](../assets/images/damage-formula/illust_inven_char003101_122.avif){.icon-portrait}
                    </td>
                    <td><strong>Hand of Salvation Elpis</strong></td>
                    <td>$25\% \sim 80\%$</td>
                    <td>$\text{6 Turns}$</td>
                    <td align="center">$2 \sim 3$</td>
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
                    ![Shadow Bunny Eleaneer](../assets/images/damage-formula/illust_inven_char061103_187.avif){.icon-portrait}
                    </td>
                    <td><strong>Shadow Bunny Eleaneer</strong></td>
                    <td>$20\% \sim 60\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{yellow}{[Domain]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>
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
                    <td align="center">
                    ![Retired Legend Olivier](../assets/images/damage-formula/illust_inven_char003604_196.avif){.icon-portrait}
                    </td>
                    <td><strong>Retired Legend Olivier</strong></td>
                    <td>$60\% \sim 100\%$</td>
                    <td>$\text{10 Turns} \newline \text{\textcolor{yellow}{[Domain]}}$</td>
                    <td align="center">$4 \sim 6$</td>
                </tr>  
            </tbody>
        </table>
</div>