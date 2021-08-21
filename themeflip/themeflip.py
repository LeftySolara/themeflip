"""themeflip.py

This is the main script for ThemeFlip.
"""

from args import parse_args
from config import create_config_dir
import sys


def main():
    args = parse_args(sys.argv[1:])
    create_config_dir()


if __name__ == "__main__":
    main()
