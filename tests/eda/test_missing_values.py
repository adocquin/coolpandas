"""Tests missing_values.py functions."""
from unittest.mock import MagicMock, patch

import pandas as pd
from numpy.testing import assert_equal

from redpandas import eda
from redpandas.eda.missing_values import plot_missing_values


@patch("redpandas.eda.missing_values.barplot")
def test_plot_missing_values(mock_barplot: MagicMock, mock_figure: object) -> None:
    """Test plot_missing_values function."""
    mock_barplot.return_value = mock_figure
    plot_missing_values(pd.DataFrame())
    mock_barplot.assert_called_once()


@patch("redpandas.eda.missing_values.plot_missing_values")
def test_missing_values(
    mock_plot_missing_values: MagicMock,
    test_dataframe: pd.DataFrame,
    mock_figure: object,
) -> None:
    """Test missing_values function."""
    mock_plot_missing_values.return_value = mock_figure
    null_data_frame: pd.DataFrame = eda.missing_values(test_dataframe, plot=False)
    assert_equal(null_data_frame["null_values"].values, [2, 1])
    assert_equal(null_data_frame["percentage"].values, [50, 25])
    eda.missing_values(test_dataframe, plot=True)
    mock_plot_missing_values.assert_called_once()
