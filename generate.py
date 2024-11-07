from catppuccin import PALETTE
import argparse

parser = argparse.ArgumentParser(
    description="Generate a Catppuccin theme for Cosmic Desktop"
)
parser.add_argument(
    "flavor",
    type=str,
    metavar="theme flavor",
    nargs="?",
    default="mocha",
    help="The flavor of the theme to generate. Can be 'mocha', 'frappe', 'macchiato', or 'latte'.",
)
parser.add_argument(
    "--accent",
    "-a",
    type=str,
    metavar="accent color",
    nargs="?",
    default="lavender",
    dest="accent",
    help="The accent color to use for the theme.",
)
parser.add_argument(
    "--bg-alpha",
    "-b",
    type=float,
    metavar="background alpha",
    nargs="?",
    default=1,
    dest="bg_alpha",
    help="The alpha value of the background color.",
)
parser.add_argument(
    "--frosted",
    "-f",
    type=bool,
    metavar="frosted effect",
    dest="is_frosted",
    default=False,
    help="Whether to use frosted glass effect for the theme.",
)
parser.add_argument(
    "--outer-gap",
    "-o",
    type=int,
    metavar="outer gap size",
    nargs="?",
    default=0,
    dest="outer_gap_size",
    help="The size of the outer gap.",
)
parser.add_argument(
    "--inner-gap",
    "-i",
    type=int,
    metavar="inner gap size",
    nargs="?",
    default=8,
    dest="inner_gap_size",
    help="The size of the inner gap.",
)
parser.add_argument(
    "--active-hint",
    "-ah",
    type=int,
    metavar="active hint size",
    nargs="?",
    default=3,
    dest="active_hint_size",
    help="The size of the active hint.",
)
parser.add_argument(
    "--roundness",
    "-r",
    type=str,
    metavar="roundness",
    nargs="?",
    default="round",
    choices=["round", "slightly round", "square"],
    dest="roundness",
    help="The roundness of the corners. Can be 'round', 'slightly round', or 'square'.",
)
parser.add_argument(
    "--window-hint-color",
    "-whc",
    type=str,
    metavar="window hint color",
    nargs="?",
    default=None,
    dest="window_hint_color",
    help="The color of the window hint.",
)
args = parser.parse_args()
flavor = args.flavor
accent = args.accent
bg_alpha = args.bg_alpha
is_frosted = args.is_frosted
outer_gap_size = args.outer_gap_size
inner_gap_size = args.inner_gap_size
active_hint_size = args.active_hint_size
roundness = args.roundness
window_hint_color = accent if args.window_hint_color is None else args.window_hint_color

palette_map = {
    "blue": "blue",
    "red": "red",
    "green": "green",
    "yellow": "yellow",
    "gray_1": "mantle",
    "gray_2": "base",
    "gray_3": "surface 0",
    "neutral_0": "crust",
    "neutral_1": "mantle",
    "neutral_2": "base",
    "neutral_3": "surface 0",
    "neutral_4": "surface 1",
    "neutral_5": "surface 2",
    "neutral_6": "overlay 0",
    "neutral_7": "overlay 1",
    "neutral_8": "overlay 2",
    "neutral_9": "subtext 0",
    "neutral_10": "subtext 1",
    "bright_green": "green",
    "bright_red": "red",
    "bright_orange": "peach",
    "ext_warm_grey": "overlay 2",
    "ext_orange": "peach",
    "ext_yellow": "yellow",
    "ext_blue": "blue",
    "ext_purple": "lavender",
    "ext_pink": "pink",
    "ext_indigo": "mauve",
    "accent_blue": "blue",
    "accent_red": "red",
    "accent_green": "green",
    "accent_warm_grey": "overlay 2",
    "accent_orange": "peach",
    "accent_yellow": "yellow",
    "accent_purple": "lavender",
    "accent_pink": "pink",
    "accent_indigo": "mauve",
}


bg_color_map = "base"
other_map = {
    "text_tint": "text",
    "accent": accent,
    "success": "green",
    "warning": "yellow",
    "destructive": "red",
    "window_hint": window_hint_color,
}
if flavor != "latte":
    other_map["neutral_tint"] = "overlay 1"
    other_map["primary_container_bg"] = "surface 0"
    other_map["secondary_container_bg"] = "surface 1"

roundness_map = {
    "round": """    corner_radii: (
        radius_0: (0.0, 0.0, 0.0, 0.0),
        radius_xs: (4.0, 4.0, 4.0, 4.0),
        radius_s: (8.0, 8.0, 8.0, 8.0),
        radius_m: (16.0, 16.0, 16.0, 16.0),
        radius_l: (32.0, 32.0, 32.0, 32.0),
        radius_xl: (160.0, 160.0, 160.0, 160.0),
    ),""",
    "slightly round": """    corner_radii: (
        radius_0: (0.0, 0.0, 0.0, 0.0),
        radius_xs: (2.0, 2.0, 2.0, 2.0),
        radius_s: (8.0, 8.0, 8.0, 8.0),
        radius_m: (8.0, 8.0, 8.0, 8.0),
        radius_l: (8.0, 8.0, 8.0, 8.0),
        radius_xl: (8.0, 8.0, 8.0, 8.0),
    ),""",
    "square": """    corner_radii: (
        radius_0: (0.0, 0.0, 0.0, 0.0),
        radius_xs: (2.0, 2.0, 2.0, 2.0),
        radius_s: (2.0, 2.0, 2.0, 2.0),
        radius_m: (2.0, 2.0, 2.0, 2.0),
        radius_l: (2.0, 2.0, 2.0, 2.0),
        radius_xl: (2.0, 2.0, 2.0, 2.0),
    ),""",
}

catppuccin_colors = {}
for color in eval(f"PALETTE.{flavor}.colors"):
    catppuccin_colors[color.name.lower()] = color

print(
    f"""(
    palette: {"Light" if flavor == "latte" else "Dark"}((
        name: "Catppuccin-{flavor.capitalize()}-{accent.capitalize()}","""
)
for color in palette_map:
    catppuccin_color = catppuccin_colors[palette_map[color]]
    print(
        f"""        {color}: (
            red: {catppuccin_color.rgb.r/255:.8f},
            green: {catppuccin_color.rgb.g/255:.8f},
            blue: {catppuccin_color.rgb.b/255:.8f},
            alpha: 1.0,
        ),"""
    )
print("    )),")
print(
    """    spacing: (
        space_none: 0,
        space_xxxs: 4,
        space_xxs: 8,
        space_xs: 12,
        space_s: 16,
        space_m: 24,
        space_l: 32,
        space_xl: 48,
        space_xxl: 64,
        space_xxxl: 128,
    ),"""
)
print(roundness_map[roundness])
print(
    f"""    bg_color: Some((
        red: {catppuccin_colors[bg_color_map].rgb.r/255:.8f},
        green: {catppuccin_colors[bg_color_map].rgb.g/255:.8f},
        blue: {catppuccin_colors[bg_color_map].rgb.b/255:.8f},
        alpha: {bg_alpha},
    )),"""
)
for color in other_map:
    catppuccin_color = catppuccin_colors[other_map[color]]
    print(
        f"""    {color}: Some((
        red: {catppuccin_color.rgb.r/255:.8f},
        green: {catppuccin_color.rgb.g/255:.8f},
        blue: {catppuccin_color.rgb.b/255:.8f},
        alpha: 1.0,
    )),"""
    )
print(
    f"""    is_frosted: {"true" if is_frosted else "false"},
    gaps: ({outer_gap_size}, {inner_gap_size}),
    active_hint: {active_hint_size},
)"""
)
