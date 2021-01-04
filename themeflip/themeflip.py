"""ThemeFlip

This is the main script for ThemeFlip.
"""

from args import parse_args
import os
import sys

CONFIG_DIR = "~/.config/themeflip"
THEME_DIR = "themes"


def create_config_dir():
    """Creates a config directory in ~/.config if it does not exist."""

    config_full_path = os.path.expanduser(CONFIG_DIR)
    if not os.path.exists(config_full_path):
        os.makedirs(config_full_path + "/" + THEME_DIR)


parse_args(sys.argv[1:])
create_config_dir()
