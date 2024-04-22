<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://github.com/pop-os/cosmic-epoch">COSMIC Desktop Environment</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/edenqwq/cosmic/stargazers"><img src="https://img.shields.io/github/stars/edenqwq/cosmic?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/edenqwq/cosmic/issues"><img src="https://img.shields.io/github/issues/edenqwq/cosmic?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/edenqwq/cosmic/contributors"><img src="https://img.shields.io/github/contributors/edenqwq/cosmic?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="assets/preview.webp"/>
</p>

## Previews

<details>
<summary>🌻 Latte</summary>
<img src="assets/latte.webp"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/frappe.webp"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/macchiato.webp"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/mocha.webp"/>
</details>

## Usage

### COSMIC Desktop Appearance

1. Clone this repository locally

```bash
git clone https://github.com/EdenQwQ/cosmic.git
```

2. Open COSMIC Settings and navigate to `Desktop -> Appearance`
3. Click `Import` and browse to where you cloned this repository
4. Select the desired theme under `cosmic-settings`

### COSMIC Terminal Color Scheme

1. Clone this repository locally
2. Open COSMIC Terminal and navigate to `View -> Color schemes...`
3. Click `Import` and browse to where you cloned this repository
4. Select the desired theme under `cosmic-term`

### Generating Custom Configs

`generate.py` allows you to generate custom configs for COSMIC Desktop.
You can use this script to generate a custom config with your preferred colors and other settings.

1. To use the script, you need to have `python` and `pip` installed on your system.
2. Clone this repository locally and cd into it

```bash
git clone https://github.com/EdenQwQ/cosmic.git
cd cosmic
```

3. Create a virtual environment and install the required dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Run the script with your desired options

```bash
$ python generate.py --help
usage: generate.py [-h] [--accent [accent color]]
                   [--bg-alpha [background alpha]] [--frosted frosted effect]
                   [--outer-gap [outer gap size]]
                   [--inner-gap [inner gap size]]
                   [--active-hint [active hint size]]
                   [--roundness [roundness]]
                   [--window-hint-color [window hint color]]
                   [theme flavor]

Generate a Catppuccino theme for Cosmic Desktop

positional arguments:
  theme flavor          The flavor of the theme to generate. Can be 'mocha',
                        'frappe', 'macchiato', or 'latte'.

options:
  -h, --help            show this help message and exit
  --accent [accent color], -a [accent color]
                        The accent color to use for the theme.
  --bg-alpha [background alpha], -b [background alpha]
                        The alpha value of the background color.
  --frosted frosted effect, -f frosted effect
                        Whether to use frosted glass effect for the theme.
  --outer-gap [outer gap size], -o [outer gap size]
                        The size of the outer gap.
  --inner-gap [inner gap size], -i [inner gap size]
                        The size of the inner gap.
  --active-hint [active hint size], -ah [active hint size]
                        The size of the active hint.
  --roundness [roundness], -r [roundness]
                        The roundness of the corners. Can be 'round',
                        'slightly round', or 'square'.
  --window-hint-color [window hint color], -whc [window hint color]
                        The color of the window hint.
```

## 💝 Thanks to

- [EdenQwQ](https://github.com/EdenQwQ)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
