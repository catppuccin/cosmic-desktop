<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://github.com/pop-os/cosmic-epoch">COSMIC Desktop Environment</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/catppuccin/cosmic-desktop/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/cosmic-desktop?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/cosmic-desktop/issues"><img src="https://img.shields.io/github/issues/catppuccin/cosmic-desktop?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/cosmic-desktop/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/cosmic-desktop?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
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
git clone https://github.com/catppuccin/cosmic-desktop.git
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

The included whiskers themes allow you to generate custom configs for COSMIC Desktop. You can use
them with the [`whiskers`](https://github.com/catppuccin/whiskers) program to generate
a custom config with your preferred colors and other settings.

1. [Install whiskers](https://github.com/catppuccin/whiskers#installation)
2. Clone this repository locally and cd into it

```bash
git clone https://github.com/catppuccin/cosmic-desktop.git
cd cosmic-desktop
```

3. Run `whiskers` with `--overrides` set to a JSON object with your desired options

```bash
whiskers templates/cosmic-settings.tera --overrides='{"roundness": "square", "window_hint_color": "peach", "bg_alpha": 0.8}'
```

## Available settings
- `accent`: The primary/accent color. May be any of the Catppuccin palette color names, or a list of color names. Defaults to rendering a version of the theme for every palette color.
- `roundness`: The roundness of the corners. Can be `round`, `slightlyround`, or `square`. Defaults to `round`.
- `window_hint_color`: The color of the window hint. May be any of the Catppuccin palette color names. Defaults to matching the accent color.
- `bg_alpha`: The alpha value (opacity) of the window background color. Must be a float between `0.0` and `1.0`. Defaults to `1.0`.
- `frosted`: Enables blurred transparency. Must be a boolean. Defaults to `false`.
- `outer_gap_size`: Compositor outer gap size. Must be an integer. Defaults to `0`.
- `inner_gap_size`: Compositor inner gap size. Must be an integer. Defaults to `8`.
- `active_hint_size`: Compositor active window hint outline width. Must be an integer. Defaults to `3`.

You can also use whiskers with `--flavor` to only render a single flavor (`latte`, `frappe`, `macchiato`, `mocha`).
By default, a version of the theme for all 4 flavors will be rendered.

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
