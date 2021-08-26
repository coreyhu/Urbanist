#!/bin/sh
set -e

echo ".
GENERATING FONTS
."
gftools builder config.yaml


echo ".
SLICING ROMAN/ITALIC
."

fonttools varLib.instancer ../fonts/variable/Urbanist\[ital,wght\].ttf ital=0 -o ../fonts/variable/Urbanist\[wght\].ttf --update-name-table
fonttools varLib.instancer ../fonts/variable/Urbanist\[ital,wght\].ttf ital=1 -o ../fonts/variable/Urbanist-Italic\[wght\].ttf --update-name-table

echo ".
POST-PROCESSING ADJUSTMENTS
."
python3 ../scripts/postprocess.py 

echo ".
VALIDATING FONTS
."
fontbakery check-googlefonts -l FAIL com.google.fonts/check/ftxvalidator ../fonts/variable/Urbanist-Italic\[wght\].ttf ../fonts/variable/Urbanist\[wght\].ttf

fontbakery check-googlefonts -l FAIL com.google.fonts/check/ftxvalidator ../fonts/ttf/*.ttf

echo ".
COMPLETE
."