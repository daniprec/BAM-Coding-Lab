from pathlib import Path

import pandas as pd
import pytest


def build_sample_data(save_path):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    df.to_csv(save_path, index=False)


@pytest.fixture
def sample_data(tmp_path):
    save_path = tmp_path / "sample.csv"
    build_sample_data(save_path)  # Setup phase
    yield save_path  # Provide the resource to the test function
    Path.unlink(save_path)  # Teardown phase


def test_add_column(sample_data):
    df = pd.read_csv(sample_data)
    df["z"] = df["x"] + df["y"]
    expected_result = pd.Series([5, 7, 9])
    pd.testing.assert_series_equal(df["z"], expected_result)
