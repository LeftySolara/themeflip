"""config.py

This file contains functionality for managing ThemeFlip's
configuration directory.
"""

from pathlib import Path

DEFAULT_CONFIG_DIR = Path("~/.config/themeflip")
THEME_DIR_NAME = "themes"


def create_config_dir(path=DEFAULT_CONFIG_DIR):
    """Creates a config directory at the given path.

    Parameters
    ----------
    path : pathlib.Path object
        Path for the new directory.
    """
    config_full_path = path.expanduser()
    if not config_full_path.exists():
        config_full_path.mkdir(parents=True)
        theme_dir = config_full_path / THEME_DIR_NAME
        theme_dir.mkdir()
