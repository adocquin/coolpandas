"""Correlation map function."""
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from .style import custom_template, format_title


def correlation_map(
    correlation_matrix: pd.DataFrame, title: str, subtitle: str = None, **kwargs
) -> go.Figure:
    """Create a correlation map.

    Args:
        correlation_matrix (pd.DataFrame): Correlation matrix to plot.
        title (str): Title of the plot.
        subtitle (str, optional): Subtitle of the plot. Defaults to None.

    Returns:
        go.Figure: Correlation map figure.
    """
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    fig = px.imshow(
        correlation_matrix.mask(mask),
        text_auto=True,
        zmin=-1,
        zmax=1,
        title=format_title(title, subtitle=subtitle),
        template=custom_template,
        width=1000,
        height=1000,
        **kwargs,
    )
    # fig: go.Heatmap = go.Heatmap(
    #     z=correlation_matrix.mask(mask),
    #     x=correlation_matrix.columns,
    #     y=correlation_matrix.columns,
    #     colorscale=px.colors.diverging.RdBu,
    #     zmin=-1,
    #     zmax=1,
    #     title=format_title(title, subtitle=subtitle),
    #     template=custom_template,
    #     width=800,
    #     height=400,
    #     **kwargs,
    # )
    return fig
