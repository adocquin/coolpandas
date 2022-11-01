"""Plot functions for RedPandas."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

custom_template = {
    "layout": go.Layout(
        font={
            "family": "Nunito",
            "size": 12,
            "color": "#707070",
        },
        title={
            "font": {
                "family": "Lato",
                "size": 18,
                "color": "#1f1f1f",
            },
            "xref": "paper",
            "yref": "paper",
            "xanchor": "left",
            "x": 0,
        },
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        colorway=px.colors.qualitative.G10,
    )
}


def format_title(title: str, subtitle: str = None, subtitle_font_size: int = 14) -> str:
    """Format title and subtitle for plotly figures.

    Args:
        title (str): Title of the plot.
        subtitle (str, optional): Subtitle of the plot. Defaults to None.
        subtitle_font_size (int, optional): Font size of the subtitle. Defaults to 14.

    Returns:
        str: Formatted title.
    """
    title = f"<b>{title}</b>"
    if not subtitle:
        return title
    subtitle = f'<span style="font-size: {subtitle_font_size}px;">{subtitle}</span>'
    return f"{title}<br>{subtitle}"


def barplot(
    data_frame: pd.DataFrame,
    x_axis: str,
    y_axis: str,
    title: str,
    labels: dict[str, str] = None,
    hover_name: str = None,
    hover_data: dict[str, bool | str] = None,
    color: str = None,
    subtitle: str = None,
) -> go.Figure:
    """Create a bar plot.

    Args:
        data_frame (pd.DataFrame): DataFrame to plot.
        x (str): Column to use as x axis.
        y (str): Column to use as y axis.
        title (str): Title of the plot.
        labels (dict[str, str], optional): Labels for the plot. Defaults to None.
        hover_name (str, optional): Column to use as hover name. Defaults to None.
        hover_data (dict[str, bool | str], optional): Columns to use as hover data.
        Defaults to None.
        color (str, optional): Column to use as color. Defaults to None.
        subtitle (str, optional): Subtitle of the plot. Defaults to None.

    Returns:
        go.Figure: Bar plot figure.
    """
    fig = px.bar(
        data_frame,
        x=x_axis,
        y=y_axis,
        labels=labels,
        hover_name=hover_name,
        hover_data=hover_data,
        color=color,
        title=format_title(title, subtitle=subtitle),
        template=custom_template,
        width=800,
        height=400,
    )
    fig.update_xaxes(tickangle=270)
    fig.update_traces(width=0.5)
    return fig
