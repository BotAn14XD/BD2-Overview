from ast import For
import json
import re

def define_env(env):

    prefix = "/BD2-Overview/"

    @env.macro
    def time(t):
        return f'<span class="local-time" data-utc="{t.strip()}">{t.strip()} UTC</span>'

    @env.macro
    def redirect_btn(target_page, button_text, color="#2196f3"):
        is_external = target_page.startswith("http://") or target_page.startswith("https://")
        
        href_target = target_page if is_external else f"/BD2-Overview/{target_page}"
        tab_behavior = 'target="_blank" rel="noopener noreferrer"' if is_external else ''

        style_override = """
        <style>
            .no-ext-icon::after { display: none !important; }
        </style>
        """ if is_external else ""

        payload = f"""
        <div style="margin-top: 10px; margin-bottom: 5px; width: 100%;">
            {style_override}
            <a href="{href_target}" {tab_behavior} class="no-ext-icon" style="display: block; text-align: center; background-color: transparent; color: #90a4ae; padding: 10px; border-radius: 4px; font-weight: bold; text-decoration: none; font-size: 1.1em; border: 1px solid #2e384d; transition: all 0.2s ease-in-out; user-select: none;" onmouseover="this.style.color='#ffffff'; this.style.backgroundColor='#1a233a'; this.style.borderColor='{color}';" onmouseout="this.style.color='#90a4ae'; this.style.backgroundColor='transparent'; this.style.borderColor='#2e384d';">
                {button_text} &rarr;
            </a>
        </div>
        """
        return payload.replace("\n", "").strip()
    
    
    @env.macro
    def share_btn(anchor_id):
        payload = f"""
        <span id="{anchor_id}"></span>
        <span style="float: right; margin-right: 25px; position: relative; z-index: 2; line-height: 1;" onclick="event.stopPropagation();">
            <input type="button" 
                   value="Copy Share Link" 
                   onclick="navigator.clipboard.writeText('https://botan14xd.github.io/BD2-Overview/FAQ/#{anchor_id}'); this.value='Copied!'; this.style.color='#4caf50'; this.style.backgroundColor='#11291b'; this.style.borderColor='#4caf50'; setTimeout(()=>{{this.value='Copy Share Link'; this.style.color='#90a4ae'; this.style.backgroundColor='#1e2638'; this.style.borderColor='#2e384d'}}, 2000);" 
                   style="all: unset; display: inline-block; white-space: nowrap; color: #90a4ae; font-size: 0.9em; font-weight: bold; cursor: pointer; background: #1e2638; padding: 4px 12px; border-radius: 4px; border: 1px solid #2e384d; transition: all 0.2s ease-in-out; user-select: none; box-sizing: border-box; vertical-align: middle;" 
                   onmouseover="if(this.value==='Copy Share Link'){{this.style.color='#ffffff'; this.style.backgroundColor='#2a354d'; this.style.borderColor='#4f5d75';}}" 
                   onmouseout="if(this.value==='Copy Share Link'){{this.style.color='#90a4ae'; this.style.backgroundColor='#1e2638'; this.style.borderColor='#2e384d';}}">
        </span>
        """
        return payload.replace("\n", "").strip()

    images = {
        "S1_Ability_S_Book": ["assets/images/icons/icon_resource901_49.png", "★1 Ability S. Book"],
        "S1_Rank_up_Star": ["assets/images/icons/icon_resource7780_58.png", "★1 Rank-up Star"],
        "S2_Ability_S_Book": ["assets/images/icons/icon_resource906_50.png", "★2 Ability S. Book"],
        "S2_Rank_up_Star": ["assets/images/icons/icon_resource7781_65.png", "★2 Rank-up Star"],
        "S3_Ability_S_Book": ["assets/images/icons/icon_resource907_51.png", "★3 Ability S. Book"],
        "S3_R_Contract": ["assets/images/icons/icon_resource40003_105.png", "★3 R. Contract"],
        "S3_Rank_up_Star": ["assets/images/icons/icon_resource7782_66.png", "★3 Rank-up Star"],
        "S4_Ability_S_Book": ["assets/images/icons/icon_resource910_54.png", "★4 Ability S. Book"],
        "S4_R_Contract": ["assets/images/icons/icon_resource40004_106.png", "★4 R. Contract"],
        "S4_Rank_up_Star": ["assets/images/icons/icon_resource7783_67.png", "★4 Rank-up Star"],
        "S5_R_Contract": ["assets/images/icons/icon_resource40005_107.png", "★5 R. Contract"],
        "Ability_Pill": ["assets/images/icons/ability_pill.png", "Ability Pill"],
        "Accessory": ["assets/images/gear-system/icons/popupicon_equip4.avif", "Accessory"],
        "Ancient_Crystal": ["assets/images/icons/icon_resource603_76.png", "Ancient Crystal"],
        "Armor": ["assets/images/gear-system/icons/popupicon_equip2.avif", "Armor"],
        "ATK": ["assets/images/gear-system/icons/icon_stats_physical_l.avif", "ATK"],
        "Aurum_Coin": ["assets/images/icons/icon_resource170001_326.png", "Aurum Coin"],
        "Awakening_Elixir": ["assets/images/icons/icon_resource20023_223.png", "Awakening Elixir"],
        "Bag": ["assets/images/icons/icon_bag.avif", "Bag"],
        "Blood_Cocktail": ["assets/images/icons/icon_resource60009_92.png", "Blood Cocktail"],
        "Blue_Slime": ["assets/images/icons/icon_resource9002_60.png", "Blue Slime"],
        "Charming_Gaze": ["assets/images/gear-system/icons/icon_equipment4506_90.avif", "Charming Gaze"],
        "Cleft_Garlic": ["assets/images/territory/icons/icon_life_item_crop_013.avif", "Cleft Garlic"],
        "Coal": ["assets/images/icons/icon_resource214_35.png", "Coal"],
        "Cooked_Rice": ["assets/images/icons/cooked_rice.png", "Cooked Rice"],
        "Copper_Ore": ["assets/images/icons/icon_resource202_28.png", "Copper Ore"],
        "Copper_Ore_T": ["assets/images/territory/icons/icon_life_item_consumption_002.avif", "Copper Ore"],
        "Costumes": ["assets/images/icons/icon_pictorialbook7.png", "Costumes"],
        "CritDMG": ["assets/images/gear-system/icons/icon_stats_criticalhit_l.avif", "Critical DMG"],
        "CritRate": ["assets/images/gear-system/icons/icon_stats_critical_l.avif", "Critical Rate"],
        "Crown_of_Galaxy": ["assets/images/gear-system/icons/icon_equipment4406_72.avif", "Crown of Galaxy"],
        "Curvaceous_Paprika": ["assets/images/territory/icons/icon_life_item_crop_008.avif", "Curvaceous Paprika"],
        "Darkness": ["assets/images/battle-system/icons/elementicon5_5.avif", "Darkness Property"],
        "Darkness_Magic_Crystal": ["assets/images/icons/icon_resource115_19.png", "Darkness Magic Crystal"],
        "Dia": ["assets/images/icons/icon_resource60001_84.png", "Dia"],
        "Deaths_Shroud": ["assets/images/gear-system/icons/icon_equipment4305_77.avif", "Death's Shroud"],
        "Deco_Coin": ["assets/images/icons/icon_resource180001_349.png", "Deco Coin"],
        "DEF": ["assets/images/gear-system/icons/icon_stats_physicaldef_l.avif", "DEF"],
        "Demons_Forbidden_Book": ["assets/images/gear-system/icons/icon_equipment4106_66.avif", "Demon's Forbidden Book"],
        "Devil_Coin": ["assets/images/icons/devil_coin.png", "Devil Coin"],
        "Dragon_Scales_Protection": ["assets/images/gear-system/icons/icon_equipment4205_83.avif", "Dragon's Scale Protection"],
        "Draw_Ticket": ["assets/images/icons/icon_resource40002_79.png", "Draw Ticket"],
        "Engraving_Scroll": ["assets/images/icons/icon_resource701_219.png", "Engraving Scroll"],
        "Essence_of_Life": ["assets/images/icons/icon_resource702_220.png", "Essence of Life"],
        "Essence_of_Perseverance": ["assets/images/icons/icon_resource704_222.png", "Essence of Perseverance"],
        "Essence_of_Strength": ["assets/images/icons/icon_resource703_221.png", "Essence of Strength"],
        "Evil_Dragons_Blade": ["assets/images/gear-system/icons/icon_equipment4101_61.avif", "Evil Dragon's Blade"],
        "Exposed_Corn": ["assets/images/territory/icons/icon_life_item_crop_005.avif", "Exposed Corn"],
        "Eye_of_the_Destroyer": ["assets/images/gear-system/icons/icon_equipment4105_65.avif", "Eye of the Destroyer"],
        "Fiend_Guard": ["assets/images/gear-system/icons/icon_equipment4304_76.avif", "Fiend Guard"],
        "Fine_Fabric": ["assets/images/icons/icon_resource411_43.png", "Fine Fabric"],
        "Fine_Leather": ["assets/images/icons/icon_resource311_40.png", "Fine Leather"],
        "Fire": ["assets/images/battle-system/icons/elementicon2_2.avif", "Fire Property"],
        "Fire_Magic_Crystal": ["assets/images/icons/icon_resource111_15.png", "Fire Magic Crystal"],
        "Firm_Apple": ["assets/images/territory/icons/icon_life_item_crop_007.avif", "Firm Apple"],
        "Gloves": ["assets/images/gear-system/icons/popupicon_equip5.avif", "Gloves"],
        "Glupy_Star": ["assets/images/icons/glupy_star.png", "Glupy Star"],
        "God_Kings_Silver_Arm": ["assets/images/gear-system/icons/icon_equipment4201_79.avif", "God-King's Silver Arm"],
        "Gold": ["assets/images/icons/icon_resource60005_88.png", "Gold"],
        "Gold_Ore": ["assets/images/icons/icon_resource203_29.png", "Gold Ore"],
        "Gold_Ore_T": ["assets/images/territory/icons/icon_life_item_consumption_005.avif", "Gold Ore"],
        "Golden_Thread": ["assets/images/icons/icon_resource4_8.png", "Golden Thread"],
        "Hammer_of_Thunder": ["assets/images/gear-system/icons/icon_equipment4102_62.avif", "Hammer of Thunder"],
        "Hardwood": ["assets/images/icons/icon_resource501_45.png", "Hardwood"],
        "Hellfire_Robe": ["assets/images/gear-system/icons/icon_equipment4306_78.avif", "Hellfire Robe"],
        "Helm_of_Carnage": ["assets/images/gear-system/icons/icon_equipment4401_67.avif", "Helm of Carnage"],
        "Helm_of_Death": ["assets/images/gear-system/icons/icon_equipment4403_69.avif", "Helm of Death"],
        "Helmet": ["assets/images/gear-system/icons/popupicon_equip3.avif", "Helmet"],
        "HP": ["assets/images/gear-system/icons/icon_stats_hp_l.avif", "HP"],
        "Invulnerable_Armor": ["assets/images/gear-system/icons/icon_equipment4301_73.avif", "Invulnerable Armor"],
        "Immortal_Golden_Armor": ["assets/images/gear-system/icons/icon_equipment4303_75.avif", "Immortal Golden Armor"],
        "Iron_Ore": ["assets/images/icons/icon_resource201_27.png", "Iron Ore"],
        "Iron_Ore_T": ["assets/images/territory/icons/icon_life_item_consumption_003.avif", "Iron Ore"],
        "Juicy_Onion": ["assets/images/territory/icons/icon_life_item_crop_003.avif", "Juicy Onion"],
        "Key_of_Salvation": ["assets/images/icons/icon_resource60024_212.png", "Key of Salvation"],
        "Knockback": ["assets/images/battle-system/icons/icon_stats_knockback.avif", "Knockback"],
        "Light": ["assets/images/battle-system/icons/elementicon4_4.avif", "Light Property"],
        "Light_Magic_Crystal": ["assets/images/icons/icon_resource114_18.png", "Light Magic Crystal"],
        "Local_Points": ["assets/images/icons/icon_resource90080_382.avif","Local Points"],
        "Lost_Silver": ["assets/images/icons/lost_silver.png", "Lost Silver"],
        "Lumber": ["assets/images/territory/icons/icon_life_item_consumption_007.avif","Lumber"],
        "Lustful_Grape": ["assets/images/territory/icons/icon_life_item_crop_010.avif", "Lustful Grape"],
        "Magical": ["assets/images/icons/icon_stats_magical.png", "Magical Damage Type"],
        "MATK": ["assets/images/gear-system/icons/icon_stats_magical_l.avif", "MATK"],
        "Medal_of_the_Fighting_Spirit": ["assets/images/icons/Medals of the Fighting Spirit.png", "Medal of the Fighting Spirit"],
        "Mercenary_Alliance_Deed": ["assets/images/icons/Mercenary_Alliance_Deed.avif", "Mercenary Alliance Deed"],
        "MRES": ["assets/images/gear-system/icons/icon_stats_magicaldef_l.avif", "Magic RES"],
        "N_Grade": ["assets/images/gear-system/icons/N_Grade.avif", "N Grade"],
        "Neutral": ["assets/images/battle-system/icons/elementicon6_6.avif", "Neutral Property"],
        "Nickname_Ticket": ["assets/images/icons/icon_useitem1_1.png", "Nickname Ticket"],
        "Night_World_Obsidian": ["assets/images/icons/night_world_obsidian.png", "Night World Obsidian"],
        "Peat": ["assets/images/icons/icon_resource204_30.png", "Peat"],
        "Peerless_Javelin": ["assets/images/gear-system/icons/icon_equipment4103_63.avif", "Peerless Javelin"],
        "Physical": ["assets/images/icons/icon_stats_physical.png", "Physical Damage Type"],
        "Pinnacle_of_Aesthetics": ["assets/images/gear-system/icons/icon_equipment4502_86.avif", "Pinnacle of Aesthetics"],
        "Plain_Fabric": ["assets/images/icons/icon_resource401_42.png", "Plain Fabric"],
        "Plain_Leather": ["assets/images/icons/icon_resource301_39.png", "Plain Leather"],
        "Powder_of_Hope": ["assets/images/icons/icon_resource602_48.png", "Powder of Hope"],
        "Prime_Authority": ["assets/images/gear-system/icons/icon_equipment4203_81.avif", "Prime Authority"],
        "Promise_of_Harmony": ["assets/images/gear-system/icons/icon_equipment4503_87.avif", "Promise of Harmony"],
        "Property_Selective_Draw_Exchange_Ticket": ["assets/images/icons/icon_resource40015_168.png", "Property Selective Draw Exchange Ticket"],
        "Pulse_Saffron": ["assets/images/territory/icons/icon_life_item_crop_015.avif", "Pulse Suffron"],
        "R_Grade": ["assets/images/gear-system/icons/R_Grade.avif", "R Grade"],
        "Radiant_Wisdom": ["assets/images/gear-system/icons/icon_equipment4404_70.avif", "Radiant Wisdom"],
        "Rebellion": ["assets/images/gear-system/icons/icon_equipment4202_80.avif", "Rebellion"],
        "Recommended_S5_Selective_Tickets": ["assets/images/icons/icon_resource40020_265.png", "Recommended ★5 Selective Tickets"],
        "Red_Slime": ["assets/images/icons/icon_resource9003_61.png", "Red Slime"],
        "Refining_Crystal": ["assets/images/icons/icon_resource126_26.png", "Refining Crystal"],
        "Refining_Powder": ["assets/images/icons/icon_resource80001_116.png", "Refining Powder"],
        "Refining_Stone": ["assets/images/icons/icon_resource106_14.png", "Refining Stone"],
        "Ring_of_Fury": ["assets/images/gear-system/icons/icon_equipment4204_82.avif", "Ring of Fury"],
        "Ring_of_the_Lake": ["assets/images/gear-system/icons/icon_equipment4505_89.avif", "Ring of the Lake"],
        "Rock": ["assets/images/territory/icons/icon_life_item_consumption_001.avif", "Rock"],
        "Scale_of_the_Sea_God": ["assets/images/gear-system/icons/icon_equipment4302_74.avif", "Scale of the Sea God"],
        "Selective_Exclusive_Draw_Ticket": ["assets/images/icons/icon_resource40021_267.png", "Selective Exclusive Draw Ticket"],
        "Shackle_of_Treachery": ["assets/images/gear-system/icons/icon_equipment4206_84.avif", "Shackle of Treachery"],
        "Shapely_Potato": ["assets/images/territory/icons/icon_life_item_crop_002.avif", "Shapely Potato"],
        "Silver_Ore_T": ["assets/images/territory/icons/icon_life_item_consumption_004.avif", "Silver Ore"],
        "Skip": ["assets/images/icons/icon_skip.avif", "Skip Button"],
        "Solar_Brilliance": ["assets/images/gear-system/icons/icon_equipment4405_71.avif", "Solar Brilliance"],
        "Spanking_Wheat": ["assets/images/territory/icons/icon_life_item_crop_001.avif", "Spanking Wheat"],
        "Spark_of_Rampage": ["assets/images/icons/icon_resource20045_383.avif", "Spark of Rampage"],
        "SR_Exclusive_Gear_Draw_Exchange_Ticket": ["assets/images/icons/icon_resource40008_130.png", "SR Exclusive Gear Draw Exchange Ticket"],
        "SR_Grade": ["assets/images/gear-system/icons/SR_Grade.avif", "SR Grade"],
        "Stamina_Pepper": ["assets/images/territory/icons/icon_life_item_crop_012.avif", "Stamina Pepper"],
        "Sticky_Melon": ["assets/images/territory/icons/icon_life_item_crop_014.avif", "Sticky Melon"],
        "Sticky_Rice": ["assets/images/territory/icons/icon_life_item_crop_009.avif", "Sticky Rice"],
        "Sturdy_Lumber": ["assets/images/territory/icons/icon_life_item_consumption_008.avif","Sturdy Lumber"],
        "Tear_of_Goddess": ["assets/images/icons/icon_resource20005_156.png", "Tear of Goddess"],
        "Torch": ["assets/images/icons/icon_resource60023_163.png", "Torch"],
        "Travel_Gods_Friend": ["assets/images/gear-system/icons/icon_equipment4104_64.avif", "Travel God's Friend"],
        "Twin_Beans": ["assets/images/territory/icons/icon_life_item_crop_006.avif", "Twin Beans"],
        "Undefeated_Glory": ["assets/images/gear-system/icons/icon_equipment4402_68.avif", "Undefeated Glory"],
        "UR_Exclusive_Gear_Guaranteed_Draw_Exchange_Ticket": ["assets/images/icons/icon_resource40007_129.png", "UR Exclusive Gear Guaranteed Draw Exchange Ticket"],
        "UR_Grade": ["assets/images/gear-system/icons/UR_Grade.avif", "UR Grade"],
        "Venomous_Touch": ["assets/images/gear-system/icons/icon_equipment4504_88.avif", "Venomous Touch"],
        "Venus_Cacao": ["assets/images/territory/icons/icon_life_item_crop_011.avif", "Venus Cacao"],
        "Virile_Mushroom": ["assets/images/territory/icons/icon_life_item_crop_004.avif", "Virile_Mushroom"],
        "Warmth_of_the_Brazier": ["assets/images/gear-system/icons/icon_equipment4501_85.avif", "Warmth of the Brazier"],
        "Water": ["assets/images/battle-system/icons/elementicon1_1.avif", "Water Property"],
        "Water_Magic_Crystal": ["assets/images/icons/icon_resource112_16.png", "Water Magic Crystal"],
        "Weapon": ["assets/images/gear-system/icons/popupicon_equip1.avif", "Weapon"],
        "Wind": ["assets/images/battle-system/icons/elementicon3_3.avif", "Wind Property"],
        "Wind_Magic_Crystal": ["assets/images/icons/icon_resource113_17.png", "Wind Magic Crystal"],
        "Wooden_Branch": ["assets/images/territory/icons/icon_life_item_consumption_006.avif", "Wooden Branch"],
        "Yellow_Slime": ["assets/images/icons/icon_resource9001_59.png", "Yellow Slime"],
        "S": ["assets/images/gear-system/icons/S_score.avif", "S Gear Score"],
        "A": ["assets/images/gear-system/icons/A_score.avif", "A Gear Score"],
        "B": ["assets/images/gear-system/icons/B_score.avif", "B Gear Score"],
        "C": ["assets/images/gear-system/icons/C_score.avif", "C Gear Score"],

        # TERRITORY 

        "Virile_Gnocchi": ["assets/images/territory/icons/icon_life_item_dish_003.avif", "Virile Gnocchi"],
        "Bulbous_Crepe": ["assets/images/territory/icons/icon_life_item_dish_013.avif", "Bulbous Crepe"],
        "Creamy_Congee": ["assets/images/territory/icons/icon_life_item_dish_004.avif", "Creamy Congee"],
        "Curvaceous_Fried_Rice": ["assets/images/territory/icons/icon_life_item_dish_002.avif", "Curvaceous Fried Rice"],
        "Milky_Steak": ["assets/images/territory/icons/icon_life_item_dish_006.avif", "Milky Steak"],
        "Venus_Pudding": ["assets/images/territory/icons/icon_life_item_dish_009.avif", "Venus Pudding"],
        "Stamina_Pasta": ["assets/images/territory/icons/icon_life_item_dish_001.avif", "Stamina Pasta"],
        "Hormone_Glass_Noodles": ["assets/images/territory/icons/icon_life_item_dish_005.avif", "Hormone Glass Noodles"],
        "Lingerie_Cookie": ["assets/images/territory/icons/icon_life_item_dish_012.avif", "Lingerie Cookie"],
        "Apple_Tea": ["assets/images/territory/icons/icon_life_item_dish_010.avif", "Apple Tea"],
        "Nude_Salad":  ["assets/images/territory/icons/icon_life_item_dish_008.avif", "Nude Salad"],
        "Lustful_Tart": ["assets/images/territory/icons/icon_life_item_dish_011.avif", "Lustful Tart"],
        "Libido_Soup": ["assets/images/territory/icons/icon_life_item_dish_007.avif", "Libido Soup"],

        # THE SOUL WAGER

        "Soul_Token": ["assets/images/soul-wager/icons/icon_resource90087_395.avif", "Soul Token"],
        "Life_Count": ["assets/images/soul-wager/icons/icon_life_count.avif", "Life Count"],
        "Alea_Chip": ["assets/images/soul-wager/icons/icon_resource90088_396.avif", "Alea Chip"],

        "Cross": ["assets/images/soul-wager/icons/slot_icon_s_2.avif",""],
        "Close_Range_Attack": ["assets/images/soul-wager/icons/icon_tag_012.avif","Close-Range Attack"],
        "Defending": ["assets/images/soul-wager/icons/icon_tag_022.avif","Defending"],
        "Support": ["assets/images/soul-wager/icons/icon_tag_015.avif","Support"],
        "Heal": ["assets/images/soul-wager/icons/icon_tag_016.avif","Heal"],
        "Curse": ["assets/images/soul-wager/icons/icon_tag_017.avif","Curse"],
        "Long_Range_Attack": ["assets/images/soul-wager/icons/icon_tag_019.avif","Long-Range Attack"],
        "Cleanse": ["assets/images/soul-wager/icons/icon_tag_020.avif","Cleanse"],
        "Remove": ["assets/images/soul-wager/icons/icon_tag_021.avif","Remove"],

        "Regeneration": ["assets/images/soul-wager/icons/icon_tag_001.avif","Regeneration"],
        "Overheat": ["assets/images/soul-wager/icons/icon_tag_002.avif","Overheat"],
        "Lifesteal": ["assets/images/soul-wager/icons/icon_tag_003.avif","Lifesteal"],
        "Focus": ["assets/images/soul-wager/icons/icon_tag_004.avif","Focus"],
        "SP": ["assets/images/soul-wager/icons/icon_tag_005.avif","SP"],
        "Strength": ["assets/images/soul-wager/icons/icon_tag_006.avif","Strength"],
        "Counter": ["assets/images/soul-wager/icons/icon_tag_007.avif","Counter"],
        "Poison": ["assets/images/soul-wager/icons/icon_tag_008.avif","Poison"],
        "Frost": ["assets/images/soul-wager/icons/icon_tag_009.avif","Frost"],
        "Darkness": ["assets/images/soul-wager/icons/icon_tag_010.avif","Darkness"],
        "Laceration": ["assets/images/soul-wager/icons/icon_tag_011.avif","Laceration"],

        "Regeneration2": ["assets/images/soul-wager/icons/icon_buff_011.avif","Regeneration"],
        "Overheat2": ["assets/images/soul-wager/icons/icon_buff_012.avif","Overheat"],
        "Lifesteal2": ["assets/images/soul-wager/icons/icon_buff_013.avif","Lifesteal"],
        "Focus2": ["assets/images/soul-wager/icons/icon_buff_014.avif","Focus"],
        "SP2": ["assets/images/soul-wager/icons/icon_buff_015.avif","SP"],
        "Strength2": ["assets/images/soul-wager/icons/icon_buff_016.avif","Strength"],
        "Counter2": ["assets/images/soul-wager/icons/icon_buff_017.avif","Counter"],
        "Poison2": ["assets/images/soul-wager/icons/icon_buff_018.avif","Poison"],
        "Frost2": ["assets/images/soul-wager/icons/icon_buff_019.avif","Frost"],
        "Darkness2": ["assets/images/soul-wager/icons/icon_buff_020.avif","Darkness"],
        "Laceration2": ["assets/images/soul-wager/icons/icon_buff_021.avif","Laceration"],
    }

    GEAR_DB = {
    "Evil Dragon's Blade": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4101_61.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{CritDMG}} **Crit DMG** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$37 \sim 112$", "stat_2": "$50\% \sim 150.8\%$"},
            "III": {"stat_1": "$30 \sim 90$", "stat_2": "$40\% \sim 120.4\%$"}
        }
    },
    "Hammer of Thunder": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4102_62.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_2}</span>", "class": "yellow"}
        ],
        "tiers": {
            "IV": {"stat_1": "$37 \sim 112$", "stat_2": "$25\% \sim 75.4\%$"}
        }
    },
    "Peerless Javelin": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4103_63.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_2}</span>", "class": "yellow"}
        ],
        "tiers": {
            "IV": {"stat_1": "$37 \sim 112$", "stat_2": "$37 \sim 112$"}
        }
    },
    "Travel God's Friend": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4104_64.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{CritDMG}} **Crit DMG** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$37 \sim 112$", "stat_2": "$50\% \sim 150.8\%$"},
            "III": {"stat_1": "$30 \sim 90$", "stat_2": "$40\% \sim 120.4\%$"}
        }
    },
    "Eye of the Destroyer": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4105_65.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_2}</span>", "class": "magenta"}
        ],
        "tiers": {
            "IV": {"stat_1": "$37 \sim 112$", "stat_2": "$25\% \sim 75.4\%$"}
        }
    },
    "Demon's Forbidden Book": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4106_66.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_2}</span>", "class": "magenta"}
        ],
        "tiers": {
            "IV": {"stat_1": "$37 \sim 112$", "stat_2": "$37 \sim 112$"}
        }
    },
    "Invulnerable Armor": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4301_73.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_2}</span>", "class": "yellow"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$9\% \sim 27\%$"},
            "III": {"stat_1": "$7.2\% \sim 21.6\%$", "stat_2": "$7.2\% \sim 21.6\%$"}
        }
    },
    "Scale of the Sea God": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4302_74.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$270 \sim 810$"}
        }
    },
    "Immortal Golden Armor": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4303_75.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$30\% \sim 90\%$"}
        }
    },
    "Fiend Guard": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4304_76.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_2}</span>", "class": "magenta"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$9\% \sim 27\%$"},
            "III": {"stat_1": "$7.2\% \sim 21.6\%$", "stat_2": "$7.2\% \sim 21.6\%$"}
        }
    },
    "Deaths Shroud": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4305_77.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$270 \sim 810$"}
        }
    },
    "Hellfire Robe": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4306_78.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$30\% \sim 90\%$"}
        }
    },
    "Helm of Carnage": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4401_67.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_2}</span>", "class": "yellow"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$9\% \sim 27\%$"},
            "III": {"stat_1": "$7.2\% \sim 21.6\%$", "stat_2": "$7.2\% \sim 21.6\%$"}
        }
    },
    "Undefeated Glory": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4402_68.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$270 \sim 810$"}
        }
    },
    "Helm of Death": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4403_69.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{DEF}} **DEF** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$30\% \sim 90\%$"}
        }
    },
    "Radiant Wisdom": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4404_70.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_2}</span>", "class": "magenta"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$9\% \sim 27\%$"},
            "III": {"stat_1": "$7.2\% \sim 21.6\%$", "stat_2": "$7.2\% \sim 21.6\%$"}
        }
    },
    "Solar Brilliance": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4405_71.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$270 \sim 810$"}
        }
    },
    "Crown of Galaxy": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4406_72.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MRES}} **MRES** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$9\% \sim 27\%$", "stat_2": "$30\% \sim 90\%$"}
        }
    },
    "Warmth of the Brazier": {
        "type": "neutral",
        "icon": "assets/images/gear-system/icons/icon_equipment4501_85.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{CritRate}} **Crit Rate** <span class='stat-num'>{stat_1}</span>", "class": "white"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{CritRate}} **Crit Rate** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$8.33\% \sim 25.13\%$", "stat_2": "$8.33\% \sim 25.13\%$"}
        }
    },
    "Pinnacle of Aesthetics": {
        "type": "neutral",
        "icon": "assets/images/gear-system/icons/icon_equipment4502_86.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{CritRate}} **Crit Rate** <span class='stat-num'>{stat_1}</span>", "class": "white"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$8.33\% \sim 25.13\%$", "stat_2": "$270 \sim 810$"}
        }
    },
    "Promise of Harmony": {
        "type": "neutral",
        "icon": "assets/images/gear-system/icons/icon_equipment4503_87.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{CritRate}} **Crit Rate** <span class='stat-num'>{stat_1}</span>", "class": "white"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$8.33\% \sim 25.13\%$", "stat_2": "$30\% \sim 90\%$"}
        }
    },
    "Venomous Touch": {
        "type": "neutral",
        "icon": "assets/images/gear-system/icons/icon_equipment4504_88.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{CritDMG}} **Crit DMG** <span class='stat-num'>{stat_1}</span>", "class": "white"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{CritDMG}} **Crit DMG** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$50\% \sim 150.8\%$", "stat_2": "$50\% \sim 150.8\%$"},
            "III": {"stat_1": "$40\% \sim 120.4\%$", "stat_2": "$40\% \sim 120.4\%$"}
        }
    },
    "Ring of the Lake": {
        "type": "neutral",
        "icon": "assets/images/gear-system/icons/icon_equipment4505_89.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{CritDMG}} **Crit DMG** <span class='stat-num'>{stat_1}</span>", "class": "white"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$50\% \sim 150.8\%$", "stat_2": "$270 \sim 810$"}
        }
    },
    "Charming Gaze": {
        "type": "neutral",
        "icon": "assets/images/gear-system/icons/icon_equipment4506_90.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{CritDMG}} **Crit DMG** <span class='stat-num'>{stat_1}</span>", "class": "white"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{HP}} **HP** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$50\% \sim 150.8\%$", "stat_2": "$30\% \sim 90\%$"}
        }
    },
    "God-King's Silver Arm": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4201_79.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_2}</span>", "class": "yellow"}
        ],
        "tiers": {
            "IV": {"stat_1": "$25\% \sim 75.4\%$", "stat_2": "$25\% \sim 75.4\%$"},
            "III": {"stat_1": "$20\% \sim 59.9\%$", "stat_2": "$20\% \sim 59.9\%$"}
        }
    },
    "Rebellion": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4202_80.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{CritRate}} **Crit Rate** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$25\% \sim 75.4\%$", "stat_2": "$8.33\% \sim 25.13\%$"}
        }
    },
    "Prime Authority": {
        "type": "physical",
        "icon": "assets/images/gear-system/icons/icon_equipment4203_81.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_1}</span>", "class": "yellow"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{ATK}} **ATK** <span class='stat-num'>{stat_2}</span>", "class": "yellow"}
        ],
        "tiers": {
            "IV": {"stat_1": "$25\% \sim 75.4\%$", "stat_2": "$37 \sim 112$"},
            "III": {"stat_1": "$20\% \sim 59.9\%$", "stat_2": "$30 \sim 90$"}
        }
    },
    "Shackle of Treachery": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4206_84.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_2}</span>", "class": "magenta"}
        ],
        "tiers": {
            "IV": {"stat_1": "$25\% \sim 75.4\%$", "stat_2": "$25\% \sim 75.4\%$"},
            "III": {"stat_1": "$20\% \sim 59.9\%$", "stat_2": "$20\% \sim 59.9\%$"}
        }
    },
    "Ring of Fury": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4204_82.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{CritRate}} **Crit Rate** <span class='stat-num'>{stat_2}</span>", "class": "white"}
        ],
        "tiers": {
            "IV": {"stat_1": "$25\% \sim 75.4\%$", "stat_2": "$8.33\% \sim 25.13\%$"}
        }
    },
    "Dragon Scales Protection": {
        "type": "magical",
        "icon": "assets/images/gear-system/icons/icon_equipment4205_83.avif",
        "stats": [
            {"text": "Main Attribute 1:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_1}</span>", "class": "magenta"},
            {"text": "Main Attribute 2:", "class": "gray"},
            {"text": "{{MATK}} **MATK** <span class='stat-num'>{stat_2}</span>", "class": "magenta"}
        ],
        "tiers": {
            "IV": {"stat_1": "$25\% \sim 75.4\%$", "stat_2": "$37 \sim 112$"},
            "III": {"stat_1": "$20\% \sim 59.9\%$", "stat_2": "$30 \sim 90$"}
        }
    }
    }


    def format_stat_line(text, prefix):
        text = text.replace("{{ATK}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_physical_l.avif" class="icon" alt="ATK">')
        text = text.replace("{{MATK}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_magical_l.avif" class="icon" alt="MATK">')
        text = text.replace("{{DEF}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_physicaldef_l.avif" class="icon" alt="DEF">')
        text = text.replace("{{MRES}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_magicaldef_l.avif" class="icon" alt="MRES">')
        text = text.replace("{{HP}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_hp_l.avif" class="icon" alt="HP">')
        text = text.replace("{{CritDMG}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_criticalhit_l.avif" class="icon" alt="Critical DMG">')
        text = text.replace("{{CritRate}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_critical_l.avif" class="icon" alt="Critical Rate">')
        return text 

    @env.macro
    def gear(name, tier="IV"):
        item = GEAR_DB.get(name, {"type": "neutral", "stats": [], "icon": "assets/images/gear-system/icons/popupicon_equip3.avif", "tiers": {}})
        
        tier_data = item.get("tiers", {}).get(tier, {"stat_1": "??", "stat_2": "??"})
    
        tooltip_html = '<span class="gear-tooltip-box">'
        tooltip_html += f'<span class="tooltip-header">'
        tooltip_html += f'<img src="{prefix}{item["icon"]}" class="icon header-icon" alt="">'
        tooltip_html += f'<span class="header-title {item["type"]}">{name} {tier}</span>'
        tooltip_html += f'</span>'
        tooltip_html += '<span class="tooltip-divider-line"></span>'
    
        for line in item["stats"]:

            text_with_icons = format_stat_line(line["text"], prefix)
            
            processed_text = text_with_icons.format(**tier_data)
            
            line_class = line.get("class", "white")
            tooltip_html += f'<span class="tooltip-line {line_class}">{processed_text}</span>'
            
        tooltip_html += '</span>'

        return (
                f'<span class="gear-tooltip-wrapper">'
                f'<img src="{prefix}{item["icon"]}" class="icon" alt="{name}">' 
                f'<span class="gear-name {item["type"]}">{name}</span>' 
                f'{tooltip_html}' 
                f'</span>'
            )

    for key, info in images.items():
        path, label = info[0], info[1]
    
        html_payload = f'<img src="{prefix}{path}" title="{label}" alt="{label}" class="icon" />'
        
        env.macros[key] = html_payload


    # -----------------------------------------------------------------------------------------------------#

    # TERRITORY STUFF 

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
        "unlock_level": 80,
        "seed_cost": 3,
        "growth_time": "18 Hours",
        "exp": 36,
        "sell_price": [88, 104, 120],
        "desc": "A round fruit with a hard shell, the crack from which oozes a sticky, white fluid. Squeezing the fruity flesh causes even more viscous liquids to seep from the fruit, wetting the floor."
    },
    "Pulse Saffron": {
        "icon": "assets/images/territory/icons/icon_life_item_crop_015.avif",
        "unlock_level": 100,
        "seed_cost": 3,
        "growth_time": "20 Hours",
        "exp": 40,
        "sell_price": [110, 130, 150],
        "desc": "A flower with moist, red stamens that stretch out like tongues between its purple petals. When touched, the way they recoil makes the flower seem almost like a living creature."
    }
    }

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
    },
    }

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
    },
    }



    @env.macro
    def territory_tile(name):
    
        item = TERRITORY_DB.get(name, {})
        icon = item.get("icon", "default.png")
        
        tooltip_html = (
            f'<span class="gear-tooltip-box">'
            f'<span class="tooltip-header">'
            f'<img src="{prefix}{icon}" class="icon header-icon" alt="">'
            f'<span class="header-title white bold">{name}</span>'
            f'</span>'
            f'<span class="tooltip-divider-line"></span>'
        )

        limit = item.get("limit", "?")
        usage = item.get("usage", "Unknown")

        if usage:
            tooltip_html += f'<span class="tooltip-line gray bold">Limit: {limit} | Type: {usage}</span>'
        else:
            tooltip_html += f'<span class="tooltip-line gray bold">Limit: {limit}</span>'

        time = item.get("time")
        if time:
            tooltip_html += f'<span class="tooltip-line gray bold">Build Time: {time}</span>'
            
        cost_data = item.get("cost")
        if isinstance(cost_data, dict): 
            cost_html_parts = []
            for mat_name, amount in cost_data.items():
                mat_icon = MATERIALS_DB.get(mat_name, "default_mat.png")
                mat_html = f'<span class="mat-cost-item"><img src="{prefix}{mat_icon}" class="inline-mat-icon icon" alt="{mat_name}"> {amount}x {mat_name}</span>'
                cost_html_parts.append(mat_html)
                
            joined_costs = "".join(cost_html_parts)
            tooltip_html += f'<span class="tooltip-line gray bold cost-flex-line"><span class="cost-label">Cost:</span> <span class="cost-items-wrap">{joined_costs}</span></span>'
            
        elif cost_data and cost_data != "None":
            tooltip_html += f'<span class="tooltip-line gray bold">Cost: {cost_data}</span>'
            
        elif cost_data and cost_data != "None":
            tooltip_html += f'<span class="tooltip-line gray bold">Cost: {cost_data}</span>'
            
        if item.get("bonus") or item.get("desc"):
            tooltip_html += f'<span class="tooltip-divider-line"></span>'
            
        bonus = item.get("bonus")
        if bonus and bonus != "None":
            tooltip_html += f'<span class="tooltip-line green"><strong class="yellow">Option:</strong> {bonus}</span>'
            
        desc = item.get("desc")
        if desc:
            tooltip_html += f'<span class="tooltip-line white">{desc}</span>'
            
        tooltip_html += f'</span>'

        return (
            f'<span class="territory-grid-tile gear-tooltip-wrapper">'
            f'<img src="{prefix}{icon}" class="tile-image" alt="{name}">'
            f'{tooltip_html}'
            f'</span>'
        )
    

    @env.macro
    def crop_tile(name):
        item = CROPS_DB.get(name, {})
        icon = item.get("icon", "default_crop.png")
        
        html = (
            f'<span class="gear-tooltip-box">'
            f'<span class="tooltip-header">'
            f'<img src="{prefix}{icon}" class="icon header-icon" alt="">'
            f'<span class="header-title white bold">{name}</span>'
            f'</span>'
            f'<span class="tooltip-divider-line"></span>'
        )

        unlock = item.get("unlock_level", "?")
        time = item.get("growth_time", "?")
        seed_cost = item.get("seed_cost", "?")
        exp = item.get("exp", "?")
        
        html += f'<span class="tooltip-line gray bold">Unlock: Lv. {unlock} | Growth: {time}</span>'
        html += f'<span class="tooltip-line gray bold">Seed Cost: {seed_cost} | EXP: {exp}</span>'
        html += f'<span class="tooltip-divider-line"></span>'
        
        prices = item.get("sell_price")
        if isinstance(prices, list) and len(prices) == 3:
            html += f'<span class="tooltip-line gray bold">Sell Price:</span>'
            html += (
                f'<span class="crop-price-row">'
                f'<span class="price-normal">Normal: {prices[0]} <img src="{prefix}assets/images/icons/icon_resource90080_382.avif" class="icon" alt="Local Points"></span>'
                f'<span class="price-high">Rare: {prices[1]} <img src="{prefix}assets/images/icons/icon_resource90080_382.avif" class="icon" alt="Local Points"></span>'
                f'<span class="price-premium">Legendary: {prices[2]} <img src="{prefix}assets/images/icons/icon_resource90080_382.avif" class="icon" alt="Local Points"></span>'
                f'</span>'
            )
            
        desc = item.get("desc")
        if desc:
            if isinstance(prices, list):
                html += f'<span class="tooltip-divider-line"></span>'
            html += f'<span class="tooltip-line white">{desc}</span>'
            
        html += f'</span>'

        return (
            f'<span class="territory-grid-tile gear-tooltip-wrapper">'
            f'<img src="{prefix}{icon}" class="tile-image" alt="{name}">'
            f'{html}'
            f'</span>'
        )
    
    @env.macro
    def dish_tile(name):
        item = DISHES_DB.get(name, {})
        icon = item.get("icon", "default_dish.png")
        
        html = (
            f'<span class="gear-tooltip-box">'
            f'<span class="tooltip-header">'
            f'<img src="{prefix}{icon}" class="icon header-icon" alt="">'
            f'<span class="header-title white bold">{name}</span>'
            f'</span>'
            f'<span class="tooltip-divider-line"></span>'
        )
        
        unlock = item.get("unlock_level", "?")
        sell = item.get("sell_price", "?")
        html += f'<span class="tooltip-line gray bold">Unlock: Lv. {unlock} | Sell Price: {sell}</span>'
        
        bonus = item.get("bonus")
        if isinstance(bonus, list):
            joined_bonuses = "<br>".join(bonus)
            html += f'<span class="tooltip-line green" style="align-items: flex-start;"><strong class="yellow">Bonus:</strong> <span>{joined_bonuses}</span></span>'
        elif bonus:
            html += f'<span class="tooltip-line green"><strong class="yellow">Bonus:</strong> {bonus}</span>'
            
        html += f'<span class="tooltip-divider-line"></span>'
        
        ingredients = item.get("ingredients")
        if isinstance(ingredients, dict):
            ing_html_parts = []
            
            for ing_name, amount in ingredients.items():
                if ing_name in CROPS_DB:
                    ing_icon = CROPS_DB[ing_name].get("icon", "default_crop.png")
                else:
                    ing_icon = MATERIALS_DB.get(ing_name, "default_mat.png")
                    
                ing_html = f'<span class="mat-cost-item"><img src="{prefix}{ing_icon}" class="inline-mat-icon icon" alt="{ing_name}"> {amount}x {ing_name}</span>'
                ing_html_parts.append(ing_html)
                
            joined_ings = "".join(ing_html_parts)
            html += f'<span class="tooltip-line gray bold cost-flex-line"><span class="cost-label">Recipe:</span> <span class="cost-items-wrap">{joined_ings}</span></span>'
            
        desc = item.get("desc")
        if desc:
            html += f'<span class="tooltip-divider-line"></span>'
            html += f'<span class="tooltip-line white">{desc}</span>'
            
        html += f'</span>'

        return (
            f'<span class="territory-grid-tile gear-tooltip-wrapper">'
            f'<img src="{prefix}{icon}" class="tile-image" alt="{name}">'
            f'{html}'
            f'</span>'
        )
    
    @env.macro
    def tool_tile(name):
        item = TOOLS_DB.get(name, {})
        icon = item.get("icon", "default_tool.png")
        
        tooltip_html = (
            f'<span class="gear-tooltip-box">'
            f'<span class="tooltip-header">'
            f'<img src="{prefix}{icon}" class="icon header-icon" alt="">'
            f'<span class="header-title white bold">{name}</span>'
            f'</span>'
            f'<span class="tooltip-divider-line"></span>'
        )
        
        level = item.get("level", "?")
        points = item.get("local_points", "?")
        tooltip_html += f'<span class="tooltip-line gray bold">Level: {level} | Local Points: {points}</span>'
        
        stats = item.get("stats")
        if stats:
            tooltip_html += f'<span class="tooltip-divider-line"></span>'
            if isinstance(stats, (list, tuple)):
                joined_stats = "<br>".join(stats)
                tooltip_html += f'<span class="tooltip-line green" style="align-items: flex-start;"><strong class="yellow">Stats:</strong> <span>{joined_stats}</span></span>'
            else:
                tooltip_html += f'<span class="tooltip-line green"><strong class="yellow">Stats:</strong> {stats}</span>'
            
        materials = item.get("materials")
        if isinstance(materials, dict):
            tooltip_html += f'<span class="tooltip-divider-line"></span>'
            mat_html_parts = []
            
            for mat_name, amount in materials.items():
                mat_icon = MATERIALS_DB.get(mat_name, "default_mat.png")
                mat_html = f'<span class="mat-cost-item"><img src="{prefix}{mat_icon}" class="inline-mat-icon icon" alt="{mat_name}"> {amount}x {mat_name}</span>'
                mat_html_parts.append(mat_html)
                
            joined_mats = "".join(mat_html_parts)
            tooltip_html += f'<span class="tooltip-line gray bold cost-flex-line"><span class="cost-label">Cost:</span> <span class="cost-items-wrap">{joined_mats}</span></span>'
            
        tooltip_html += f'</span>'

        return (
            f'<span class="territory-grid-tile gear-tooltip-wrapper">'
            f'<img src="{prefix}{icon}" class="tile-image" alt="{name}">'
            f'{tooltip_html}'
            f'</span>'
        )
    