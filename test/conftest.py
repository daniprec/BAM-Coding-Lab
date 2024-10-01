import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--special", action="store_true", default=False, help="run special tests"
    )


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "special: mark test as special")


def pytest_collection_modifyitems(config: pytest.Config, items: list) -> None:
    if config.getoption("--special"):
        pass
    else:
        skip_special = pytest.mark.skip(reason="need --special option to run")
        for item in items:
            if "special" in item.keywords:
                item.add_marker(skip_special)
