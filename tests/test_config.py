import themeflip.config


def test_create_config_dir(tmp_path):
    full_default_config_path = themeflip.config.DEFAULT_CONFIG_DIR.expanduser()
    config_dir = tmp_path / str(full_default_config_path)[1:]
    assert config_dir.exists() is False

    themeflip.config.create_config_dir(config_dir)
    assert config_dir.exists() is True

    content = "Sample config"
    test_file = config_dir / "config"
    test_file.write_text(content)

    assert test_file.read_text() == content
    assert len(list(tmp_path.iterdir())) == 1
