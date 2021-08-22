"""themeflip.py

This is the main script for ThemeFlip.
"""

from args import parse_args
from config import create_config_dir
import wallpaper
import os
import sys


def main():
    args = parse_args(sys.argv[1:])
    create_config_dir()

    if args.load:
        walls = wallpaper.get_wallpapers(args.load)
        if walls:
            wallpaper.set_wallpapers(walls)


if __name__ == "__main__":
    main()
