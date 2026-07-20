import os
import sys
from ast import For
import json
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docs.data.icons import IMAGES
from docs.data.gear import GEAR_DB
from docs.data.territory import MATERIALS_DB, TERRITORY_DB, CROPS_DB, TOOLS_DB, DISHES_DB

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

    for key, info in IMAGES.items():
        path, label = info[0], info[1]
    
        html_payload = f'<img src="{prefix}{path}" title="{label}" alt="{label}" class="icon" />'
        
        env.macros[key] = html_payload


    # -----------------------------------------------------------------------------------------------------#

    # TERRITORY STUFF 

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
    