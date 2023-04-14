def test_import() -> None:
    from sphinxy.sphinx import Sphinx

    assert Sphinx("Sphinxy")
