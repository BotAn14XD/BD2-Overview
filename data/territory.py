# ---------------------------------  MATERIALS  --------------------------------- #

MATERIALS_DB = {
    "Rock": "assets/images/territory/icons/icon_life_item_consumption_001.avif",
    "Copper Ore": "assets/images/territory/icons/icon_life_item_consumption_002.avif",
    "Iron Ore": "assets/images/territory/icons/icon_life_item_consumption_003.avif",
    "Silver Ore": "assets/images/territory/icons/icon_life_item_consumption_004.avif",
    "Gold Ore": "assets/images/territory/icons/icon_life_item_consumption_005.avif",
    "Wooden Branch": "assets/images/territory/icons/icon_life_item_consumption_006.avif",
    "Lumber": "assets/images/territory/icons/icon_life_item_consumption_007.avif",
    "Sturdy Lumber": "assets/images/territory/icons/icon_life_item_consumption_008.avif"
    }

# ---------------------------------  BUILDINGS  --------------------------------- #

TERRITORY_DB = {
    "Home": {
        "icon": "assets/images/territory/icons/icon_life_object_building_004.avif",
        "limit": "1",
        "usage": "Main Building",
        "time": "",
        "cost": "",
        "bonus": "",
        "desc": "A private retreat where you can rest and recharge. Furnished with cozy decor and items of personal value, this space serves as the control hub of everything that goes on in your territory."
    },
    "Cooking Pot": {
        "icon": "assets/images/territory/icons/icon_life_object_building_001.avif",
        "limit": "1",
        "usage": "Cooking",
        "cost": {
        "Rock": 10,
        "Wooden Branch": 10
    },
        "desc": "Fierce flames lick the base of a massive iron cauldron, as countless ingredients swirl together inside, giving off a rich fragrance."
    },
    "Workbench": {
        "icon": "assets/images/territory/icons/icon_life_object_building_002.avif",
        "limit": "1",
        "usage": "Crafting",
        "desc": "A heavy wooden workbench bearing the marks of frequent use, equipped with various crafting tools. A wide range of everyday items can be refined and assembled here."
    },
    "Helper Lodging":{
        "icon": "assets/images/territory/icons/icon_life_object_building_003.avif",
        "limit": "5",
        "usage": "",
        "cost":{
        "Iron Ore": 40,
        "Copper Ore": 20,
        "Lumber": 120
        },
        "time": "12 hours",
        "desc": "A cozy cottage that retains heat with its roof of soft, leafy layers. A perfect retreat after a day of hard labor."
    },
    "Resident Mansion":{
        "icon": "assets/images/territory/icons/icon_life_object_building_004.avif",
        "limit": "5",
        "usage": "",
        "cost":{
        "Rock": 40,
        "Copper Ore": 15,
        "Lumber": 40,
        "Sturdy Lumber": 40,
        },
        "time": "15 minutes",
        "desc": "A luxury residence featuring an ornate roof and large windows. Built for those who call your Territory home, it boasts a spacious interior and a solid structure."
    },
    "Pub":{
        "icon": "assets/images/territory/icons/icon_life_object_building_005.avif",
        "limit": "1",
        "usage": "",
        "cost":{
        "Rock": 100,
        "Copper Ore": 40,
        "Iron Ore": 20,
        "Lumber": 120,
        },
        "time": "8 hours",
        "desc": "A breezy, bar-style tavern. A lively place for grabbing a drink and getting the latest scoop on your Territory.",
        "bonus": "+1 Lumber Bonus"
    },
    "Warehouse":{
        "icon": "assets/images/territory/icons/icon_life_object_building_006.avif",
        "limit": "1",
        "usage": "",
        "cost":{
        "Rock": 100,
        "Copper Ore": 40,
        "Iron Ore": 20,
        "Lumber": 120,
        },
        "time": "8 hours",
        "desc": "A standard wooden building reinforced with thick planks and nails for heavy-duty storage. Safely houses harvested resources and supplies against external threats.",
        "bonus": "+1 Mineral Bonus"
    },
    "Field":{
        "icon": "assets/images/territory/icons/icon_life_object_building_007.avif",
        "limit": "100",
        "usage": "",
        "cost":{
        "Rock": 5,
        "Wooden Branch": 5,
        "Lumber": 3,
        },
        "time": "",
        "desc": "A plot of farmland with fertile soil, carefully leveled and tilled. Rich in nutrients, it provides everything seeds need to take root and grow into strangely shaped crops.",
    },
    "Logging Site":{
        "icon": "assets/images/territory/icons/icon_life_object_building_008.avif",
        "limit": "2",
        "usage": "",
        "cost":{
        "Sturdy Lumber":120,
        "Iron Ore":50,
        "Silver Ore":40,
        "Gold Ore":15,
        },
        "time": "24 hours",
        "desc": "A dense woodland where thick trees grow without end. New shoots spring up wherever a tree is felled, steadily supplying the local demand for timber.",
    },
    "Quarry":{
        "icon": "assets/images/territory/icons/icon_life_object_building_009.avif",
        "limit": "2",
        "usage": "",
        "cost":{
        "Lumber": 300,
        "Iron Ore": 50,
        "Silver Ore": 50,
        "Gold Ore": 15,
        },
        "time": "24 hours",
        "desc": "A rugged rock formation where massive boulders have broken through and risen above the surface. Solid ore veins periodically emerge throughout the area.",
    },
    "Forge":{
        "icon": "assets/images/territory/icons/icon_life_object_building_010.avif",
        "limit": "1",
        "usage": "",
        "cost":{
        "Rock": 15,
        "Wooden Branch": 15,
        "Lumber": 15,
        },
        "time": "",
        "desc": "A forge where red molten metal flows ceaselessly from a massive furnace. Fully equipped with all manner of facilities, it is the ideal place for enhancing tools of every kind.",
    },
}

# ---------------------------------  CROPS  --------------------------------- #

CROPS_DB = {
    "Spanking Wheat": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_001.avif",
        "unlock_level": 1,
        "seed_cost": 1,
        "growth_time": "5 Minutes",
        "exp": 1,
        "sell_price": [1, 1, 2],
        "desc": "A grain crop whose slender, elongated ears droop from the tips of their stalks, bending in a whip-like curve. When beaded with dew, they sway even more fluidly and take on a smooth sheen."
    },
    "Shapely Potato": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_002.avif",
        "unlock_level": 1,
        "seed_cost": 1,
        "growth_time": "1 Minute",
        "exp": 1,
        "sell_price": [1, 1, 1],
        "desc": "A root crop with a deep central cleft, split into a form uncannily reminiscent of rounded buttocks. The smooth curves revealed when the soil is brushed away invite no shortage of curious imaginings."
    },
    "Juicy Onion": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_003.avif",
        "unlock_level": 2,
        "seed_cost": 2,
        "growth_time": "10 Minutes",
        "exp": 2,
        "sell_price": [2, 2, 3],
        "desc": "A vegetable consisting of white inner flesh cleft into two halves, from which a transparent, viscous fluid endlessly oozes. Its many layers grow increasingly moist the more they are touched."
    },
    "Virile Mushroom": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_004.avif",
        "unlock_level": 2,
        "seed_cost": 3,
        "growth_time": "15 Minutes",
        "exp": 2,
        "sell_price": [3, 3, 4],
        "desc": "A fungus featuring a thick, smooth head atop a sturdy stalk. Beneath the cap, the reddish stem is marked by protruding, vein-like ridges."
    },
    "Exposed Corn": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_005.avif",
        "unlock_level": 5,
        "seed_cost": 30,
        "growth_time": "5 Hours",
        "exp": 15,
        "sell_price": [33, 39, 45],
        "desc": "A crop with rows of yellow kernels studded beneath long, drooping silk, taking a form reminiscent of a woman's curved figure. The more the husk is peeled back, the more nakedly its luscious form is revealed."
    },
    "Twin Beans": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_006.avif",
        "unlock_level": 3,
        "seed_cost": 6,
        "growth_time": "30 Minutes",
        "exp": 3,
        "sell_price": [6, 7, 9],
        "desc": "A pod in which two gently rounded beans, their shape evocative of a full bust, nestle snugly together within a thin shell. The pod, swollen taut as if about to burst, makes for quite the tantalizing sight."
    },
    "Firm Apple": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_007.avif",
        "unlock_level": 5,
        "seed_cost": 40,
        "growth_time": "8 Hours",
        "exp": 20,
        "sell_price": [44, 52, 60],
        "desc": "A fruit with a deep, soft groove running toward the center, evoking the rounded curves of a pair of buttocks. Its surface, flushed a deep red, is taut and firm to the touch—as if it might burst at any moment."
    },
    "Curvaceous Paprika": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_008.avif",
        "unlock_level": 4,
        "seed_cost": 20,
        "growth_time": "3 Hours",
        "exp": 10,
        "sell_price": [22, 26, 30],
        "desc": "A vegetable that consists of a smooth, leather-like peel over an empty space that resembles the voluptuous body of a woman. Cutting it in half reveals its sensual silhouette."
    },
    "Sticky Rice": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_009.avif",
        "unlock_level": 4,
        "seed_cost": 10,
        "growth_time": "1 Hour",
        "exp": 5,
        "sell_price": [11, 13, 15],
        "desc": "A grain with a slender tail at the tip of every kernel. Beneath the husk, the grains are remarkably white and possess a slippery, sticky quality."
    },
    "Lustful Grape": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_010.avif",
        "unlock_level": 8,
        "seed_cost": 70,
        "growth_time": "15 Hours",
        "exp": 33,
        "sell_price": [77, 91, 105],
        "desc": "A fruit where each grape takes the form of a perky breast. Each grape differs in size and shape."
    },
    "Venus Cacao": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_011.avif",
        "unlock_level": 6,
        "seed_cost": 50,
        "growth_time": "10 Hours",
        "exp": 25,
        "sell_price": [55, 65, 75],
        "desc": "A berry that consists of a coarse shell and a moist inner flesh. Breaking the shell open by force will reveal the hot and sticky seeds inside."
    },
    "Stamina Pepper": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_012.avif",
        "unlock_level": 7,
        "seed_cost": 60,
        "growth_time": "12 Hours",
        "exp": 30,
        "sell_price": [66, 78, 90],
        "desc": "A vegetable with a bluntly swollen tip and vivid vein-like lines tracing its surface. An intense heat emanates from its rigidly upright form."
    },
    "Cleft Garlic": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_013.avif",
        "unlock_level": 3,
        "seed_cost": 8,
        "growth_time": "45 Minutes",
        "exp": 4,
        "sell_price": [8, 10, 12],
        "desc": "A root vegetable with a thin skin that, once peeled, reveals a pair of white mounds. Its piquant aroma and smooth, supple flesh take on a provocative form that stimulates the imagination."
    },
    "Sticky Melon": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_014.avif",
        "unlock_level": 8,
        "seed_cost": 80,
        "growth_time": "18 Hours",
        "exp": 36,
        "sell_price": [88, 104, 120],
        "desc": "A round fruit with a hard shell, the crack from which oozes a sticky, white fluid. Squeezing the fruity flesh causes even more viscous liquids to seep from the fruit, wetting the floor."
    },
    "Pulse Saffron": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_015.avif",
        "unlock_level": 8,
        "seed_cost": 100,
        "growth_time": "20 Hours",
        "exp": 40,
        "sell_price": [110, 130, 150],
        "desc": "A flower with moist, red stamens that stretch out like tongues between its purple petals. When touched, the way they recoil makes the flower seem almost like a living creature."
    }
    }

# ---------------------------------  DISHES  --------------------------------- #

DISHES_DB = {
    "Virile Gnocchi": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_003.avif",
        "unlock_level": 1,
        "sell_price": 44,
        "bonus": "Logging Skill +8 | 10m",
        "ingredients": {
            "Shapely Potato": 5,
            "Spanking Wheat": 3,
            "Virile Mushroom": 2
        },
        "desc": "A dish where thick mushrooms are laid as if nestled atop soft gnocchi, each piece indented with a gentle hollow at its center. The tender, yielding flesh of the gnocchi and the firm texture of the mushroom meld together in a hot sauce, creating a strangely satisfying sense of unity."
    },
    "Bulbous Crepe": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_013.avif",
        "unlock_level": 2,
        "sell_price": 57,
        "bonus": "Mining Skill +8 | 10m",
        "ingredients": {
            "Spanking Wheat": 5,
            "Juicy Onion": 3,
            "Virile Mushroom": 2
        },
        "desc": "A dish featuring a dried, bulbous mushroom peeking its cap out of a smooth, thin layer of buckwheat crepe. The silhouette of the fungal head penetrating the slick membrane is a sight to behold."
    },
    "Creamy Congee": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_004.avif",
        "unlock_level": 3,
        "sell_price": 213,
        "bonus": "Farming Skill +1 | 10m",
        "ingredients": {
            "Sticky Rice": 5,
            "Cleft Garlic": 5,
            "Twin Beans": 3
        },
        "desc": "A dish featuring thick, white congee oozing between two garlic cloves that protrude like a pair of exposed breasts. The savory richness of the beans mingles with the sticky texture to create a titillating flavor profile."
    },
    "Curvaceous Fried Rice": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_002.avif",
        "unlock_level": 4,
        "sell_price": 460,
        "bonus": ["Logging Skill +10 | 10m", "Mining Skill +10 | 10m"],
        "ingredients": {
            "Sticky Rice": 10,
            "Juicy Onion": 10,
            "Curvaceous Paprika": 5
        },
        "desc": "Two lumps of fried rice placed side-by-side on an elongated plate. Finely sliced vegetables have been sprinkled over the perky curvature of the mounds, making for a tantalizing sight."
    },
    "Milky Steak": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_006.avif",
        "unlock_level": 5,
        "sell_price": 714,
        "bonus": "Farming Skill +1 | 10m",
        "ingredients": {
            "Exposed Corn": 12,
            "Twin Beans": 8,
            "Juicy Onion": 10
        },
        "desc": "A hot, white sauce spurts out from between multiple layers of patties. As the milky white sauce seeps out from the creases of the succulent meat, it leaves behind a suggestive trace."
    },
    "Venus Pudding": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_009.avif",
        "unlock_level": 6,
        "sell_price": 926,
        "bonus": ["Logging Skill +14 | 10m", "Mining Skill +14 | 10m", "Farming Skill +1 | 10m"],
        "ingredients": {
            "Venus Cacao": 6,
            "Exposed Corn": 12,
        },
        "desc": "A jiggling plate of cacao pudding. The pudding trembles with every touch, evoking the seductive sight of tender flesh."
    },
    "Stamina Pasta": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_001.avif",
        "unlock_level": 7,
        "sell_price": 1395,
        "bonus": ["Mineral Bonus +1 | 10m"],
        "ingredients": {
            "Spanking Wheat": 15,
            "Cleft Garlic": 5,
            "Stamina Pepper": 15,
        },
        "desc": "A dish where pasta noodles wrap tightly around a stiff, upright Stamina Pepper in a seamless cylindrical form. The oily curves of the glistening noodles and the bold silhouette of the chili create a strangely captivating tension."
    },
    "Hormone Glass Noodles": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_005.avif",
        "unlock_level": 7,
        "sell_price": 1605,
        "bonus": ["Lumber Bonus +1 | 10m"],
        "ingredients": {
            "Virile Mushroom": 15,
            "Stamina Pepper": 15,
            "Curvaceous Paprika": 10
        },
        "desc": "A dish featuring a smattering of chili peppers and bulbous mushrooms over vermicelli noodles. The vegetables, tangled together in an oily heap, seem to evoke an image of lust."
    },
    "Lingerie Cookie": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_012.avif",
        "unlock_level": 7,
        "sell_price": 1665,
        "bonus": ["Crops Bonus +1 | 10m"],
        "ingredients": {
            "Spanking Wheat": 15,
            "Venus Cacao": 10,
            "Stamina Pepper": 10
        },
        "desc": "A cookie with an icing flourish in the shape of lace underwear. There's something pleasing about the smooth finish of the sugar coating against the crisp texture of the biscuit."
    },
    "Apple Tea": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_010.avif",
        "unlock_level": 8,
        "sell_price": 1810,
        "bonus": ["Logging Skill +16 | 10m", "Lumber Bonus +1 | 10m"],
        "ingredients": {
            "Firm Apple": 15,
            "Lustful Grape": 10,
        },
        "desc": "A drink featuring large slices of apple over a cup of tea. From above, it almost looks as though a figure is swimming through the crimson brew."
    },
    "Nude Salad": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_008.avif",
        "unlock_level": 8,
        "sell_price": 1810,
        "bonus": ["Mining Skill +16 | 10m", "Mineral Bonus +1 | 10m"],
        "ingredients": {
            "Firm Apple": 15,
            "Lustful Grape": 5,
            "Sticky Melon": 5,
        },
        "desc": "A dish consisting of an opaque, white sauce poured over curvaceous grapes and melon slices. The sight of the sticky sauce running down the smooth surface of the fruit evokes explicit fantasies."
    },
    "Lustful Tart": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_011.avif",
        "unlock_level": 8,
        "sell_price": 2220,
        "bonus": ["Farming Skill +2 | 10m", "Crop Bonus +1 | 10m"],
        "ingredients": {
            "Spanking Wheat": 20,
            "Sticky Melon": 10,
            "Lustful Grape": 10
        },
        "desc": "A tart topped with a variety of round fruit. The sticky, transparent syrup coating gives off a tantalizing sheen."
    },
    "Libido Soup": {
        "icon": "assets/images/territory/icons/icon_life_item_dish_007.avif",
        "unlock_level": 8,
        "sell_price": 2640,
        "bonus": ["Mineral Bonus +1 | 10m", "Lumber Bonus +1 | 10m", "Crop Bonus +1 | 10m"],
        "ingredients": {
            "Shapely Potato": 40,
            "Pulse Saffron": 20
        },
        "desc": "A creamy soup with the delicate scent of saffron. Each stir sends white silhouettes into dizzying swirls, leaving behind a lingering, sensual trail."
    }
}

# ---------------------------------  TOOLS  --------------------------------- #

TOOLS_DB = {
    "Stone Pickaxe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_001.avif",
        "level": 1,
        "local_points": "-",
        "stats": [
            "Mining Skill: 10"
        ],
        "materials": {
        }
    },
    "Copper Pickaxe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_002.avif",
        "level": 2,
        "local_points": 300,
        "stats": [
            "Mining Skill: 21"
        ],
        "materials": {
            "Copper Ore": 8,
            "Lumber": 20
        }
    },
    "Silver Pickaxe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_003.avif",
        "level": 3,
        "local_points": 5000,
        "stats": [
            "Mining Skill: 67",
            "Mineral Bonus: 1"
        ],
        "materials": {
            "Iron Ore": 50,
            "Silver Ore": 40,
            "Lumber": 200,
            "Sturdy Lumber": 40
        }
    },
    "Gold Pickaxe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_004.avif",
        "level": 4,
        "local_points": 30000,
        "stats": [
            "Mining Skill: 100",
            "Mineral Bonus: 2"
        ],
        "materials": {
            "Iron Ore": 150,
            "Gold Ore": 60,
            "Lumber": 600,
            "Sturdy Lumber": 200
        }
    },
    "Stone Axe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_005.avif",
        "level": 1,
        "local_points": "-",
        "stats": [
            "Logging Skill: 10"
        ],
        "materials": {
        }
    },
    "Copper Axe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_006.avif",
        "level": 2,
        "local_points": 300,
        "stats": [
            "Logging Skill: 21"
        ],
        "materials": {
            "Copper Ore": 8,
            "Lumber": 20
        }
    },
    "Silver Axe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_007.avif",
        "level": 3,
        "local_points": 5000,
        "stats": [
            "Logging Skill: 67",
            "Lumber Bonus: 1"
        ],
        "materials": {
            "Iron Ore": 50,
            "Silver Ore": 40,
            "Lumber": 200,
            "Sturdy Lumber": 40
        }
    },
    "Gold Axe": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_008.avif",
        "level": 4,
        "local_points": 30000,
        "stats": [
            "Logging Skill: 100",
            "Lumber Bonus: 2"
        ],
        "materials": {
            "Iron Ore": 150,
            "Gold Ore": 60,
            "Lumber": 600,
            "Sturdy Lumber": 200
        }
    },
    "Stone Sickle": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_009.avif",
        "level": 1,
        "local_points": "-",
        "stats": [
            "Farming Skill: 2",
            "Simultaneous Harvesting Capacity: 2"
        ],
        "materials": {
        }
    },
    "Copper Sickle": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_010.avif",
        "level": 2,
        "local_points": 300,
        "stats": [
            "Farming Skill: 5",
            "Simultaneous Harvesting Capacity: 3"
        ],
        "materials": {
            "Copper Ore": 8,
            "Lumber": 20
        }
    },
    "Silver Sickle": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_011.avif",
        "level": 3,
        "local_points": 5000,
        "stats": [
            "Farming Skill: 10",
            "Simultaneous Harvesting Capacity: 4"
        ],
        "materials": {
            "Iron Ore": 50,
            "Silver Ore": 40,
            "Lumber": 200,
            "Sturdy Lumber": 40
        }
    },
    "Gold Sickle": {
        "icon": "assets/images/territory/icons/icon_life_item_tool_012.avif",
        "level": 4,
        "local_points": 30000,
        "stats": [
            "Farming Skill: 15",
            "Simultaneous Harvesting Capacity: 5"
        ],
        "materials": {
            "Iron Ore": 150,
            "Gold Ore": 60,
            "Lumber": 600,
            "Sturdy Lumber": 200
        }
    }
}