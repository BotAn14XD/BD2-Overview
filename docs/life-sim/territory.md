---

description: A technical guide to the Brown Dust 2 Territory management mode. Includes detailed information on resource generation, skill scaling formulas, building priorities, and optimization strategies for cooking and recruitment.
comments: true
image: assets/images/site-assets/territory-banner.png
hero: assets/images/site-assets/index-pc-nav-20.avif
icon: material/terrain

---
![Territory](../assets/images/site-assets/index-pc-nav-20.avif){: .card-header-img fetchpriority=high loading=eager }

#

Territory is a cozy management mode where players gather resources through farming, logging, and mining to build, landscape, and customize their own town while populating it with character residents.

!!! tip "TL;DR"

     * This is a game mode that does not impact your game progress in any way. Think of it as an optional time killer.  
     * To generate the currency, {{Local_Points}} **Local Points**, you need to actively farm and sell the cooked dishes. Refer to the [guide below](#cooking-guide) for more information.
     * Start by heavily investing in **Farming**, while upgrading your **Axe** and **Pickaxe** to increase resource yields and unlock decorations.

It is located in **Fantasia Square**. To access it, walk down the staircase at the bottom of the Square.
??? image "Image Guide"
    ![Access Guide](../assets/images/territory/access-guide.avif)

## Activities

There are three main activities you need to perform to progress in the Territory: **Logging**, **Mining**, and **Farming**. While Logging and Mining provide progression resources such as {{Rock}} **Rock** or {{Lumber}} **Lumber**, Farming primarily provides {{Local_Points}} **Local Points**.

### Logging

Logging is done via the **Logging Site**. It is the main source of {{Wooden_Branch}} **Wooden Branches**, {{Lumber}} **Lumber** and {{Sturdy_Lumber}} **Sturdy Lumber**. To obtain them, you must chop down a **tree** using the **Axe**.

Each tree has 3 stages of growth, with a more grown version providing **more resources** and **Logging EXP** but taking **longer to chop down**.

Therefore, you should **always** chop down only fully grown trees to obtain the maximum amount of resources.

??? image "Different Growth Stages"
    ![Different Growth Stages Image](../assets/images/territory/logging-1.avif)

??? example "Technical Details"

    * The Logging Site is a 3x3 field, resulting in a maximum of 9 trees.
    * Whenever any tile is empty, the Logging Site will grow **one Stage 1** tree in **60 seconds**. Therefore, if you chop down all the trees, it will take 9 minutes to replenish them completely.
    * A tree needs **120** seconds to grow into Stage 2 and **180** seconds to grow into Stage 3; therefore, it takes **5 minutes** to get a fully grown tree after it appears initially.
    * A tree's health determines how difficult it is to chop down, requiring a different number of hits depending on your progression.

    ---

    ??? abstract "Tree Health"
        * **Stage 1:** 20 
        * **Stage 2:** 29 
        * **Stage 3:** 38


    ---

    ??? abstract "Dropped Resources"
        * **Stage 1:** 3 {{Wooden_Branch}} **Wooden Branches**
        * **Stage 2:** 2 {{Wooden_Branch}} **Wooden Branches**, 3 {{Lumber}} **Lumber**
        * **Stage 3:** 2 {{Wooden_Branch}} **Wooden Branches**, 3 {{Lumber}} **Lumber** and 1 {{Sturdy_Lumber}} **Sturdy Lumber**

    ---

    ??? abstract "Logging EXP"
        * **Stage 1:** 1 EXP
        * **Stage 2:** 2 EXP
        * **Stage 3:** 4 EXP

### Mining

Mining is done via the **Quarry**. It is the main source of {{Rock}} **Rock**, {{Copper_Ore_T}} **Copper Ore**, {{Iron_Ore_T}} **Iron Ore**, {{Silver_Ore_T}} **Silver Ore** and {{Gold_Ore_T}} **Gold Ore**. To obtain them, you must mine the clusters with a **Pickaxe**.

Ores have different chances to appear; however, unlike trees, they do not grow and can be mined immediately upon spawning.

??? image "Different Ore Clusters Showcase"
    ![Different Ore Clusters Showcase](../assets/images/territory/mining-1.avif)

??? example "Technical Details"

    * Similar to the Logging site, the Quarry is a 3x3 field, resulting in a maximum of 9 clusters. The positioning isn't fixed in place; therefore, clusters are spawned randomly within the Quarry.
    * Whenever there are fewer than 9 ore clusters at any given moment, the Quarry will generate 1 cluster in **60** **seconds**. Therefore, if you mine all clusters, it will take 9 minutes to fill the Quarry again.

    ---

    ??? abstract "Clusters Spawn Chance"
        * {{Rock}} **Rock Cluster:** 30%
        * {{Copper_Ore_T}} **Copper Cluster:** 20%
        * {{Iron_Ore_T}} **Iron Cluster:** 25%
        * {{Silver_Ore_T}} **Silver Cluster:** 15%
        * {{Gold_Ore_T}} **Gold Cluster:** 10%

    ---

    ??? abstract "Cluster Health"
        * {{Rock}} **Rock Cluster:** 20
        * {{Copper_Ore_T}} **Copper Cluster:** 30
        * {{Iron_Ore_T}} **Iron Cluster:** 25
        * {{Silver_Ore_T}} **Silver Cluster:** 34
        * {{Gold_Ore_T}} **Gold Cluster:** 38

    ---

    ??? abstract "Dropped Resources"
        * {{Rock}} **Rock Cluster:** 4 {{Rock}} **Rock**
        * {{Copper_Ore_T}} **Copper Cluster:** 2 {{Rock}} **Rock**, 2 {{Copper_Ore_T}} **Copper Ore**
        * {{Iron_Ore_T}} **Iron Cluster:** 2 {{Rock}} **Rock**, 2 {{Iron_Ore_T}} **Iron Ore**
        * {{Silver_Ore_T}} **Silver Cluster:** 2 {{Rock}} **Rock**, 2 {{Silver_Ore_T}} **Silver Ore**
        * {{Gold_Ore_T}} **Gold Cluster:** 2 {{Rock}} **Rock**, 1 {{Gold_Ore_T}} **Gold Ore**

    ---

    ??? abstract "Mining EXP"
        * {{Rock}} **Rock Cluster:** 2 EXP
        * {{Copper_Ore_T}} **Copper Cluster:** 3 EXP
        * {{Iron_Ore_T}} **Iron Cluster:** 4 EXP
        * {{Silver_Ore_T}} **Silver Cluster:** 5 EXP
        * {{Gold_Ore_T}} **Gold Cluster:** 6 EXP

### Farming

Farming is done via the **Fields**. It is the main source of **Crops**, which can be turned into dishes with the help of a **Cooking Pot**. To gather crops, you need to use a **Sickle**.

Each crop requires seeds that are purchasable at the moment of planting. Crops have different prices and growth times.

??? example "Technical Details"

    * Similar to trees, crops have **3 stages of growth** that differ visually. This growth cycle, however, is structurally different from trees, as you cannot harvest crops at Stage 1 or 2.
    * Each crop has 3 rarities: **Normal**, **Rare** and **Legendary**. They differ by selling price and have different chances to be obtained from harvesting.
    * Normally, you get 1 item per harvest. This, however, can be changed by obtaining the **Crops Bonus** buff. Each **Crops Bonus** stack increases the quantity of the harvested crop by 1.

    ---

    ??? abstract "Crops Seeds Cost"
        * {{Shapely_Potato}} **Shapely Potato**: 1 {{Local_Points}} 
        * {{Spanking_Wheat}} **Spanking Wheat**: 1 {{Local_Points}}
        * {{Juicy_Onion}} **Juicy Onion**: 2 {{Local_Points}}
        * {{Virile_Mushroom}} **Virile Mushroom**: 3 {{Local_Points}}
        * {{Twin_Beans}} **Twin Beans**: 6 {{Local_Points}}
        * {{Cleft_Garlic}} **Cleft Garlic**: 8 {{Local_Points}}
        * {{Sticky_Rice}} **Sticky Rice**: 10 {{Local_Points}}
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: 20 {{Local_Points}}
        * {{Exposed_Corn}} **Exposed Corn**: 30 {{Local_Points}}
        * {{Firm_Apple}} **Firm Apple**: 40 {{Local_Points}}
        * {{Venus_Cacao}} **Venus Cacao**: 50 {{Local_Points}}
        * {{Stamina_Pepper}} **Stamina Pepper**: 60 {{Local_Points}}
        * {{Lustful_Grape}} **Lustful Grape**: 70 {{Local_Points}}
        * {{Sticky_Melon}} **Sticky Melon**: 80 {{Local_Points}}
        * {{Pulse_Saffron}} **Pulse Saffron**: 100 {{Local_Points}}


    ---

    ??? abstract "Crop Growth Time"
        * {{Shapely_Potato}} **Shapely Potato**: 1 Minute
        * {{Spanking_Wheat}} **Spanking Wheat**: 5 Minutes
        * {{Juicy_Onion}} **Juicy Onion**: 10 Minutes
        * {{Virile_Mushroom}} **Virile Mushroom**: 15 Minutes
        * {{Twin_Beans}} **Twin Beans**: 30 Minutes
        * {{Cleft_Garlic}} **Cleft Garlic**: 45 Minutes
        * {{Sticky_Rice}} **Sticky Rice**: 1 Hour
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: 3 Hours
        * {{Exposed_Corn}} **Exposed Corn**: 5 Hours
        * {{Firm_Apple}} **Firm Apple**: 8 Hours
        * {{Venus_Cacao}} **Venus Cacao**: 10 Hours
        * {{Stamina_Pepper}} **Stamina Pepper**: 12 Hours
        * {{Lustful_Grape}} **Lustful Grape**: 15 Hours
        * {{Sticky_Melon}} **Sticky Melon**: 18 Hours
        * {{Pulse_Saffron}} **Pulse Saffron**: 20 Hours

    --- 

    ??? abstract "Crop Sell Price"
        * {{Shapely_Potato}} **Shapely Potato**: <span class="price-normal">1</span> {{Local_Points}}, <span class="price-high">1</span> {{Local_Points}}, <span class="rainbow-text">1</span> {{Local_Points}}
        * {{Spanking_Wheat}} **Spanking Wheat**: <span class="price-normal">1</span> {{Local_Points}}, <span class="price-high">1</span> {{Local_Points}}, <span class="rainbow-text">2</span> {{Local_Points}}
        * {{Juicy_Onion}} **Juicy Onion**: <span class="price-normal">2</span> {{Local_Points}}, <span class="price-high">2</span> {{Local_Points}}, <span class="rainbow-text">3</span> {{Local_Points}}
        * {{Virile_Mushroom}} **Virile Mushroom**: <span class="price-normal">3</span> {{Local_Points}}, <span class="price-high">3</span> {{Local_Points}}, <span class="rainbow-text">4</span> {{Local_Points}}
        * {{Twin_Beans}} **Twin Beans**: <span class="price-normal">6</span> {{Local_Points}}, <span class="price-high">7</span> {{Local_Points}}, <span class="rainbow-text">9</span> {{Local_Points}}
        * {{Cleft_Garlic}} **Cleft Garlic**: <span class="price-normal">8</span> {{Local_Points}}, <span class="price-high">10</span> {{Local_Points}}, <span class="rainbow-text">12</span> {{Local_Points}}
        * {{Sticky_Rice}} **Sticky Rice**: <span class="price-normal">11</span> {{Local_Points}}, <span class="price-high">13</span> {{Local_Points}}, <span class="rainbow-text">15</span> {{Local_Points}}
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: <span class="price-normal">22</span> {{Local_Points}}, <span class="price-high">26</span> {{Local_Points}}, <span class="rainbow-text">30</span> {{Local_Points}}
        * {{Exposed_Corn}} **Exposed Corn**: <span class="price-normal">33</span> {{Local_Points}}, <span class="price-high">39</span> {{Local_Points}}, <span class="rainbow-text">45</span> {{Local_Points}}
        * {{Firm_Apple}} **Firm Apple**: <span class="price-normal">44</span> {{Local_Points}}, <span class="price-high">52</span> {{Local_Points}}, <span class="rainbow-text">60</span> {{Local_Points}}
        * {{Venus_Cacao}} **Venus Cacao**: <span class="price-normal">55</span> {{Local_Points}}, <span class="price-high">65</span> {{Local_Points}}, <span class="rainbow-text">75</span> {{Local_Points}}
        * {{Stamina_Pepper}} **Stamina Pepper**: <span class="price-normal">66</span> {{Local_Points}}, <span class="price-high">78</span> {{Local_Points}}, <span class="rainbow-text">90</span> {{Local_Points}}
        * {{Lustful_Grape}} **Lustful Grape**: <span class="price-normal">77</span> {{Local_Points}}, <span class="price-high">91</span> {{Local_Points}}, <span class="rainbow-text">105</span> {{Local_Points}}
        * {{Sticky_Melon}} **Sticky Melon**: <span class="price-normal">88</span> {{Local_Points}}, <span class="price-high">104</span> {{Local_Points}}, <span class="rainbow-text">120</span> {{Local_Points}}
        * {{Pulse_Saffron}} **Pulse Saffron**: <span class="price-normal">110</span> {{Local_Points}}, <span class="price-high">130</span> {{Local_Points}}, <span class="rainbow-text">150</span> {{Local_Points}}


    ---

    ??? abstract "Farming EXP"
        * {{Shapely_Potato}} **Shapely Potato**: 1 EXP
        * {{Spanking_Wheat}} **Spanking Wheat**: 1 EXP
        * {{Juicy_Onion}} **Juicy Onion**: 2 EXP
        * {{Virile_Mushroom}} **Virile Mushroom**: 2 EXP
        * {{Twin_Beans}} **Twin Beans**: 3 EXP
        * {{Cleft_Garlic}} **Cleft Garlic**: 4 EXP
        * {{Sticky_Rice}} **Sticky Rice**: 5 EXP
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: 10 EXP
        * {{Exposed_Corn}} **Exposed Corn**: 15 EXP
        * {{Firm_Apple}} **Firm Apple**: 20 EXP
        * {{Venus_Cacao}} **Venus Cacao**: 25 EXP
        * {{Stamina_Pepper}} **Stamina Pepper**: 30 EXP
        * {{Lustful_Grape}} **Lustful Grape**: 33 EXP
        * {{Sticky_Melon}} **Sticky Melon**: 36 EXP
        * {{Pulse_Saffron}} **Pulse Saffron**: 40 EXP


<!--
* {{Shapely_Potato}} **Shapely Potato**         id--2--no--1--
* {{Spanking_Wheat}} **Spanking Wheat**         id--1--no--2--
* {{Juicy_Onion}} **Juicy Onion**               id--3--no--3--
* {{Virile_Mushroom}} **Virile Mushroom**       id--4--no--4--
* {{Twin_Beans}} **Twin Beans**                 id--6--no--5--
* {{Cleft_Garlic}} **Cleft Garlic**             id--13--no--6--
* {{Sticky_Rice}} **Sticky Rice**               id--9--no--7--
* {{Curvaceous_Paprika}} **Curvaceous Paprika** id--8--no--8--
* {{Exposed_Corn}} **Exposed Corn**             id--5--no--9--
* {{Firm_Apple}} **Firm Apple**                 id--7--no--10--
* {{Venus_Cacao}} **Venus Cacao**               id--11--no--11--
* {{Stamina_Pepper}} **Stamina Pepper**         id--12--no--12--
* {{Lustful_Grape}} **Lustful Grape**           id--10--no--13--
* {{Sticky_Melon}} **Sticky Melon**             id--14--no--14--
* {{Pulse_Saffron}} **Pulse Saffron**           id--15--no--15--
-->

#### Crops List {.territory-inventory-grid}

{{ crop_tile("Shapely Potato") }}
{{ crop_tile("Spanking Wheat") }}
{{ crop_tile("Juicy Onion") }}
{{ crop_tile("Virile Mushroom") }}
{{ crop_tile("Twin Beans") }}
{{ crop_tile("Cleft Garlic") }}
{{ crop_tile("Sticky Rice") }}
{{ crop_tile("Curvaceous Paprika") }}
{{ crop_tile("Exposed Corn") }}
{{ crop_tile("Firm Apple") }}
{{ crop_tile("Venus Cacao") }}
{{ crop_tile("Stamina Pepper") }}
{{ crop_tile("Lustful Grape") }}
{{ crop_tile("Sticky Melon") }}
{{ crop_tile("Pulse Saffron") }}

## Player Levels

As was stated previously, doing any activity grants EXP. Each activity, such as **Logging**, **Mining**, or **Farming**, has a separate progress bar. Once you gain enough EXP in some activity, you get a level up.

Leveling up unlocks new crops and dishes (for **Farming**) and decorative items (for **Logging** and **Mining**). Additionally, each level up increases the corresponding **Skill**.

### Level Table

The table below displays the level, EXP required to reach it (from the previous level), Cumulative EXP, and the bonus that specific level provides. There is a total of 10 levels for each activity.

=== "Logging"

    <span class="responsive-table-wrapper">
    <table class="data-table">
        <thead>
            <tr>
                <th>Level</th>
                <th style="width:30%">EXP from previous Level</th>
                <th>Cumulative EXP</th>
                <th>Skill Bonus</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td>5 **Logging Skill**</td>
            </tr>
            <tr>
                <td>2</td>
                <td>15</td>
                <td>15</td>
                <td>11 **Logging Skill**</td>
            </tr>
            <tr>
                <td>3</td>
                <td>40</td>
                <td>55</td>
                <td>15 **Logging Skill**</td>
            </tr>
            <tr>
                <td>4</td>
                <td>100</td>
                <td>155</td>
                <td>20 **Logging Skill**</td>
            </tr>
            <tr>
                <td>5</td>
                <td>250</td>
                <td>405</td>
                <td>26 **Logging Skill**</td>
            </tr>
            <tr>
                <td>6</td>
                <td>500</td>
                <td>905</td>
                <td>32 **Logging Skill**</td>
            </tr>
            <tr>
                <td>7</td>
                <td>1000</td>
                <td>1905</td>
                <td>39 **Logging Skill**</td>
            </tr>
            <tr>
                <td>8</td>
                <td>1800</td>
                <td>3705</td>
                <td>46 **Logging Skill**</td>
            </tr>
            <tr>
                <td>9</td>
                <td>3000</td>
                <td>6705</td>
                <td>54 **Logging Skill**</td>
            </tr>
            <tr>
                <td>10</td>
                <td>5000</td>
                <td>11705</td>
                <td>62 **Logging Skill**</td>
            </tr>
        </tbody>
    </table>
    </span>

=== "Mining"

    <span class="responsive-table-wrapper">
    <table class="data-table">
        <thead>
            <tr>
                <th>Level</th>
                <th style="width:30%">EXP from previous Level</th>
                <th>Cumulative EXP</th>
                <th>Skill Bonus</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td>5 **Mining Skill**</td>
            </tr>
            <tr>
                <td>2</td>
                <td>15</td>
                <td>15</td>
                <td>11 **Mining Skill**</td>
            </tr>
            <tr>
                <td>3</td>
                <td>40</td>
                <td>55</td>
                <td>15 **Mining Skill**</td>
            </tr>
            <tr>
                <td>4</td>
                <td>100</td>
                <td>155</td>
                <td>20 **Mining Skill**</td>
            </tr>
            <tr>
                <td>5</td>
                <td>250</td>
                <td>405</td>
                <td>26 **Mining Skill**</td>
            </tr>
            <tr>
                <td>6</td>
                <td>500</td>
                <td>905</td>
                <td>32 **Mining Skill**</td>
            </tr>
            <tr>
                <td>7</td>
                <td>1000</td>
                <td>1905</td>
                <td>39 **Mining Skill**</td>
            </tr>
            <tr>
                <td>8</td>
                <td>1800</td>
                <td>3705</td>
                <td>46 **Mining Skill**</td>
            </tr>
            <tr>
                <td>9</td>
                <td>3000</td>
                <td>6705</td>
                <td>54 **Mining Skill**</td>
            </tr>
            <tr>
                <td>10</td>
                <td>5000</td>
                <td>11705</td>
                <td>62 **Mining Skill**</td>
            </tr>
        </tbody>
    </table>
    </span>

=== "Farming"

    <span class="responsive-table-wrapper">
    <table class="data-table">
        <thead>
            <tr>
                <th>Level</th>
                <th style="width:30%">EXP from previous Level</th>
                <th>Cumulative EXP</th>
                <th>Skill Bonus</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td>1 **Farming Skill**</td>
            </tr>
            <tr>
                <td>2</td>
                <td>9</td>
                <td>9</td>
                <td>2 **Farming Skill**</td>
            </tr>
            <tr>
                <td>3</td>
                <td>30</td>
                <td>39</td>
                <td>3 **Farming Skill**</td>
            </tr>
            <tr>
                <td>4</td>
                <td>80</td>
                <td>119</td>
                <td>4 **Farming Skill**</td>
            </tr>
            <tr>
                <td>5</td>
                <td>250</td>
                <td>369</td>
                <td>5 **Farming Skill**</td>
            </tr>
            <tr>
                <td>6</td>
                <td>600</td>
                <td>969</td>
                <td>6 **Farming Skill**</td>
            </tr>
            <tr>
                <td>7</td>
                <td>2000</td>
                <td>2969</td>
                <td>7 **Farming Skill**</td>
            </tr>
            <tr>
                <td>8</td>
                <td>6000</td>
                <td>8969</td>
                <td>8 **Farming Skill**</td>
            </tr>
            <tr>
                <td>9</td>
                <td>15000</td>
                <td>23969</td>
                <td>9 **Farming Skill**</td>
            </tr>
            <tr>
                <td>10</td>
                <td>43000</td>
                <td>66969</td>
                <td>10 **Farming Skill**</td>
            </tr>
        </tbody>
    </table>
    </span>

---

## Player Bonuses

### Skills

There are a total of 3 stats: **Logging Skill**, **Mining Skill**, and **Farming Skill**. You can check them all via Phone.

??? image "Image Guide"
    ![Skill Check](../assets/images/territory/stats.avif)

* **Logging Skill** increases the **damage** you deal to trees, effectively **reducing the number of hits** to chop down a tree.
* **Mining Skill** increases the **damage** you deal to ore clusters, effectively **reducing the number of hits** to mine a cluster.
* **Farming Skill** increases **crop rarity**, yielding higher rarity crops from the Fields.

??? abstract "Crop Rarity Chance"
    * **Farming Skill 1**: <span class="price-normal">80</span>, <span class="price-high">19.9</span>, <span class="rainbow-text">0.1%</span>
    * **Farming Skill 2**: <span class="price-normal">79</span>, <span class="price-high">20.8</span>, <span class="rainbow-text">0.2%</span>
    * **Farming Skill 3**: <span class="price-normal">78</span>, <span class="price-high">21.7</span>, <span class="rainbow-text">0.3%</span>
    * **Farming Skill 4**: <span class="price-normal">77</span>, <span class="price-high">22.6</span>, <span class="rainbow-text">0.4%</span>
    * **Farming Skill 5**: <span class="price-normal">76</span>, <span class="price-high">23.5</span>, <span class="rainbow-text">0.5%</span>
    * **Farming Skill 6**: <span class="price-normal">75</span>, <span class="price-high">24.3</span>, <span class="rainbow-text">0.7%</span>
    * **Farming Skill 7**: <span class="price-normal">74</span>, <span class="price-high">25.1</span>, <span class="rainbow-text">0.9%</span>
    * **Farming Skill 8**: <span class="price-normal">73</span>, <span class="price-high">25.9</span>, <span class="rainbow-text">1.1%</span>
    * **Farming Skill 9**: <span class="price-normal">72</span>, <span class="price-high">26.7</span>, <span class="rainbow-text">1.3%</span>
    * **Farming Skill 10**: <span class="price-normal">71</span>, <span class="price-high">27.5</span>, <span class="rainbow-text">1.5%</span>
    * **Farming Skill 11**: <span class="price-normal">70</span>, <span class="price-high">28.3</span>, <span class="rainbow-text">1.7%</span>
    * **Farming Skill 12**: <span class="price-normal">69</span>, <span class="price-high">29.1</span>, <span class="rainbow-text">1.9%</span>
    * **Farming Skill 13**: <span class="price-normal">68</span>, <span class="price-high">30</span>, <span class="rainbow-text">2%</span>
    * **Farming Skill 14**: <span class="price-normal">67</span>, <span class="price-high">30.9</span>, <span class="rainbow-text">2.1%</span>
    * **Farming Skill 15**: <span class="price-normal">66</span>, <span class="price-high">31.7</span>, <span class="rainbow-text">2.3%</span>
    * **Farming Skill 16**: <span class="price-normal">65</span>, <span class="price-high">32.5</span>, <span class="rainbow-text">2.5%</span>
    * **Farming Skill 17**: <span class="price-normal">64</span>, <span class="price-high">33.3</span>, <span class="rainbow-text">2.7%</span>
    * **Farming Skill 18**: <span class="price-normal">63</span>, <span class="price-high">34</span>, <span class="rainbow-text">3%</span>
    * **Farming Skill 19**: <span class="price-normal">62</span>, <span class="price-high">34.5</span>, <span class="rainbow-text">3.5%</span>
    * **Farming Skill 20**: <span class="price-normal">61</span>, <span class="price-high">34.8</span>, <span class="rainbow-text">4.2%</span>
    * **Farming Skill 21**: <span class="price-normal">60</span>, <span class="price-high">35</span>, <span class="rainbow-text">5%</span>
    * **Farming Skill 22**: <span class="price-normal">59</span>, <span class="price-high">35.8</span>, <span class="rainbow-text">5.2%</span>
    * **Farming Skill 23**: <span class="price-normal">58</span>, <span class="price-high">36.5</span>, <span class="rainbow-text">5.5%</span>
    * **Farming Skill 24**: <span class="price-normal">57</span>, <span class="price-high">37.1</span>, <span class="rainbow-text">5.9%</span>
    * **Farming Skill 25**: <span class="price-normal">56</span>, <span class="price-high">37.6</span>, <span class="rainbow-text">6.4%</span>
    * **Farming Skill 26**: <span class="price-normal">55</span>, <span class="price-high">38</span>, <span class="rainbow-text">7%</span>
    * **Farming Skill 27**: <span class="price-normal">54</span>, <span class="price-high">38.3</span>, <span class="rainbow-text">7.7%</span>
    * **Farming Skill 28**: <span class="price-normal">53</span>, <span class="price-high">38.5</span>, <span class="rainbow-text">8.5%</span>
    * **Farming Skill 29**: <span class="price-normal">52</span>, <span class="price-high">38.6</span>, <span class="rainbow-text">9.4%</span>
    * **Farming Skill 30**: <span class="price-normal">51</span>, <span class="price-high">39</span>, <span class="rainbow-text">10%</span>
    * **Farming Skill 31**: <span class="price-normal">50</span>, <span class="price-high">39</span>, <span class="rainbow-text">11%</span>

??? example "Technical Details"
    * All skills can be increased via **Tools**, **Leveling Up** and **Consuming specific Food**.
    * **Farming Skill** is hard-capped at 31.

    !!! abstract "Skills Formula"
        * $\text{Logging} = 4 + \text{Logging LVL Bonus} + \text{Tool Bonus}$
        * $\text{Mining} = 4 + \text{Mining LVL Bonus} + \text{Tool Bonus}$
        * $\text{Farming} = 1 + \text{Farming LVL Bonus} + \text{Tool Bonus}$
    
    * **Damage** for **Logging** and **Mining** is calculated as $\frac{1}{3.8} \times \text{Skill Value}$.
        * This means if you have 145 **Mining & Logging** Skills, you can instantly chop any tree or mine any ore cluster.

<div class="custom-nav-card-1" style="padding: 20px; max-width: 100%; margin: 20px auto;">
    <h3 class="letter-heading" style="margin-top: 0; text-align: center;">Gathering Breakpoint Calculator</h3>
    
    <div style="display: flex; gap: 15px; margin-bottom: 15px;">
        <label class="white bold" style="flex: 1;">
            Logging Skill:<br>
            <input type="number" id="calc-log-skill" value="40" min="4" max="300" class="slang-search-box" style="margin-top: 8px; margin-bottom: 0;">
        </label>
        
        <label class="white bold" style="flex: 1;">
            Mining Skill:<br>
            <input type="number" id="calc-mine-skill" value="40" min="4" max="300" class="slang-search-box" style="margin-top: 8px; margin-bottom: 0;">
        </label>
    </div>

    <label class="white bold">
        Select the Target:<br>
        <select id="calc-target" class="slang-search-box" style="margin-top: 8px; margin-bottom: 0; cursor: pointer;">
            <option value="small_tree">Small Tree</option>
            <option value="medium_tree">Medium Tree</option>
            <option value="large_tree">Large Tree</option>
            <option value="rock">Rock Cluster</option>
            <option value="copper_ore">Copper Ore Cluster</option>
            <option value="iron_ore">Iron Ore Cluster</option>
            <option value="silver_ore">Silver Ore Cluster</option>
            <option value="gold_ore">Gold Ore Cluster</option>
        </select>
    </label>

    <span class="tooltip-divider-line"></span>

    <div style="display: flex; flex-direction: column; gap: 8px;">
        <span class="tooltip-line gray bold">
            Relevant Skill Used: <strong class="white stat-num" id="calc-active-skill">0</strong>
        </span>
        <span class="tooltip-line gray bold">
            Damage Per Hit: <strong class="yellow stat-num" id="calc-dmg">0.00</strong>
        </span>
        <span class="tooltip-line gray bold">
            Hits to Clear: <strong class="magenta stat-num" id="calc-hits" style="font-size: 1.2em;">0</strong>
        </span>
    </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const logInput = document.getElementById('calc-log-skill');
    const mineInput = document.getElementById('calc-mine-skill');
    const targetSelect = document.getElementById('calc-target');
    
    const activeSkillOut = document.getElementById('calc-active-skill');
    const dmgOut = document.getElementById('calc-dmg');
    const hitsOut = document.getElementById('calc-hits');
    
    const NODE_DATABASE = {
        "small_tree": { type: "logging", hp: 20.00 },
        "medium_tree": { type: "logging", hp: 29.00 },
        "large_tree": { type: "logging", hp: 38.00 }, 
        "rock": { type: "mining",  hp: 20.00 },
        "copper_ore": { type: "mining",  hp: 30.00 },
        "iron_ore":   { type: "mining",  hp: 25.00 },
        "silver_ore":   { type: "mining",  hp: 34.00 },
        "gold_ore":   { type: "mining",  hp: 38.00 } 
    };

    function updateCalc() {
        const targetKey = targetSelect.value;
        const nodeData = NODE_DATABASE[targetKey];
        
        let activeSkill = 0;
        if (nodeData.type === "logging") {
            activeSkill = parseInt(logInput.value) || 0;
        } else if (nodeData.type === "mining") {
            activeSkill = parseInt(mineInput.value) || 0;
        }
        
        activeSkillOut.textContent = `${activeSkill} (${nodeData.type.charAt(0).toUpperCase() + nodeData.type.slice(1)})`;
        
        let dmg = activeSkill / 3.8; 
        dmgOut.textContent = dmg.toFixed(2);
        
        if (dmg > 0) {
            let hits = Math.ceil(nodeData.hp / dmg);
            hitsOut.textContent = hits;
        } else {
            hitsOut.textContent = "∞";
        }
    }

    logInput.addEventListener('input', updateCalc);
    mineInput.addEventListener('input', updateCalc);
    targetSelect.addEventListener('change', updateCalc);
    
    updateCalc();
});
</script>

### Other Bonuses

* **Lumber Bonus**: Increases obtained wood count from logging by 1 per bonus active.
* **Mineral Bonus**: Increases obtained ores count from mining by 1 per bonus active.
* **Crops Bonus**: Increases obtained crops count from farming by 1 per bonus active.

## Buildings

There are 11 building types, each having its own purpose. Most of the buildings cost resources to build and take some time to be built.

Hover over the icons below to learn more about each of the buildings.

### Building List {.territory-inventory-grid}

{{ territory_tile("Home") }}
{{ territory_tile("Cooking Pot") }}
{{ territory_tile("Workbench") }}
{{ territory_tile("Helper Lodging") }}
{{ territory_tile("Resident Mansion") }}
{{ territory_tile("Pub") }}
{{ territory_tile("Warehouse") }}
{{ territory_tile("Field") }}
{{ territory_tile("Logging Site") }}
{{ territory_tile("Quarry") }}
{{ territory_tile("Forge") }}

### Building Priority

1. **Home**, **Cooking Pot**, **Workbench**, **Forge**, **Resident Mansion** x1 — during initial Missions.
2. **Fields**
3. **Logging Site** & **Quarry**
4. **Pub** & **Warehouse**
5. **Helper Lodging**
6. **Resident Mansion** x4 — Optional & Cosmetic Only.

## Territory Options & Expansion

### Select Territory (Terrain)

During the intro, you can choose 1 of 6 Territory layouts: **Plain Terrain**, **River Terrain 1**, **River Terrain 2**, **Coast Terrain**, **Beach Terrain I**, and **Beach Terrain II**.

Your chosen terrain does not affect your progression.

You cannot place anything except **Bridges** on **Water Tiles**, which technically means that the **Plain Terrain** layout contains the most buildable tiles.

??? image "Terrain Selection"
    ![Terrain Selection](../assets/images/territory/select_territory.avif)

You can change the Terrain at any given point via **Phone**, but doing so will:

* Destroy all structures you've built, with a material refund.
* Destroy all crops, trees, and ores **without a refund**.
* Remove all expansions, with a {{Local_Points}} **Local Points** refund.

This essentially means that for refunding, you should not have any active crops growing and be ready to spend time rebuilding all buildings from scratch.

??? image "Change Terrain Guide"
    ![Change Terrain Guide](../assets/images/territory/swap_guide.avif)

??? image "Confirmation Window"
    ![Confirmation Window](../assets/images/territory/confirmation.avif)

Worth mentioning that despite **Helper Lodging** will be destroyed as well, **Helpers** you recruited before can be recruited back for free.

### Territory Expansion

Each terrain layout contains locked regions, which you can unlock using {{Local_Points}} **Local Points**.

You start with 9 unlocked regions and can expand up to 25 using the Territory Phone.

??? image "Image Guide"
    ![Expand Guide](../assets/images/territory/expand_guide.avif)

<span class="responsive-table-wrapper">
<table class="data-table">
    <thead>
        <tr>
            <th>Regions Unlocked</th>
            <th style="width:30%">Cost for the next, {{Local_Points}}</th>
            <th>Total Cost, {{Local_Points}}</th>
            <th>Flooring, Mats & Fixtures Limit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>2</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>3</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>4</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>5</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>6</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>7</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>8</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>9</td>
            <td>40</td>
            <td>40</td>
            <td>650</td>
        </tr>
        <tr>
            <td>10</td>
            <td>100</td>
            <td>140</td>
            <td>750</td>
        </tr>
        <tr>
            <td>11</td>
            <td>300</td>
            <td>440</td>
            <td>850</td>
        </tr>
        <tr>
            <td>12</td>
            <td>1000</td>
            <td>1440</td>
            <td>950</td>
        </tr>
        <tr>
            <td>13</td>
            <td>2500</td>
            <td>3940</td>
            <td>1050</td>
        </tr>
        <tr>
            <td>14</td>
            <td>5000</td>
            <td>8940</td>
            <td>1150</td>
        </tr>
        <tr>
            <td>15</td>
            <td>9000</td>
            <td>17940</td>
            <td>1250</td>
        </tr>
        <tr>
            <td>16</td>
            <td>15000</td>
            <td>32940</td>
            <td>1350</td>
        </tr>
        <tr>
            <td>17</td>
            <td>22000</td>
            <td>54940</td>
            <td>1450</td>
        </tr>
        <tr>
            <td>18</td>
            <td>32000</td>
            <td>86940</td>
            <td>1550</td>
        </tr>
        <tr>
            <td>19</td>
            <td>45000</td>
            <td>131940</td>
            <td>1650</td>
        </tr>
        <tr>
            <td>20</td>
            <td>60000</td>
            <td>191940</td>
            <td>1750</td>
        </tr>
        <tr>
            <td>21</td>
            <td>75000</td>
            <td>266940</td>
            <td>1850</td>
        </tr>
        <tr>
            <td>22</td>
            <td>85000</td>
            <td>351940</td>
            <td>1950</td>
        </tr>
        <tr>
            <td>23</td>
            <td>92000</td>
            <td>443940</td>
            <td>2050</td>
        </tr>
        <tr>
            <td>24</td>
            <td>100000</td>
            <td>543940</td>
            <td>2150</td>
        </tr>
    </tbody>
</table>
</span>

The **order** in which you expand the Territory **does not matter**. This also provides no real gain except increased space for placement; therefore, expand only when you need more room or when you have good {{Local_Points}} **Local Points** income.

## Dishes

Dishes are the items you can create using a **Cooking Pot**. They can be consumed to obtain a **temporary bonus** or be **sold** for {{Local_Points}} **Local Points**.

Each dish provides different bonuses, but all have a 10-minute duration. Consuming the same dish again extends the bonus duration, while bonuses from different dishes stack.

!!! abstract "An Example"
    * If you consume **Virile Gnocchi**, you will get +8 Logging Skill for 10 minutes.
    * If you consume <u>**two**</u> **Virile Gnocchis**, you will get +8 Logging Skill for **20** minutes instead.
    * If you consume **Virile Gnocchi** <u>**and**</u> **Curvaceous Fried Rice**, you will get **+18** Logging Skill and +10 Mining Skill for 10 minutes instead.

There is no difference in dishes depending on the ingredient rarity you use; therefore, using Normal rarity ingredients exclusively is preferred, allowing you to sell higher rarity crops for more profit.

### Dishes List {.territory-inventory-grid}

{{ dish_tile("Virile Gnocchi") }}
{{ dish_tile("Bulbous Crepe") }}
{{ dish_tile("Creamy Congee") }}
{{ dish_tile("Curvaceous Fried Rice") }}
{{ dish_tile("Milky Steak") }}
{{ dish_tile("Venus Pudding") }}
{{ dish_tile("Stamina Pasta") }}
{{ dish_tile("Hormone Glass Noodles") }}
{{ dish_tile("Lingerie Cookie") }}
{{ dish_tile("Apple Tea") }}
{{ dish_tile("Nude Salad") }}
{{ dish_tile("Lustful Tart") }}
{{ dish_tile("Libido Soup") }}

### Cooking Guide

There are several strategies when it comes to gaining {{Local_Points}} **Local Points**.

They can be roughly divided into **Active (Early Game)**, **More Passive (Late Game)**, and **Lazy**.

=== "Active (Early Game)"

    The main income for the early game and active gameplay comes from {{Virile_Gnocchi}} **Virile Gnocchi**. 
    
    It is easy to mass-produce and is available immediately; however, this requires constantly playing the game, which is a significant downside on its own.

=== "More Passive (Late Game)"

    A more passive approach revolves around the **Crop Bonus** from dishes.

    That involves three dishes:
    
    * {{Lingerie_Cookie}} **Lingerie Cookie**
    * {{Lustful_Tart}} **Lustful Tart**
    * {{Libido_Soup}} **Libido Soup**

    The idea relies on **consuming** these three dishes before harvesting fully grown ingredients for them, such as {{Pulse_Saffron}} **Pulse Saffron**.

    Therefore, you must always save 3 of each dish listed above and cycle their production to maximize the **Crop Bonus**.

    Alternatively, you can grow {{Venus_Cacao}} **Venus Cacao**, {{Stamina_Pepper}} **Stamina Pepper**, {{Lustful_Grape}} **Lustful Grape**, {{Sticky_Melon}} **Sticky Melon** and {{Pulse_Saffron}} **Pulse Saffron** in a ratio of 3:3:3:3:88 (3 {{Venus_Cacao}} **Venus Cacao**, 3 {{Stamina_Pepper}} **Stamina Pepper**, 3 {{Lustful_Grape}} **Lustful Grape**, 3 {{Sticky_Melon}} **Sticky Melon** and 88 {{Pulse_Saffron}} **Pulse Saffron** placed at the same time).

    If you have [Helpers](#helpers) with high Farming Efficiency, you can manually grow {{Pulse_Saffron}} **Pulse Saffron** only and let Helpers grow the rest of the necessary crops.

=== "Lazy"

    Honestly, cooking any food results in a net positive. Therefore, you can ignore all advice and grow whatever you want based on what best fits your login schedule.
    
    Territory is not tied to the main gameplay; therefore, there is no reason to rush anything when it comes to this game mode.

---

<!-- ## Missions -->

## Tools

Tools are designed to improve resource-gathering efficiency.

There are **3** tools, each having **4** rarities: **Stone**, **Copper**, **Silver**, and **Gold**.

While **Stone** tools are given by default, you can upgrade them in the **Forge**. Each upgrade costs **Materials** and {{Local_Points}} **Local Points**.

??? example "Technical Details"
    * **Pickaxe** and **Axe** increase **Mining** and **Logging Skills**, as well as **Lumber** and **Mineral** bonuses respectively.
    * **Sickle**, on the other hand, increases **Farming Skill** and **Simultaneous Harvesting Capacity** — the amount of crops you can collect in one swing.

### Tools List

#### Axe {.territory-inventory-grid}

{{ tool_tile("Stone Axe") }}
{{ tool_tile("Copper Axe") }}
{{ tool_tile("Silver Axe") }}
{{ tool_tile("Gold Axe") }}

#### Pickaxe {.territory-inventory-grid}

{{ tool_tile("Stone Pickaxe") }}
{{ tool_tile("Copper Pickaxe") }}
{{ tool_tile("Silver Pickaxe") }}
{{ tool_tile("Gold Pickaxe") }}

#### Sickle {.territory-inventory-grid}

{{ tool_tile("Stone Sickle") }}
{{ tool_tile("Copper Sickle") }}
{{ tool_tile("Silver Sickle") }}
{{ tool_tile("Gold Sickle") }}

### Tools Priority

1. **Axe** and **Pickaxe**. Their upgrades increase the quantity of items obtained, similar to the **Pub** and **Warehouse** buildings.
2. **Sickle**. It will help you grow rarer crops and collect more of them within one swing, which can be crucial during [Late Game Cooking Strategy](#more-passive-late-game).

**Axe / Pickaxe** are slightly better due to the increased item drop that you can use as an additional income source from selling raw materials.

You should prioritize Tools before [**Helpers**](#helpers).

## Helpers

To earn resources offline, you can hire **Helpers** by first constructing a **Helper Lodging** building.

Recruiting a Helper costs 5000 {{Local_Points}} **Local Points**.

After you press the "Start Recruiting" button, you will be allowed to choose one of three Helpers to recruit.

??? image "Recruitment Menu"
    ![Helper Recruitment Menu](../assets/images/territory/helper-2.avif)

Each Helper has 3 stats:

* **Logging Efficiency**: The quantity of trees chopped per 4 hours.
* **Mining Efficiency**: The quantity of ore mined every 4 hours.
* **Farming Efficiency**: The quantity of items harvested per 1 crop harvested.

Each stat value can vary from 1 to 6; therefore, recruiting a Helper with the highest possible efficiency stats is ideal.

There are a total of 8 Races:

* **Goblin**
* **Orc**
* **Rabbit Beastfolk**
* **Squirrel Beastfolk**
* **Sheep Beastfolk**
* **Cat Beastfolk**
* **Puppy Beastfolk**
* **Unknown** (Yuridori)

??? example "Technical Details"

    * There are 180 possible options that can appear during Recruitment.

    ---

    * The chance to get **Goblin** or **Orc**: 37% each.
    * The chance to get **Rabbit Beastfolk**, **Sheep Beastfolk**, **Puppy Beastfolk**, **Squirrel Beastfolk**, **Cat Beastfolk**: 5% each.
    * The chance to get **Unknown** (Yuridori): 1%.

    ---

    * There is a 59.4776% chance to get at least one Beastfolk or Yuridori from the selection.

    ---

    * **Squirrel Beastfolk** is the only race that can get **Logging Efficiency** of 6 (Chance: 0.2%).
    * **Sheep Beastfolk** is the only race that can get **Mining Efficiency** of 6 (Chance: 0.2%).
    * **Rabbit Beastfolk** is the only race that can get **Farming Efficiency** of 6 (Chance: 0.2%).

    ---

    * **Cat Beastfolk** and **Unknown** (Yuridori) races have the best average Efficiency but both have a maximum value of 5.

    ---

    * Helpers cannot harvest **Rare** or **Legendary** crops; they only gather items of **Normal** rarity.
    * Helpers do not interact with the crops on your active fields; instead, they produce resources in a separate, virtual inventory space.

Upon recruiting a Helper, you can assign them to do one task. If the task is Farming, you can choose the crop to grow as well.

You can also **Rename**, **Replace** them, or **Terminate the Contract** with them, essentially deleting the Helper.
??? image "Manage Helper Menu"
    ![Manage Helper Menu](../assets/images/territory/helper-3.avif)

Resources gathered by Helpers are stored automatically with no player involvement. They have a cap of 24h, similar to **Diner Sales** or the **Fish Trap**.

To gather earned resources, press **Business Management** in the main menu.

??? image "Image Guide"
    ![Collecting Resources from Helpers](../assets/images/territory/helper-idle.avif)

## Related Links

* [Territory Codex | Brown Dust II Database by <u>Souseha</u>](https://browndust2-db.souseha.com/en/territory)

<!--{{ territory_table() }}

{{ crop_table() }}

{{ dish_table() }}

{{ tool_table() }}

{{ materials_table() }}-->
