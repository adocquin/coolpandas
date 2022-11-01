"""Test duplicates.py functions."""
from unittest.mock import MagicMock, patch

import pandas as pd
from numpy.testing import assert_equal

from redpandas import eda


@patch("redpandas.eda.duplicates.display", return_value=None)
@patch("builtins.print")
def test_duplicated_rows(
    mock_print: MagicMock, mock_display: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test duplicated_rows function."""
    duplicated_rows: pd.DataFrame = eda.duplicated_rows(
        test_dataframe, display_summary=False, drop=False
    )
    assert duplicated_rows.empty

    test_dataframe_duplicated: pd.DataFrame = pd.concat(
        [test_dataframe, test_dataframe.head()]
    )
    duplicated_rows: pd.DataFrame = eda.duplicated_rows(
        test_dataframe_duplicated, display_summary=False, drop=False
    )
    assert len(duplicated_rows) == 4

    eda.duplicated_rows(test_dataframe_duplicated, display_summary=True, drop=False)
    eda.duplicated_rows(test_dataframe_duplicated, display_summary=True, drop=True)
    assert_equal(
        test_dataframe_duplicated.fillna(0).values, test_dataframe.fillna(0).values
    )
    assert mock_print.call_count == 6
    assert mock_display.call_count == 2


@patch("redpandas.eda.duplicates.display", return_value=None)
@patch("builtins.print")
def test_duplicated_columns(
    mock_print: MagicMock, mock_display: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test duplicated_columns function."""
    duplicated_columns: list[str] = eda.duplicated_columns(
        test_dataframe, display_summary=False, drop=False
    )
    assert duplicated_columns.empty

    test_dataframe_duplicated: pd.DataFrame = test_dataframe.copy()
    test_dataframe_duplicated["test"] = test_dataframe_duplicated["Animal"]
    duplicated_columns: list[str] = eda.duplicated_columns(
        test_dataframe_duplicated, display_summary=False, drop=False
    )
    assert duplicated_columns.columns == ["test"]

    eda.duplicated_columns(test_dataframe_duplicated, display_summary=True, drop=False)
    eda.duplicated_columns(test_dataframe_duplicated, display_summary=True, drop=True)
    assert_equal(
        test_dataframe_duplicated.columns.values, test_dataframe.columns.values
    )
    assert mock_print.call_count == 6
    assert mock_display.call_count == 2