import argparse


def parse_args(args):
    """Parse arguments passed to the program at runtime.

    Parameters
    ----------
    args : list
        A list of cammand-line arguments that were passed to the program.
    """
    parser = argparse.ArgumentParser(description="Linux theme switcher")
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-s",
        "--save",
        help="save the current configuration as a new theme",
        metavar="THEME",
    )
    group.add_argument("-l", "--load", help="load a saved theme", metavar="THEME")
    group.add_argument(
        "--load-random",
        help="load a random saved theme",
        action="store_true",
        dest="load_random",
    )
    group.add_argument(
        "--show", help="display the configuration for a theme", metavar="THEME"
    )
    group.add_argument(
        "--list", help="display a list of saved themes", action="store_true"
    )

    return parser.parse_args(args)
