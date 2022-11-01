"""pytest tests configuration."""
import pandas as pd
import pytest


@pytest.fixture
def test_dataframe() -> pd.DataFrame:
    """Returns a test DataFrame."""
    return pd.DataFrame(
        {
            "Animal": ["cat", "Dog", "Fish", "Lemur"],
            "Legs": ["4", None, None, "2"],
            "Height": [30, 80, 7, None],
        }
    )


class FigureMock:
    """Mock a Figure object."""

    def update_layout(self, **kwargs) -> None:
        """Mock update_yaxes method."""
        return

    def show(self) -> None:
        """Mock show method."""
        return


@pytest.fixture
def mock_figure() -> FigureMock:
    """Returns a mock Figure."""
    return FigureMock()
