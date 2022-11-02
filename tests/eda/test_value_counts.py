"""Test value_counts.py function."""
from unittest.mock import MagicMock, patch

import pandas as pd
from numpy.testing import assert_equal

from coolpandas import eda
from coolpandas.eda.value_counts import plot_value_counts


@patch("coolpandas.eda.value_counts.barplot")
def test_plot_value_counts(mock_barplot: MagicMock, mock_figure: object) -> None:
    """Test plot_value_counts function."""
    mock_barplot.return_value = mock_figure
    plot_value_counts(pd.DataFrame({"Test": [0]}))
    assert mock_barplot.called


@patch("coolpandas.eda.value_counts.barplot")
def test_get_value_counts(
    mock_barplot: MagicMock,
    test_dataframe: pd.DataFrame,
    mock_figure: object,
) -> None:
    """Test get_value_counts function."""
    mock_barplot.return_value = mock_figure
    summary: pd.DataFrame = eda.get_value_counts(test_dataframe, "Legs", plot=False)
    assert_equal(summary["count"].values, [2, 1, 1])
    assert_equal(summary["percentage"].values, [50, 25, 25])
    eda.get_value_counts(test_dataframe, "Legs", plot=True)
    mock_barplot.assert_called_once()
