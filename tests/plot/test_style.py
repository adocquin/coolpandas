"""Test style.py functions."""
from redpandas.plot.style import format_title


def test_format_title() -> None:
    """Test format_title function."""
    assert format_title("Test") == "<b>Test</b>"
    assert (
        format_title("Test", "Subtitle")
        == '<b>Test</b><br><span style="font-size: 14px;">Subtitle</span>'
    )
