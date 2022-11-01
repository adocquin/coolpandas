"""pytest tests configuration."""
import pandas as pd
import pytest


@pytest.fixture
def test_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Animal": ["cat", "Dog", "Fish", "Lemur"],
            "Legs": ["4", None, None, "2"],
            "Height": [30, 80, 7, None],
        }
    )
