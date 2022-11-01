"""Test plot.py module."""
import plotly.graph_objects as go
from numpy.testing import assert_equal

from redpandas import plot


def test_format_title() -> None:
    """Test format_title function."""
    assert plot.format_title("Test") == "<b>Test</b>"
    assert (
        plot.format_title("Test", "Subtitle")
        == '<b>Test</b><br><span style="font-size: 14px;">Subtitle</span>'
    )


def test_barplot(test_dataframe) -> None:
    """Test barplot function."""
    fig: go.Figure = plot.barplot(
        data_frame=test_dataframe, x_axis="Animal", y_axis="Legs", title="Test"
    )
    assert fig.data[0].type == "bar"
    assert_equal(fig.data[0].x, ("cat", "Dog", "Fish", "Lemur"))
    assert_equal(fig.data[0].y, ("4", None, None, "2"))
    assert fig.layout.title.text is not None
