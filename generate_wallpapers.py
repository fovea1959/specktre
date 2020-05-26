#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Generate a new set of wallpapers for all my devices.

I use the standard screen resolution for desktops/laptops, and the
parallax sizes for iOS devices: http://dekoapp.com/parallax/
"""

import os

from specktre.colors import RGBColor
from specktre.cli import Settings
from specktre.specktre import save_speckled_wallpaper
from specktre.tilings import generate_hexagons, generate_squares, generate_triangles

OUTPUT_PATH = 'output'


wallpaper_config = [
    # iMac: purple hexagons
    (generate_hexagons,  2560, 1440, RGBColor(55, 19, 78),  RGBColor(72, 27, 100), 'imac-wallpaper'),

    # MacBook: red squares
    (generate_squares,   2304, 1440, RGBColor(178, 26, 16), RGBColor(136, 25, 17), 'macbook-wallpaper'),

    # iPhone: blue triangles on the lock screen, black on the home screen
    (generate_triangles,  744, 1392, RGBColor(18, 18, 18),  RGBColor(11, 11, 11),  'iphone-lock'),
    (generate_triangles,  744, 1392, RGBColor(13, 16, 155), RGBColor(14, 58, 180), 'iphone-home'),

    # iPad: green triangles on the lock screen, black on the home screen
    (generate_triangles, 2524, 2524, RGBColor(18, 18, 18),  RGBColor(11, 11, 11),  'ipad-lock'),
    (generate_triangles, 2524, 2524, RGBColor(11, 153, 46), RGBColor(6, 86, 9),    'ipad-home'),

    # Demo wallpapers
    (generate_squares,   400, 400, RGBColor(178, 26, 16), RGBColor(136, 25, 17),   'demo_sq'),
    (generate_triangles, 400, 400, RGBColor(255, 204, 0), RGBColor(255, 238, 56),  'demo_tr'),
    (generate_hexagons,  400, 400, RGBColor(56, 56, 255), RGBColor(0, 0, 194),     'demo_hex'),
]


if __name__ == '__main__':
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    for wallpaper in wallpaper_config:
        settings = list(wallpaper)
        settings[-1] = os.path.join(OUTPUT_PATH, settings[-1] + '.png')
        settings = Settings(*settings)

        save_speckled_wallpaper(settings)
