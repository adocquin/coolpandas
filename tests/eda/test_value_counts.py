"""Test value_counts.py function."""
from unittest.mock import MagicMock, patch

import pandas as pd
from numpy.testing import assert_equal

from redpandas import eda
from redpandas.eda.value_counts import plot_value_counts


@patch("redpandas.eda.value_counts.barplot")
def test_plot_value_counts(mock_barplot: MagicMock, mock_figure: object) -> None:
    """Test plot_value_counts function."""
    mock_barplot.return_value = mock_figure
    plot_value_counts(pd.DataFrame({"Test": [0]}))
    assert mock_barplot.called


@patch("redpandas.eda.value_counts.plot_value_counts")
def test_value_counts(
    mock_plot_value_counts: MagicMock,
    test_dataframe: pd.DataFrame,
    mock_figure: object,
) -> None:
    """Test value_counts function."""
    mock_plot_value_counts.return_value = mock_figure
    summary: pd.DataFrame = eda.value_counts(test_dataframe, "Legs", plot=False)
    assert_equal(summary["count"].values, [2, 1, 1])
    assert_equal(summary["percentage"].values, [50, 25, 25])
    eda.value_counts(test_dataframe, "Legs", plot=True)
    mock_plot_value_counts.assert_called_once()
