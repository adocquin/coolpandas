"""Test features_type.py functions."""
from unittest.mock import MagicMock, patch

import pandas as pd

from coolpandas import eda


@patch("builtins.print")
def test_categorical_features(
    mock_print: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test categorical_features function."""
    categorical_features: list[str] = eda.categorical_features(
        test_dataframe, display_summary=False
    )
    assert categorical_features == ["Animal", "Legs"]
    eda.categorical_features(test_dataframe, display_summary=True)
    assert mock_print.call_count == 2


@patch("builtins.print")
def test_numerical_features(
    mock_print: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test numerical_features function."""
    numerical_features: list[str] = eda.numerical_features(
        test_dataframe, display_summary=False
    )
    assert numerical_features == ["Height"]
    eda.numerical_features(test_dataframe, display_summary=True)
    assert mock_print.call_count == 2


@patch("builtins.print")
def test_boolean_features(mock_print: MagicMock, test_dataframe: pd.DataFrame) -> None:
    """Test boolean_features function."""
    boolean_features: list[str] = eda.boolean_features(
        test_dataframe, display_summary=False
    )
    assert boolean_features == ["Legs"]
    eda.boolean_features(test_dataframe, display_summary=True)
    assert mock_print.call_count == 2


@patch("builtins.print")
def test_zero_variance_features(
    mock_print: MagicMock, test_dataframe: pd.DataFrame
) -> None:
    """Test zero_variance_features function."""
    test_dataframe_zero_variance: pd.DataFrame = test_dataframe.copy()
    test_dataframe_zero_variance["zero_variance"] = 0
    zero_variance_features: list[str] = eda.zero_variance_features(
        test_dataframe_zero_variance, display_summary=False
    )
    assert zero_variance_features == ["zero_variance"]
    eda.zero_variance_features(test_dataframe, display_summary=True)
    assert mock_print.call_count == 2
