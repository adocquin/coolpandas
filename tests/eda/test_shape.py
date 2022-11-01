"""Test shape function."""
from unittest.mock import MagicMock, patch

import pandas as pd

from redpandas import eda


@patch("redpandas.eda.shape.display", return_value=None)
@patch("builtins.print")
def test_shape(
    mock_print: MagicMock, mock_display: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test data_shape function."""
    eda.shape(test_dataframe, display_summary=False)
    eda.shape(test_dataframe)
    assert mock_display.call_count == 1
    assert mock_print.call_count == 3
