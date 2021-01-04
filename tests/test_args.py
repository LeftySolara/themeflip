from themeflip.args import parse_args


def test_no_args():
    args = parse_args([])
    assert vars(args) == {
        "save": None,
        "load": None,
        "load_random": False,
        "show": None,
        "list": False,
    }


def test_save():
    args = parse_args(["-s", "nord"])
    assert args.save == "nord"
    args = parse_args(["--save", "nord"])
    assert args.save == "nord"


def test_load():
    args = parse_args(["-l", "gruvbox"])
    assert args.load == "gruvbox"
    args = parse_args(["--load", "gruvbox"])
    assert args.load == "gruvbox"


def test_load_random():
    args = parse_args(["--load-random"])
    assert args.load_random is True


def test_show():
    args = parse_args(["--show", "nord"])
    assert args.show == "nord"


def test_list():
    args = parse_args(["--list"])
    assert args.list is True
