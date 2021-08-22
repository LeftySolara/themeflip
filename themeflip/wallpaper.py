"""wallpaper.py

Functions for managing and setting wallpapers associated with themes.
"""

from config import DEFAULT_CONFIG_DIR, THEME_DIR_NAME

import json
import os
import sys


def get_wallpapers(theme):
    """Gets the paths to wallpapers for a theme.

    Parameters
    ----------
    theme : string
        The name of the theme to fetch wallpapers for.
    """
    config_path = os.path.expanduser(
        f"{DEFAULT_CONFIG_DIR}/{THEME_DIR_NAME}/{theme}/{theme}.json"
    )

    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            walls = " ".join(config["wallpapers"])
        return walls

    except FileNotFoundError:
        print(f'Error: no theme named "{theme}" found.', file=sys.stderr)


def set_wallpapers(path):
    """Sets the desktop wallpaper using the file at the given path.

        If using feh, a space-separated list of n paths will set the wallpaper for n monitors.

    Parameters
    ----------
    path : string
        The path to the wallpaper file.
    """
    # TODO let user provide options to pass to feh, or user another program for setting wallpaper
    print("Setting wallpaper...")
    command = f"feh --no-fehbg --bg-scale {path} > /dev/null 2>&1"
    status = os.system(command)

    if os.waitstatus_to_exitcode(status) != 0:
        print(
            f"Unable to set wallpaper. Please check the path and verify the file exists.",
            file=sys.stderr,
        )
