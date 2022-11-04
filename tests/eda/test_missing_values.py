"""Tests missing_values.py functions."""
from unittest.mock import MagicMock, patch

import pandas as pd
from numpy.testing import assert_equal

from coolpandas import eda
from coolpandas.eda.missing_values import plot_missing_values


@patch("coolpandas.eda.missing_values.barplot")
def test_plot_missing_values(mock_barplot: MagicMock, mock_figure: object) -> None:
    """Test plot_missing_values function."""
    mock_barplot.return_value = mock_figure
    plot_missing_values(pd.DataFrame())
    mock_barplot.assert_called_once()


@patch("coolpandas.eda.missing_values.barplot")
@patch("builtins.print")
def test_get_missing_values(
    mock_print: MagicMock,
    mock_barplot: MagicMock,
    test_dataframe: pd.DataFrame,
    mock_figure: object,
) -> None:
    """Test get_missing_values function."""
    mock_barplot.return_value = mock_figure
    null_data_frame: pd.DataFrame = eda.get_missing_values(test_dataframe, plot=False)
    assert_equal(null_data_frame["null_values"].values, [2, 1])
    assert_equal(null_data_frame["percentage"].values, [50, 25])
    eda.get_missing_values(test_dataframe, plot=True)
    assert mock_print.call_count == 2
    mock_barplot.assert_called_once()
