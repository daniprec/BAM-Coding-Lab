from pathlib import Path

import pandas as pd
import pytest


def build_sample_data(save_path):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    df.to_csv(save_path, index=False)


@pytest.fixture
def data_path():
    save_path = Path("test/sample_data.csv")
    build_sample_data(save_path)  # Setup phase
    yield save_path  # Provide the resource to the test function
    Path.unlink(save_path)  # Teardown phase


def test_add_column(data_path:Path):
    df = pd.read_csv(data_path)
    expected_result = pd.Series([5, 7, 9])
    pd.testing.assert_series_equal(df.sum(axis=1), expected_result)
