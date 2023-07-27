"""Test shape function."""
from unittest.mock import MagicMock, patch

import pandas as pd

from coolpandas import eda


@patch("coolpandas.eda.shape.display", return_value=None)
@patch("builtins.print")
def test_get_shape(
    mock_print: MagicMock, mock_display: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test get_shape function."""
    eda.get_shape(test_dataframe, display_summary=False)
    eda.get_shape(test_dataframe)
    assert mock_display.call_count == 1
    assert mock_print.call_count == 3
