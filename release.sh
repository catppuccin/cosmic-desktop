#!/usr/bin/env bash

THEMES="mocha frappe macchiato latte"
ACCENTS="blue red green peach yellow lavender pink mauve"

for theme in $THEMES; do
  for accent in $ACCENTS; do
    python generate.py -a $accent $theme > "cosmic-settings/Catppuccin-${theme^}-${accent^}.ron"
  done
done

python cosmic-term.py
