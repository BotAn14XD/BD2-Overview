import os
import sys
import json
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.icons import IMAGES
from data.gear import GEAR_DB
from data.territory import MATERIALS_DB, TERRITORY_DB, CROPS_DB, TOOLS_DB, DISHES_DB

_EMPTY = "\u2014"

def _data_table(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(f"<tr>{r}</tr>" for r in rows)
    return (
        '<div class="responsive-table-wrapper">'
        f'<table class="data-table"><thead><tr>{head}</tr></thead>'
        f'<tbody>{body}</tbody></table></div>'
    )

def _multi(val):
    if isinstance(val, list):
        return "<br>".join(str(x) for x in val) if val else _EMPTY
    return val if val else _EMPTY

def _tt_header(name, icon, prefix):
    """Opening of a tooltip box: icon + title + divider."""
    return (
        f'<span class="gear-tooltip-box">'
        f'<span class="tooltip-header">'
        f'<img src="{prefix}{icon}" class="icon header-icon" alt="">'
        f'<span class="header-title white bold">{name}</span>'
        f'</span>'
        f'<span class="tooltip-divider-line"></span>'
    )


def _mat_icon(name):
    """Where to find the icon for a plain material."""
    return MATERIALS_DB.get(name, "default_mat.png")


def _ingredient_icon(name):
    """Dish ingredients can be crops OR materials, so check crops first."""
    if name in CROPS_DB:
        return CROPS_DB[name].get("icon", "default_crop.png")
    return MATERIALS_DB.get(name, "default_mat.png")


def _tt_cost(label, items, prefix, icon_resolver):
    """The 'Cost:' / 'Recipe:' flex line.

    label         -> the word before the colon ("Cost", "Recipe")
    items         -> dict of {name: amount}
    icon_resolver -> a function that turns a name into its icon path
                     (pass _mat_icon or _ingredient_icon)
    """
    parts = []
    for mat_name, amount in items.items():
        icon = icon_resolver(mat_name)
        parts.append(
            f'<span class="mat-cost-item">'
            f'<img src="{prefix}{icon}" class="inline-mat-icon icon" alt="{mat_name}"> '
            f'{amount}x {mat_name}</span>'
        )
    return (f'<span class="tooltip-line gray bold cost-flex-line">'
            f'<span class="cost-label">{label}:</span> '
            f'<span class="cost-items-wrap">{"".join(parts)}</span></span>')


def _tt_wrap(name, icon, inner, prefix):
    """The outer clickable tile that holds the image + its tooltip."""
    return (f'<span class="territory-grid-tile gear-tooltip-wrapper">'
            f'<img src="{prefix}{icon}" class="tile-image" alt="{name}">'
            f'{inner}</span>')


def define_env(env):
    from urllib.parse import urlparse

    prefix = urlparse(env.conf["site_url"]).path or "/"
    if not prefix.endswith("/"):
        prefix += "/"
    env.variables["prefix"] = prefix 

    @env.macro
    def time(t):
        return f'<span class="local-time" data-utc="{t.strip()}">{t.strip()} UTC</span>'

    @env.macro
    def redirect_btn(target_page, button_text, color="#2196f3"):
        is_external = target_page.startswith("http://") or target_page.startswith("https://")

        href_target = target_page if is_external else f"{prefix}{target_page}"
        ext_class = " no-ext-icon" if is_external else ""

        attrs = f'href="{href_target}" class="redirect-btn{ext_class}" style="--hover-color: {color};"'
        if is_external:
            attrs += ' target="_blank" rel="noopener noreferrer"'

        return (
            f'<div class="redirect-btn-wrap">'
            f'<a {attrs}>{button_text} &rarr;</a>'
            f'</div>'
        )


    @env.macro
    def share_btn(anchor_id):
        return (
            f'<span id="{anchor_id}"></span>'
            f'<span class="share-link-wrapper">'
            f'<input type="button" class="share-btn" data-anchor="{anchor_id}" value="Copy Share Link">'
            f'</span>'
        )


    def format_stat_line(text, prefix):
        text = text.replace("{{ATK}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_physical_l.avif" class="icon mono" alt="ATK">')
        text = text.replace("{{MATK}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_magical_l.avif" class="icon mono" alt="MATK">')
        text = text.replace("{{DEF}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_physicaldef_l.avif" class="icon mono" alt="DEF">')
        text = text.replace("{{MRES}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_magicaldef_l.avif" class="icon mono" alt="MRES">')
        text = text.replace("{{HP}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_hp_l.avif" class="icon mono" alt="HP">')
        text = text.replace("{{CritDMG}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_criticalhit_l.avif" class="icon mono" alt="Critical DMG">')
        text = text.replace("{{CritRate}}", f'<img src="{prefix}assets/images/gear-system/icons/icon_stats_critical_l.avif" class="icon mono" alt="Critical Rate">')
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
            processed_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', processed_text)
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
        cls = "icon mono" if (len(info) > 2 and "mono" in info[2:]) else "icon"

        html_payload = f'<img src="{prefix}{path}" title="{label}" alt="{label}" class="{cls}" />'

        env.macros[key] = html_payload

    @env.macro
    def gear_table():
        rows = [f'<td>{gear(name)}</td><td>{item.get("type","").title()}</td>'
                for name, item in GEAR_DB.items()]
        return _data_table(["Gear", "Type"], rows)



    # -----------------------------------------------------------------------------------------------------#

    # TERRITORY STUFF

    @env.macro
    def territory_tile(name):
        item = TERRITORY_DB.get(name, {})
        icon = item.get("icon", "default.png")

        html = _tt_header(name, icon, prefix)

        limit = item.get("limit", "?")
        usage = item.get("usage", "Unknown")
        if usage:
            html += f'<span class="tooltip-line gray bold">Limit: {limit} | Type: {usage}</span>'
        else:
            html += f'<span class="tooltip-line gray bold">Limit: {limit}</span>'

        time = item.get("time")
        if time:
            html += f'<span class="tooltip-line gray bold">Build Time: {time}</span>'

        cost_data = item.get("cost")
        if isinstance(cost_data, dict):
            html += _tt_cost("Cost", cost_data, prefix, _mat_icon)
        elif cost_data and cost_data != "None":
            html += f'<span class="tooltip-line gray bold">Cost: {cost_data}</span>'

        if item.get("bonus") or item.get("desc"):
            html += f'<span class="tooltip-divider-line"></span>'

        bonus = item.get("bonus")
        if bonus and bonus != "None":
            html += f'<span class="tooltip-line green"><strong class="yellow">Option:</strong> {bonus}</span>'

        desc = item.get("desc")
        if desc:
            html += f'<span class="tooltip-line white">{desc}</span>'

        html += f'</span>'
        return _tt_wrap(name, icon, html, prefix)


    @env.macro
    def crop_tile(name):
        item = CROPS_DB.get(name, {})
        icon = item.get("icon", "default_crop.png")

        html = _tt_header(name, icon, prefix)

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
        return _tt_wrap(name, icon, html, prefix)


    @env.macro
    def dish_tile(name):
        item = DISHES_DB.get(name, {})
        icon = item.get("icon", "default_dish.png")

        html = _tt_header(name, icon, prefix)

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
            html += _tt_cost("Recipe", ingredients, prefix, _ingredient_icon)

        desc = item.get("desc")
        if desc:
            html += f'<span class="tooltip-divider-line"></span>'
            html += f'<span class="tooltip-line white">{desc}</span>'

        html += f'</span>'
        return _tt_wrap(name, icon, html, prefix)


    @env.macro
    def tool_tile(name):
        item = TOOLS_DB.get(name, {})
        icon = item.get("icon", "default_tool.png")

        html = _tt_header(name, icon, prefix)

        level = item.get("level", "?")
        points = item.get("local_points", "?")
        html += f'<span class="tooltip-line gray bold">Level: {level} | Local Points: {points}</span>'

        stats = item.get("stats")
        if stats:
            html += f'<span class="tooltip-divider-line"></span>'
            if isinstance(stats, (list, tuple)):
                joined_stats = "<br>".join(stats)
                html += f'<span class="tooltip-line green" style="align-items: flex-start;"><strong class="yellow">Stats:</strong> <span>{joined_stats}</span></span>'
            else:
                html += f'<span class="tooltip-line green"><strong class="yellow">Stats:</strong> {stats}</span>'

        materials = item.get("materials")
        if isinstance(materials, dict):
            html += f'<span class="tooltip-divider-line"></span>'
            html += _tt_cost("Cost", materials, prefix, _mat_icon)

        html += f'</span>'
        return _tt_wrap(name, icon, html, prefix)
    
    def _icon_cell(icon):
        return f'<td><img src="{prefix}{icon}" class="table-icon icon-list" alt=""></td>'

    def _mats_inline(items, resolver):
        if not isinstance(items, dict) or not items:
            return _EMPTY
        return "<br>".join(
            f'<img src="{prefix}{resolver(n)}" class="icon" alt="{n}"> {amt}x {n}'
            for n, amt in items.items()
        )

    @env.macro
    def materials_table():
        rows = [_icon_cell(icon) + f'<td>{name}</td>' for name, icon in MATERIALS_DB.items()]
        return _data_table(["", "Material"], rows)

    @env.macro
    def territory_table():
        rows = []
        for name, item in TERRITORY_DB.items():
            cost = item.get("cost")
            cost_cell = _mats_inline(cost, _mat_icon) if isinstance(cost, dict) else (cost if cost and cost != "None" else _EMPTY)
            usage = _multi(item.get("usage"))
            time  = _multi(item.get("time"))
            bonus = _multi(item.get("bonus"))
            rows.append(
                _icon_cell(item.get("icon","")) +
                f'<td>{name}</td><td>{usage}</td><td>{item.get("limit", _EMPTY)}</td>'
                f'<td>{time}</td><td>{cost_cell}</td><td>{bonus}</td>'
            )
        return _data_table(["", "Building", "Type", "Limit", "Build Time", "Cost", "Option"], rows)

    @env.macro
    def crop_table():
        rows = []
        for name, item in CROPS_DB.items():
            sp = item.get("sell_price")
            sell = " / ".join(str(x) for x in sp) if isinstance(sp, list) else (sp or _EMPTY)
            rows.append(
                _icon_cell(item.get("icon","")) +
                f'<td>{name}</td><td>{item.get("unlock_level", _EMPTY)}</td>'
                f'<td>{item.get("growth_time", _EMPTY)}</td><td>{item.get("seed_cost", _EMPTY)}</td>'
                f'<td>{item.get("exp", _EMPTY)}</td><td>{sell}</td>'
            )
        return _data_table(["", "Crop", "Unlock Lv.", "Growth", "Seed", "EXP", "Sell (N/R/L)"], rows)

    @env.macro
    def dish_table():
        rows = []
        for name, item in DISHES_DB.items():
            rows.append(
                _icon_cell(item.get("icon","")) +
                f'<td>{name}</td><td>{item.get("unlock_level", _EMPTY)}</td>'
                f'<td>{item.get("sell_price", _EMPTY)}</td><td>{_multi(item.get("bonus"))}</td>'
                f'<td>{_mats_inline(item.get("ingredients"), _ingredient_icon)}</td>'
            )
        return _data_table(["", "Dish", "Unlock Lv.", "Sell", "Bonus", "Recipe"], rows)

    @env.macro
    def tool_table():
        rows = []
        for name, item in TOOLS_DB.items():
            rows.append(
                _icon_cell(item.get("icon","")) +
                f'<td>{name}</td><td>{item.get("level", _EMPTY)}</td>'
                f'<td>{item.get("local_points", _EMPTY)}</td><td>{_multi(item.get("stats"))}</td>'
                f'<td>{_mats_inline(item.get("materials"), _mat_icon)}</td>'
            )
        return _data_table(["", "Tool", "Level", "Local Pts", "Stats", "Materials"], rows)