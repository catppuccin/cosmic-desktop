from catppuccin import PALETTE

flavors = ["mocha", "frappe", "macchiato", "latte"]


def generate_color_scheme(flavor):
    color_map = {
        "foreground": "text",
        "cursor": "rosewater",
        "bright_foreground": "text",
        "dim_foreground": "overlay 0",
        "black": "subtext 1" if flavor == "latte" else "surface 1",
        "red": "red",
        "green": "green",
        "yellow": "yellow",
        "blue": "blue",
        "magenta": "pink",
        "cyan": "teal",
        "white": "surface 2" if flavor == "latte" else "subtext 1",
        "bright-black": "subtext 0" if flavor == "latte" else "surface 2",
        "bright-red": "red",
        "bright-green": "green",
        "bright-yellow": "yellow",
        "bright-blue": "blue",
        "bright-magenta": "pink",
        "bright-cyan": "teal",
        "bright-white": "surface 1" if flavor == "latte" else "subtext 0",
        "dim-black": "subtext 1" if flavor == "latte" else "surface 1",
        "dim-red": "red",
        "dim-green": "green",
        "dim-yellow": "yellow",
        "dim-blue": "blue",
        "dim-magenta": "pink",
        "dim-cyan": "teal",
        "dim-white": "surface 2" if flavor == "latte" else "subtext 1",
    }

    catppuccin_colors = {}
    for color in eval(f"PALETTE.{flavor}.colors"):
        catppuccin_colors[color.name.lower()] = color

    def get_color(name):
        return catppuccin_colors[color_map[name]].hex.upper()

    color_scheme = f"""(
        name: "Catppuccin {flavor.capitalize()}",
        foreground: "{get_color('foreground')}",
        cursor: "{get_color('cursor')}",
        bright_foreground: "{get_color('bright_foreground')}",
        dim_foreground: "{get_color('dim_foreground')}",
        normal: (
            black: "{get_color('black')}",
            red: "{get_color('red')}",
            green: "{get_color('green')}",
            yellow: "{get_color('yellow')}",
            blue: "{get_color('blue')}",
            magenta: "{get_color('magenta')}",
            cyan: "{get_color('cyan')}",
            white: "{get_color('white')}",
        ),
        bright: (
            black: "{get_color('bright-black')}",
            red: "{get_color('bright-red')}",
            green: "{get_color('bright-green')}",
            yellow: "{get_color('bright-yellow')}",
            blue: "{get_color('bright-blue')}",
            magenta: "{get_color('bright-magenta')}",
            cyan: "{get_color('bright-cyan')}",
            white: "{get_color('bright-white')}",
        ),
        dim: (
            black: "{get_color('dim-black')}",
            red: "{get_color('dim-red')}",
            green: "{get_color('dim-green')}",
            yellow: "{get_color('dim-yellow')}",
            blue: "{get_color('dim-blue')}",
            magenta: "{get_color('dim-magenta')}",
            cyan: "{get_color('dim-cyan')}",
            white: "{get_color('dim-white')}",
        ),
    )"""
    return color_scheme


for flavor in flavors:
    with open(f"./cosmic-term/Catppuccin-{flavor.capitalize()}.ron", "w") as f:
        f.write(generate_color_scheme(flavor))
