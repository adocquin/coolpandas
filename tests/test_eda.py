"""Tests eda.py module."""
from unittest.mock import patch

import pandas as pd
from numpy.testing import assert_equal

from redpandas import eda


class TestFigure:
    """Test Figure class."""

    def update_yaxes(self, range: list[int, int]) -> None:
        """Mock update_yaxes method."""
        pass

    def show(self) -> None:
        """Mock show method."""
        pass


@patch("redpandas.eda.barplot", return_value=TestFigure())
def test_missing_values(mock_barplot, test_dataframe) -> None:
    """Test missing_values function."""
    null_data_frame: pd.DataFrame = eda.missing_values(test_dataframe, plot=False)
    assert_equal(null_data_frame["null_values"].values, [2, 1])
    assert_equal(null_data_frame["percentage"].values, [50, 25])
    assert mock_barplot.call_count == 0
    null_data_frame: pd.DataFrame = eda.missing_values(test_dataframe, plot=True)
    mock_barplot.assert_called_once()
