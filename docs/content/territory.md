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

Logging is done via **Logging Site**. It is main source of {{Wooden_Branch}} **Wooden Branches**, {{Lumber}} **Lumber** and {{Sturdy_Lumber}} **Sturdy Lumber**. To obtain them, you must chop down a **tree** using the **Axe**.

Each tree has 3 stages of growth, with more grown version providing **more resources** and **Logging EXP** but **longer to chop down**.

Therefore, you should **always** chop down only the most grown trees to obtain the biggest amount of resources.

??? image "Different Growth Stages"
    ![Different Growth Stages Image](../assets/images/territory/logging-1.avif)

??? example "Technical Details"

    * Logging site is $3x3$ field, resulting in possible $9$ trees growing at the same time.
    * Whenever any tile is empty, Logging Site will grow **one Stage 1** tree in $\bf{60}$ **seconds**. Therefore, if you cropped all trees, it will take $9$ minutes to replant them completely.
    * Tree needs $\bf{120}$ seconds to grow into the Stage 2 and $\bf{180}$ seconds to grow into the Stage 3, therefore, it takes $\bf{5}$ **minutes** to get fully grown tree after it appeared initially.
    * **Stage 1** has $\bf{20}$ "health", **Stage 2** has $\bf{29}$ "health" and **Stage 3** has $\bf{38}$, respectively. Health determines how hard it is to destroy the tree, resulting in different amount of hits depending on your progression.

    ---

    * **Resources dropped:**
        * **Stage 1:** $3$ {{Wooden_Branch}} **Wooden Branches**
        * **Stage 2:** $2$ {{Wooden_Branch}} **Wooden Branches**, $3$ {{Lumber}} **Lumber**
        * **Stage 3:** $2$ {{Wooden_Branch}} **Wooden Branches**, $3$ {{Lumber}} **Lumber** and $1$ {{Sturdy_Lumber}} **Sturdy Lumber**

    ---

    * **Logging EXP awarded:**
        * **Stage 1:** $1$ EXP
        * **Stage 2:** $2$ EXP
        * **Stage 3:** $4$ EXP

### Mining

Mining is done via **Quarry**. It is a main source of {{Rock}} **Rock**, {{Copper_Ore_T}} **Copper Ore**, {{Iron_Ore_T}} **Iron Ore**, {{Silver_Ore_T}} **Silver Ore** and {{Gold_Ore_T}} **Gold Ore**. To obtain them, you must mine the clusters with a **Pickaxe**.

Ores have different chance to appear but, unlike trees, they have no growth, therefore can be mined immediately as they are generated. 

??? image "Different Ore Clusters Showcase"
    ![Different Ore Clusters Showcase](../assets/images/territory/mining-1.avif)

??? example "Technical Details"

    * Similar to the Logging site, Quarry is $3x3$ field, resulting in possible $9$ clusters being there at the same time. The positioning isn't fixed in place, however, therefore clusters are spawned randomly within the Quarry.
    * Whenever there are less than 9 ore clusters at the given moment, Quarry will generate 1 cluster in $\bf{60}$ **seconds**. Therefore, if you mined all clusters, it will take $9$ minutes to fill the Quarry again.

    ---

    * **Clusters spawn chance:**
        * {{Rock}} **Rock Cluster:** $30\%$
        * {{Copper_Ore_T}} **Copper Cluster:** $20\%$
        * {{Iron_Ore_T}} **Iron Cluster:** $25\%$
        * {{Silver_Ore_T}} **Silver Cluster:** $15\%$
        * {{Gold_Ore_T}} **Gold Cluster:** $10\%$

    ---

    * **Clusters Health:**
        * {{Rock}} **Rock Cluster:** $20$
        * {{Copper_Ore_T}} **Copper Cluster:** $30$
        * {{Iron_Ore_T}} **Iron Cluster:** $25$
        * {{Silver_Ore_T}} **Silver Cluster:** $34$
        * {{Gold_Ore_T}} **Gold Cluster:** $38$

    ---

    * **Resources dropped:**
        * {{Rock}} **Rock Cluster:** $4$ {{Rock}} **Rock**
        * {{Copper_Ore_T}} **Copper Cluster:** $2$ {{Rock}} **Rock**, $2$ {{Copper_Ore_T}} **Copper Ore**
        * {{Iron_Ore_T}} **Iron Cluster:** $2$ {{Rock}} **Rock**, $2$ {{Iron_Ore_T}} **Iron Ore**
        * {{Silver_Ore_T}} **Silver Cluster:** $2$ {{Rock}} **Rock**, $2$ {{Silver_Ore_T}} **Silver Ore**
        * {{Gold_Ore_T}} **Gold Cluster:** $2$ {{Rock}} **Rock**, $1$ {{Gold_Ore_T}} **Gold Ore**

    ---

    * **Mining EXP awarded:**
        * {{Rock}} **Rock Cluster:** $2$ EXP
        * {{Copper_Ore_T}} **Copper Cluster:** $3$ EXP
        * {{Iron_Ore_T}} **Iron Cluster:** $4$ EXP
        * {{Silver_Ore_T}} **Silver Cluster:** $5$ EXP
        * {{Gold_Ore_T}} **Gold Cluster:** $6$ EXP

### Farming

Farming is done via **Fields**. It is main source of **Crops**, that can be turned into dishes with the help of **Cooking Pot**. To gather crops, you need to use a **Scythe**.

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

Each stat value can vary from 1 to 6, therefore getting Helper with the highest Efficiency is preferred.

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

    * There are $181$ possible options that can appear during Recruit.

    ---

    * Chance to get **Goblin** or **Orc**: $42\%$ each.
    * Chance to get **Rabbit Beastfolk**, **Sheep Beastfolk**, **Puppy Beastfolk**, **Squirrel Beastfolk**, **Cat Beastolk**: $3\%$ each.
    * Chance to get **Unknown** (Yuridori): $1\%$.

    ---

    * There is $40.7296\%$ chance to get at least one Beaskfolk or Yuridori from selection.

    ---

    * **Squirrel Beastfolk** is the only race that can get **Logging Efficiency** of $6$ (Chance: $0.15\%$).
    * **Sheep Beastfolk** is the only race that can get **Mining Efficiency** of $6$ (Chance: $0.15\%$).
    * **Rabbit Beastfolk** is the only race that can get **Farming Efficiency** of $6$ (Chance: $0.15\%$).

    ---

    * **Cat Beastfolk** and **Unknown** (Yuridori) races have the best average Efficiency but both have maximum value of $5$.

Upon recruiting a Helper, you can assign them to do one task. If the task is Farming, you can choose the crop to grow as well.

You can also **Rename**, **Replace** them or **Terminate Contract** with them, essentially deleting the Helper.
??? image "Manage Helper Menu"
    ![Manage Helper Menu](../assets/images/territory/helper-3.avif)

Resources gathered by Helpers are stored automatically with no player involvement. They have cap of 24h, similar to **Diner Sales** or **Fish Trap**.

To gather earned resources, press the **Business Management** in the main menu.

??? image "Image Guide"
    ![Collecting Resources from Helpers](../assets/images/territory/helper-idle.avif)


# WORK IN PROGRESS