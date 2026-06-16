def define_env(env):

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
        "Coal": ["assets/images/icons/icon_resource214_35.png", "Coal"],
        "Cooked_Rice": ["assets/images/icons/cooked_rice.png", "Cooked Rice"],
        "Copper_Ore": ["assets/images/icons/icon_resource202_28.png", "Copper Ore"],
        "Costumes": ["assets/images/icons/icon_pictorialbook7.png", "Costumes"],
        "CritDMG": ["assets/images/gear-system/icons/icon_stats_criticalhit_l.avif", "Critical DMG"],
        "CritRate": ["assets/images/gear-system/icons/icon_stats_critical_l.avif", "Critical Rate"],
        "Crown_of_Galaxy": ["assets/images/gear-system/icons/icon_equipment4406_72.avif", "Crown of Galaxy"],
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
        "Eye_of_the_Destroyer": ["assets/images/gear-system/icons/icon_equipment4105_65.avif", "Eye of the Destroyer"],
        "Fiend_Guard": ["assets/images/gear-system/icons/icon_equipment4304_76.avif", "Fiend Guard"],
        "Fine_Fabric": ["assets/images/icons/icon_resource411_43.png", "Fine Fabric"],
        "Fine_Leather": ["assets/images/icons/icon_resource311_40.png", "Fine Leather"],
        "Fire": ["assets/images/battle-system/icons/elementicon2_2.avif", "Fire Property"],
        "Fire_Magic_Crystal": ["assets/images/icons/icon_resource111_15.png", "Fire Magic Crystal"],
        "Gloves": ["assets/images/gear-system/icons/popupicon_equip5.avif", "Gloves"],
        "Glupy_Star": ["assets/images/icons/glupy_star.png", "Glupy Star"],
        "God_Kings_Silver_Arm": ["assets/images/gear-system/icons/icon_equipment4201_79.avif", "God-King's Silver Arm"],
        "Gold": ["assets/images/icons/icon_resource60005_88.png", "Gold"],
        "Gold_Ore": ["assets/images/icons/icon_resource203_29.png", "Gold Ore"],
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
        "Key_of_Salvation": ["assets/images/icons/icon_resource60024_212.png", "Key of Salvation"],
        "Knockback": ["assets/images/battle-system/icons/icon_stats_knockback.avif", "Knockback"],
        "Light": ["assets/images/battle-system/icons/elementicon4_4.avif", "Light Property"],
        "Light_Magic_Crystal": ["assets/images/icons/icon_resource114_18.png", "Light Magic Crystal"],
        "Lost_Silver": ["assets/images/icons/lost_silver.png", "Lost Silver"],
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
        "Scale_of_the_Sea_God": ["assets/images/gear-system/icons/icon_equipment4302_74.avif", "Scale of the Sea God"],
        "Selective_Exclusive_Draw_Ticket": ["assets/images/icons/icon_resource40021_267.png", "Selective Exclusive Draw Ticket"],
        "Shackle_of_Treachery": ["assets/images/gear-system/icons/icon_equipment4206_84.avif", "Shackle of Treachery"],
        "Skip": ["assets/images/icons/icon_skip.avif", "Skip Button"],
        "Solar_Brilliance": ["assets/images/gear-system/icons/icon_equipment4405_71.avif", "Solar Brilliance"],
        "Spark_of_Rampage": ["assets/images/icons/icon_resource20045_383.avif", "Spark of Rampage"],
        "SR_Exclusive_Gear_Draw_Exchange_Ticket": ["assets/images/icons/icon_resource40008_130.png", "SR Exclusive Gear Draw Exchange Ticket"],
        "SR_Grade": ["assets/images/gear-system/icons/SR_Grade.avif", "SR Grade"],
        "Tear_of_Goddess": ["assets/images/icons/icon_resource20005_156.png", "Tear of Goddess"],
        "Torch": ["assets/images/icons/icon_resource60023_163.png", "Torch"],
        "Travel_Gods_Friend": ["assets/images/gear-system/icons/icon_equipment4104_64.avif", "Travel God's Friend"],
        "Undefeated_Glory": ["assets/images/gear-system/icons/icon_equipment4402_68.avif", "Undefeated Glory"],
        "UR_Exclusive_Gear_Guaranteed_Draw_Exchange_Ticket": ["assets/images/icons/icon_resource40007_129.png", "UR Exclusive Gear Guaranteed Draw Exchange Ticket"],
        "UR_Grade": ["assets/images/gear-system/icons/UR_Grade.avif", "UR Grade"],
        "Venomous_Touch": ["assets/images/gear-system/icons/icon_equipment4504_88.avif", "Venomous Touch"],
        "Warmth_of_the_Brazier": ["assets/images/gear-system/icons/icon_equipment4501_85.avif", "Warmth of the Brazier"],
        "Water": ["assets/images/battle-system/icons/elementicon1_1.avif", "Water Property"],
        "Water_Magic_Crystal": ["assets/images/icons/icon_resource112_16.png", "Water Magic Crystal"],
        "Weapon": ["assets/images/gear-system/icons/popupicon_equip1.avif", "Weapon"],
        "Wind": ["assets/images/battle-system/icons/elementicon3_3.avif", "Wind Property"],
        "Wind_Magic_Crystal": ["assets/images/icons/icon_resource113_17.png", "Wind Magic Crystal"],
        "Yellow_Slime": ["assets/images/icons/icon_resource9001_59.png", "Yellow Slime"],
        "S": ["assets/images/gear-system/icons/S_score.avif", "S Gear Score"],
        "A": ["assets/images/gear-system/icons/A_score.avif", "A Gear Score"],
        "B": ["assets/images/gear-system/icons/B_score.avif", "B Gear Score"],
        "C": ["assets/images/gear-system/icons/C_score.avif", "C Gear Score"]
    }

    prefix = "/BD2-Overview/"

    for key, info in images.items():
        path, label = info[0], info[1]
    
        html_payload = f'<img src="{prefix}{path}" title="{label}" alt="{label}" class="icon" />'
        
        env.macros[key] = html_payload