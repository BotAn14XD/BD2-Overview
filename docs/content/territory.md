---
comments: true
image: assets/images/site-assets/territory-banner.png
---
![Territory](../assets/images/site-assets/index-pc-nav-20.avif){: .card-header-img }
#

Territory is a cozy management mode where players gather resources through farming, logging, and mining to build, landscape, and customize their own town while populating it with character residents.

It is located in **Fantasia Square**. To access it, walk down the staircase at the bottom of the Square.
??? image "Image Guide"
    ![Access Guide](../assets/images/territory/access-guide.avif)

## Activities

There are three main activities you need to do to progress in the Territory: **Logging**, **Mining** and **Farming**. While Logging and Mining give you resources to progress such as {{Rock}} **Rock** or {{Lumber}} **Lumber**, Farming essentially gives you {{Local_Points}} **Local Points**.

### Logging

Logging is done via the **Logging Site**. It is the main source of {{Wooden_Branch}} **Wooden Branches**, {{Lumber}} **Lumber** and {{Sturdy_Lumber}} **Sturdy Lumber**. To obtain them, you must chop down a **tree** using the **Axe**.

Each tree has 3 stages of growth, with a more grown version providing **more resources** and **Logging EXP** but taking **longer to chop down**.

Therefore, you should **always** chop down only the most grown trees to obtain the biggest amount of resources.

??? image "Different Growth Stages"
    ![Different Growth Stages Image](../assets/images/territory/logging-1.avif)

??? example "Technical Details"

    * The Logging Site is a $3x3$ field, resulting in a possible $9$ trees.
    * Whenever any tile is empty, the Logging Site will grow **one Stage 1** tree in $\bf{60}$ **seconds**. Therefore, if you chopped all trees, it will take $9$ minutes to replant them completely.
    * A tree needs $\bf{120}$ seconds to grow into Stage 2 and $\bf{180}$ seconds to grow into Stage 3, therefore, it takes $\bf{5}$ **minutes** to get a fully grown tree after it appeared initially.
    * Health of the tree determines how hard it is to destroy it, resulting in a different amount of hits depending on your progression.

    ---

    ??? abstract "Trees Health"
        * **Stage 1:** $20$ 
        * **Stage 2:** $29$ 
        * **Stage 3:** $38$


    ---

    ??? abstract "Dropped Resources"
        * **Stage 1:** $3$ {{Wooden_Branch}} **Wooden Branches**
        * **Stage 2:** $2$ {{Wooden_Branch}} **Wooden Branches**, $3$ {{Lumber}} **Lumber**
        * **Stage 3:** $2$ {{Wooden_Branch}} **Wooden Branches**, $3$ {{Lumber}} **Lumber** and $1$ {{Sturdy_Lumber}} **Sturdy Lumber**

    ---

    ??? abstract "Logging EXP"
        * **Stage 1:** $1$ EXP
        * **Stage 2:** $2$ EXP
        * **Stage 3:** $4$ EXP

### Mining

Mining is done via the **Quarry**. It is the main source of {{Rock}} **Rock**, {{Copper_Ore_T}} **Copper Ore**, {{Iron_Ore_T}} **Iron Ore**, {{Silver_Ore_T}} **Silver Ore** and {{Gold_Ore_T}} **Gold Ore**. To obtain them {{Local_Points}}, you must mine the clusters with a **Pickaxe**.

Ores have different chances to appear but, unlike trees, they have no growth, and therefore can be mined immediately as they are generated.

??? image "Different Ore Clusters Showcase"
    ![Different Ore Clusters Showcase](../assets/images/territory/mining-1.avif)

??? example "Technical Details"

    * Similar to the Logging site, the Quarry is a $3x3$ field, resulting in a possible $9$ clusters. The positioning isn't fixed in place; therefore, clusters are spawned randomly within the Quarry.
    * Whenever there are less than $9$ ore clusters at the given moment, the Quarry will generate 1 cluster in $\bf{60}$ **seconds**. Therefore, if you mined all clusters, it will take $9$ minutes to fill the Quarry again.

    ---

    ??? abstract "Clusters Spawn Chance"
        * {{Rock}} **Rock Cluster:** $30\%$
        * {{Copper_Ore_T}} **Copper Cluster:** $20\%$
        * {{Iron_Ore_T}} **Iron Cluster:** $25\%$
        * {{Silver_Ore_T}} **Silver Cluster:** $15\%$
        * {{Gold_Ore_T}} **Gold Cluster:** $10\%$

    ---

    ??? abstract "Clusters Health"
        * {{Rock}} **Rock Cluster:** $20$
        * {{Copper_Ore_T}} **Copper Cluster:** $30$
        * {{Iron_Ore_T}} **Iron Cluster:** $25$
        * {{Silver_Ore_T}} **Silver Cluster:** $34$
        * {{Gold_Ore_T}} **Gold Cluster:** $38$

    ---

    ??? abstract "Dropped Resources"
        * {{Rock}} **Rock Cluster:** $4$ {{Rock}} **Rock**
        * {{Copper_Ore_T}} **Copper Cluster:** $2$ {{Rock}} **Rock**, $2$ {{Copper_Ore_T}} **Copper Ore**
        * {{Iron_Ore_T}} **Iron Cluster:** $2$ {{Rock}} **Rock**, $2$ {{Iron_Ore_T}} **Iron Ore**
        * {{Silver_Ore_T}} **Silver Cluster:** $2$ {{Rock}} **Rock**, $2$ {{Silver_Ore_T}} **Silver Ore**
        * {{Gold_Ore_T}} **Gold Cluster:** $2$ {{Rock}} **Rock**, $1$ {{Gold_Ore_T}} **Gold Ore**

    ---

    ??? abstract "Mining EXP"
        * {{Rock}} **Rock Cluster:** $2$ EXP
        * {{Copper_Ore_T}} **Copper Cluster:** $3$ EXP
        * {{Iron_Ore_T}} **Iron Cluster:** $4$ EXP
        * {{Silver_Ore_T}} **Silver Cluster:** $5$ EXP
        * {{Gold_Ore_T}} **Gold Cluster:** $6$ EXP

### Farming

Farming is done via the **Fields**. It is the main source of **Crops**, which can be turned into dishes with the help of a **Cooking Pot**. To gather crops, you need to use a **Scythe**.

Each crop requires seeds that are purchasable at the moment of planting. Crops have different price and growth time.


??? example "Technical Details"

    * Similar to trees, crops have **3 stages of growth** that differ visually. That, however, isn't as functional as trees, because you cannot collect crops at Stage 1 or 2.
    * Each crop has 3 rarities: **Normal**, **Rare** and **Legendary**. They differ by selling price and have different chance to be obtained from harvesting.
    * Normally, you get 1 item per harvest. This, however, can be changed by obtaining **Crops Bonus** buff. Each **Crops Bonus** increases quantity of received crop by 1.

    ---

    ??? abstract "Crops Seeds Cost"
        * {{Spanking_Wheat}} **Spanking Wheat**: $1$ {{Local_Points}}
        * {{Shapely_Potato}} **Shapely Potato**: $1$ {{Local_Points}}
        * {{Juicy_Onion}} **Juicy Onion**: $2$ {{Local_Points}}
        * {{Virile_Mushroom}} **Virile Mushroom**: $3$ {{Local_Points}}
        * {{Exposed_Corn}} **Exposed Corn**: $30$ {{Local_Points}}
        * {{Twin_Beans}} **Twin Beans**: $6$ {{Local_Points}}
        * {{Firm_Apple}} **Firm Apple**: $40$ {{Local_Points}}
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: $20$ {{Local_Points}}
        * {{Sticky_Rice}} **Sticky Rice**: $10$ {{Local_Points}}
        * {{Lustful_Grape}} **Lustful Grape**: $70$ {{Local_Points}}
        * {{Venus_Cacao}} **Venus Cacao**: $50$ {{Local_Points}}
        * {{Stamina_Pepper}} **Stamina Pepper**: $60$ {{Local_Points}}
        * {{Cleft_Garlic}} **Cleft Garlic**: $8$ {{Local_Points}}
        * {{Sticky_Melon}} **Sticky Melon**: $80$ {{Local_Points}}
        * {{Pulse_Saffron}} **Pulse Saffron**: $100$ {{Local_Points}}


    ---

    ??? abstract "Crops Growth Time"
        * {{Spanking_Wheat}} **Spanking Wheat**: $5$ Minutes
        * {{Shapely_Potato}} **Shapely Potato**: $1$ Minute
        * {{Juicy_Onion}} **Juicy Onion**: $10$ Minutes
        * {{Virile_Mushroom}} **Virile Mushroom**: $15$ Minutes
        * {{Exposed_Corn}} **Exposed Corn**: $5$ Hours
        * {{Twin_Beans}} **Twin Beans**: $30$ Minutes
        * {{Firm_Apple}} **Firm Apple**: $8$ Hours
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: $3$ Hours
        * {{Sticky_Rice}} **Sticky Rice**: $1$ Hour
        * {{Lustful_Grape}} **Lustful Grape**: $15$ Hours
        * {{Venus_Cacao}} **Venus Cacao**: $10$ Hours
        * {{Stamina_Pepper}} **Stamina Pepper**: $12$ Hours
        * {{Cleft_Garlic}} **Cleft Garlic**: $45$ Minutes
        * {{Sticky_Melon}} **Sticky Melon**: $18$ Hours
        * {{Pulse_Saffron}} **Pulse Saffron**: $20$ Hours

    --- 

    ??? abstract "Crops Sell Price"
        * {{Spanking_Wheat}} **Spanking Wheat**: $\textcolor{82d68b}{1}$ {{Local_Points}}, $\textcolor{77c8f9}{1}$ {{Local_Points}}, <span class="rainbow-text">$2$ </span> {{Local_Points}}
        * {{Shapely_Potato}} **Shapely Potato**: $\textcolor{82d68b}{1}$ {{Local_Points}}, $\textcolor{77c8f9}{1}$ {{Local_Points}}, <span class="rainbow-text">$1$ </span> {{Local_Points}}
        * {{Juicy_Onion}} **Juicy Onion**: $\textcolor{82d68b}{2}$ {{Local_Points}}, $\textcolor{77c8f9}{2}$ {{Local_Points}}, <span class="rainbow-text">$3$ </span> {{Local_Points}}
        * {{Virile_Mushroom}} **Virile Mushroom**: $\textcolor{82d68b}{3}$ {{Local_Points}}, $\textcolor{77c8f9}{3}$ {{Local_Points}}, <span class="rainbow-text">$4$ </span> {{Local_Points}}
        * {{Exposed_Corn}} **Exposed Corn**: $\textcolor{82d68b}{33}$ {{Local_Points}}, $\textcolor{77c8f9}{39}$ {{Local_Points}}, <span class="rainbow-text">$45$ </span> {{Local_Points}}
        * {{Twin_Beans}} **Twin Beans**: $\textcolor{82d68b}{6}$ {{Local_Points}}, $\textcolor{77c8f9}{7}$ {{Local_Points}}, <span class="rainbow-text">$9$ </span> {{Local_Points}}
        * {{Firm_Apple}} **Firm Apple**: $\textcolor{82d68b}{44}$ {{Local_Points}}, $\textcolor{77c8f9}{52}$ {{Local_Points}}, <span class="rainbow-text">$60$ </span> {{Local_Points}}
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: $\textcolor{82d68b}{22}$ {{Local_Points}}, $\textcolor{77c8f9}{26}$ {{Local_Points}}, <span class="rainbow-text">$30$ </span> {{Local_Points}}
        * {{Sticky_Rice}} **Sticky Rice**: $\textcolor{82d68b}{11}$ {{Local_Points}}, $\textcolor{77c8f9}{13}$ {{Local_Points}}, <span class="rainbow-text">$15$ </span> {{Local_Points}}
        * {{Lustful_Grape}} **Lustful Grape**: $\textcolor{82d68b}{77}$ {{Local_Points}}, $\textcolor{77c8f9}{91}$ {{Local_Points}}, <span class="rainbow-text">$105$ </span> {{Local_Points}}
        * {{Venus_Cacao}} **Venus Cacao**: $\textcolor{82d68b}{55}$ {{Local_Points}}, $\textcolor{77c8f9}{65}$ {{Local_Points}}, <span class="rainbow-text">$75$ </span> {{Local_Points}}
        * {{Stamina_Pepper}} **Stamina Pepper**: $\textcolor{82d68b}{66}$ {{Local_Points}}, $\textcolor{77c8f9}{78}$ {{Local_Points}}, <span class="rainbow-text">$90$ </span> {{Local_Points}}
        * {{Cleft_Garlic}} **Cleft Garlic**: $\textcolor{82d68b}{8}$ {{Local_Points}}, $\textcolor{77c8f9}{10}$ {{Local_Points}}, <span class="rainbow-text">$12$ </span> {{Local_Points}}
        * {{Sticky_Melon}} **Sticky Melon**: $\textcolor{82d68b}{88}$ {{Local_Points}}, $\textcolor{77c8f9}{104}$ {{Local_Points}}, <span class="rainbow-text">$120$ </span> {{Local_Points}}
        * {{Pulse_Saffron}} **Pulse Saffron**: $\textcolor{82d68b}{110}$ {{Local_Points}}, $\textcolor{77c8f9}{130}$ {{Local_Points}}, <span class="rainbow-text">$150$ </span> {{Local_Points}}


    ---

    ??? abstract "Crops Rarity Chance"
        * **Farming Skill 1**: $\textcolor{82d68b}{80\%}$, $\textcolor{77c8f9}{19.9\%}$, <span class="rainbow-text">$0.1\%$</span>
        * **Farming Skill 2**: $\textcolor{82d68b}{79\%}$, $\textcolor{77c8f9}{20.8\%}$, <span class="rainbow-text">$0.2\%$</span>
        * **Farming Skill 3**: $\textcolor{82d68b}{78\%}$, $\textcolor{77c8f9}{21.7\%}$, <span class="rainbow-text">$0.3\%$</span>
        * **Farming Skill 4**: $\textcolor{82d68b}{77\%}$, $\textcolor{77c8f9}{22.6\%}$, <span class="rainbow-text">$0.4\%$</span>
        * **Farming Skill 5**: $\textcolor{82d68b}{76\%}$, $\textcolor{77c8f9}{23.5\%}$, <span class="rainbow-text">$0.5\%$</span>
        * **Farming Skill 6**: $\textcolor{82d68b}{75\%}$, $\textcolor{77c8f9}{24.3\%}$, <span class="rainbow-text">$0.7\%$</span>
        * **Farming Skill 7**: $\textcolor{82d68b}{74\%}$, $\textcolor{77c8f9}{25.1\%}$, <span class="rainbow-text">$0.9\%$</span>
        * **Farming Skill 8**: $\textcolor{82d68b}{73\%}$, $\textcolor{77c8f9}{25.9\%}$, <span class="rainbow-text">$1.1\%$</span>
        * **Farming Skill 9**: $\textcolor{82d68b}{72\%}$, $\textcolor{77c8f9}{26.7\%}$, <span class="rainbow-text">$1.3\%$</span>
        * **Farming Skill 10**: $\textcolor{82d68b}{71\%}$, $\textcolor{77c8f9}{27.5\%}$, <span class="rainbow-text">$1.5\%$</span>
        * **Farming Skill 11**: $\textcolor{82d68b}{70\%}$, $\textcolor{77c8f9}{28.3\%}$, <span class="rainbow-text">$1.7\%$</span>
        * **Farming Skill 12**: $\textcolor{82d68b}{69\%}$, $\textcolor{77c8f9}{29.1\%}$, <span class="rainbow-text">$1.9\%$</span>
        * **Farming Skill 13**: $\textcolor{82d68b}{68\%}$, $\textcolor{77c8f9}{30\%}$, <span class="rainbow-text">$2\%$</span>
        * **Farming Skill 14**: $\textcolor{82d68b}{67\%}$, $\textcolor{77c8f9}{30.9\%}$, <span class="rainbow-text">$2.1\%$</span>
        * **Farming Skill 15**: $\textcolor{82d68b}{66\%}$, $\textcolor{77c8f9}{31.7\%}$, <span class="rainbow-text">$2.3\%$</span>
        * **Farming Skill 16**: $\textcolor{82d68b}{65\%}$, $\textcolor{77c8f9}{32.5\%}$, <span class="rainbow-text">$2.5\%$</span>
        * **Farming Skill 17**: $\textcolor{82d68b}{64\%}$, $\textcolor{77c8f9}{33.3\%}$, <span class="rainbow-text">$2.7\%$</span>
        * **Farming Skill 18**: $\textcolor{82d68b}{63\%}$, $\textcolor{77c8f9}{34\%}$, <span class="rainbow-text">$3\%$</span>
        * **Farming Skill 19**: $\textcolor{82d68b}{62\%}$, $\textcolor{77c8f9}{34.5\%}$, <span class="rainbow-text">$3.5\%$</span>
        * **Farming Skill 20**: $\textcolor{82d68b}{61\%}$, $\textcolor{77c8f9}{34.8\%}$, <span class="rainbow-text">$4.2\%$</span>
        * **Farming Skill 21**: $\textcolor{82d68b}{60\%}$, $\textcolor{77c8f9}{35\%}$, <span class="rainbow-text">$5\%$</span>
        * **Farming Skill 22**: $\textcolor{82d68b}{59\%}$, $\textcolor{77c8f9}{35.8\%}$, <span class="rainbow-text">$5.2\%$</span>
        * **Farming Skill 23**: $\textcolor{82d68b}{58\%}$, $\textcolor{77c8f9}{36.5\%}$, <span class="rainbow-text">$5.5\%$</span>
        * **Farming Skill 24**: $\textcolor{82d68b}{57\%}$, $\textcolor{77c8f9}{37.1\%}$, <span class="rainbow-text">$5.9\%$</span>
        * **Farming Skill 25**: $\textcolor{82d68b}{56\%}$, $\textcolor{77c8f9}{37.6\%}$, <span class="rainbow-text">$6.4\%$</span>
        * **Farming Skill 26**: $\textcolor{82d68b}{55\%}$, $\textcolor{77c8f9}{38\%}$, <span class="rainbow-text">$7\%$</span>
        * **Farming Skill 27**: $\textcolor{82d68b}{54\%}$, $\textcolor{77c8f9}{38.3\%}$, <span class="rainbow-text">$7.7\%$</span>
        * **Farming Skill 28**: $\textcolor{82d68b}{53\%}$, $\textcolor{77c8f9}{38.5\%}$, <span class="rainbow-text">$8.5\%$</span>
        * **Farming Skill 29**: $\textcolor{82d68b}{52\%}$, $\textcolor{77c8f9}{38.6\%}$, <span class="rainbow-text">$9.4\%$</span>
        * **Farming Skill 30**: $\textcolor{82d68b}{51\%}$, $\textcolor{77c8f9}{39\%}$, <span class="rainbow-text">$10\%$</span>
        * **Farming Skill 31**: $\textcolor{82d68b}{50\%}$, $\textcolor{77c8f9}{39\%}$, <span class="rainbow-text">$11\%$</span>
    ---

    ??? abstract "Farming EXP"
        * {{Spanking_Wheat}} **Spanking Wheat**: $1$ EXP
        * {{Shapely_Potato}} **Shapely Potato**: $1$ EXP
        * {{Juicy_Onion}} **Juicy Onion**: $2$ EXP
        * {{Virile_Mushroom}} **Virile Mushroom**: $2$ EXP
        * {{Exposed_Corn}} **Exposed Corn**: $15$ EXP
        * {{Twin_Beans}} **Twin Beans**: $3$ EXP
        * {{Firm_Apple}} **Firm Apple**: $20$ EXP
        * {{Curvaceous_Paprika}} **Curvaceous Paprika**: $10$ EXP
        * {{Sticky_Rice}} **Sticky Rice**: $5$ EXP
        * {{Lustful_Grape}} **Lustful Grape**: $33$ EXP
        * {{Venus_Cacao}} **Venus Cacao**: $25$ EXP
        * {{Stamina_Pepper}} **Stamina Pepper**: $30$ EXP
        * {{Cleft_Garlic}} **Cleft Garlic**: $4$ EXP
        * {{Sticky_Melon}} **Sticky Melon**: $36$ EXP
        * {{Pulse_Saffron}} **Pulse Saffron**: $40$ EXP


<!--
* {{Spanking_Wheat}} **Spanking Wheat**
* {{Shapely_Potato}} **Shapely Potato**
* {{Juicy_Onion}} **Juicy Onion**
* {{Virile_Mushroom}} **Virile Mushroom**
* {{Exposed_Corn}} **Exposed Corn**
* {{Twin_Beans}} **Twin Beans**
* {{Firm_Apple}} **Firm Apple**
* {{Curvaceous_Paprika}} **Curvaceous Paprika**
* {{Sticky_Rice}} **Sticky Rice**
* {{Lustful_Grape}} **Lustful Grape**
* {{Venus_Cacao}} **Venus Cacao**
* {{Stamina_Pepper}} **Stamina Pepper**
* {{Cleft_Garlic}} **Cleft Garlic**
* {{Sticky_Melon}} **Sticky Melon**
* {{Pulse_Saffron}} **Pulse Saffron**
-->

### Crops List {.territory-inventory-grid}

{{ crop_tile("Spanking Wheat") }}
{{ crop_tile("Shapely Potato") }}
{{ crop_tile("Shapely Potato") }}
{{ crop_tile("Juicy Onion") }}
{{ crop_tile("Virile Mushroom") }}
{{ crop_tile("Exposed Corn") }}
{{ crop_tile("Twin Beans") }}
{{ crop_tile("Firm Apple") }}
{{ crop_tile("Curvaceous Paprika") }}
{{ crop_tile("Sticky Rice") }}
{{ crop_tile("Lustful Grape") }}
{{ crop_tile("Venus Cacao") }}
{{ crop_tile("Stamina Pepper") }}
{{ crop_tile("Cleft Garlic") }}
{{ crop_tile("Sticky Melon") }}
{{ crop_tile("Pulse Saffron") }}

## Buildings

There are 11 building types, each having its own purpose. Most of the Buildings cost resources to build and take some time to be built.

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

## Dishes

## Missions

## Tools

## Helpers

To earn offline resources, you can hire **Helpers**. To do that, you need to build **Helper Lodging** first.

Recruiting a Helper costs $5000$ {{Local_Points}} **Local Points**.

After you press the "Start Recruiting" button, you will be allowed to choose one of three Helpers to recruit.

??? image "Recruitment Menu"
    ![Helper Recruitment Menu](../assets/images/territory/helper-2.avif)

Each helper has 3 stats:

* **Logging Efficiency**: Amount of trees chopped per 4h.
* **Mining Efficiency**: Amount of ores chopped per 4h.
* **Farming Efficiency**: Amount of items harvested per 1 crop harvested.

Each stat value can vary from 1 to 6, therefore getting the Helper with the highest Efficiency is preferred.

There is a total of $8$ Races:

* **Goblin**
* **Orc**
* **Rabbit Beastfolk**
* **Squirrel Beastfolk**
* **Sheep Beastfolk**
* **Cat Beastfolk**
* **Puppy Beastfolk**
* **Unknown** (Yuridori)

??? example "Technical Details"

    * There are $180$ possible options that can appear during Recruit.

    ---

    * Chance to get **Goblin** or **Orc**: $42\%$ each.
    * Chance to get **Rabbit Beastfolk**, **Sheep Beastfolk**, **Puppy Beastfolk**, **Squirrel Beastfolk**, **Cat Beastfolk**: $3\%$ each.
    * Chance to get **Unknown** (Yuridori): $1\%$.

    ---

    * There is a $40.7296\%$ chance to get at least one Beaskfolk or Yuridori from the selection.

    ---

    * **Squirrel Beastfolk** is the only race that can get **Logging Efficiency** of $6$ (Chance: $0.15\%$).
    * **Sheep Beastfolk** is the only race that can get **Mining Efficiency** of $6$ (Chance: $0.15\%$).
    * **Rabbit Beastfolk** is the only race that can get **Farming Efficiency** of $6$ (Chance: $0.15\%$).

    ---

    * **Cat Beastfolk** and **Unknown** (Yuridori) races have the best average Efficiency but both have a maximum value of $5$.

Upon recruiting a Helper, you can assign them to do one task. If the task is Farming, you can choose the crop to grow as well.

You can also **Rename**, **Replace** them or **Terminate the Contract** with them, essentially deleting the Helper.
??? image "Manage Helper Menu"
    ![Manage Helper Menu](../assets/images/territory/helper-3.avif)

Resources gathered by Helpers are stored automatically with no player involvement. They have a cap of 24h, similar to **Diner Sales** or **Fish Trap**.

To gather earned resources, press the **Business Management** in the main menu.

??? image "Image Guide"
    ![Collecting Resources from Helpers](../assets/images/territory/helper-idle.avif)


# WORK IN PROGRESS