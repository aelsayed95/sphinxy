def test_import() -> None:
    from sphinxy import Riddle, Sphinx

    assert Riddle("What has a head and a tail, but no body?", "Coin")
    assert Sphinx("Sphinxy")
