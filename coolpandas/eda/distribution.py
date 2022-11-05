"""Get a DataFrame column distribution overview."""
import pandas as pd

from coolpandas.plot import distplot


def plot_distribution(
    summary: pd.DataFrame,
    groupby_column: str,
    nbins: int = 100,
    title: str = "",
    subtitle: str = "",
    **kwargs,
) -> None:
    """Plot a feature distribution.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        groupby_column (str): Column to group by.
        nbins (int, optional): Number of bins. Defaults to 10.
        title (str, optional): Title of the plot. Defaults to "".
        subtitle (str, optional): Subtitle of the plot. Defaults to "".
        **kwargs: Keyword arguments to pass to distplot.
    """
    column: str = summary.columns[0]
    if not title:
        title = f"{column} distribution"
    if not subtitle:
        subtitle = f"Distribution for {summary.columns[0]} in DataFrame."
    if not kwargs.get("color"):
        kwargs["text_auto"] = True
    fig = distplot(
        summary,
        x_axis=groupby_column,
        y_axis=None,
        title=title,
        labels={
            "count": "Count",
        },
        subtitle=subtitle,
        histnorm="percent",
        nbins=nbins,
        **kwargs,
    )
    fig.update_yaxes(tickformat=".3")
    fig.update_layout(
        yaxis={"ticksuffix": "%", "range": [0, 100]},
        yaxis_title="Percentage",
        barmode="overlay",
    )
    if kwargs.get("color"):
        fig.update_traces(opacity=0.75)
    fig.show()


def get_groupby_distribution(
    data_frame: pd.DataFrame,
    groupby_column: str,
    data_type: str,
    plot: bool = True,
    **kwargs,
) -> pd.DataFrame:
    """Get the distribution overview of a DataFrame ordinal column grouped by size.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        groupby_column (str): Column to group by.
        data_type (str): Data type to get distribution overview.
        plot (bool, optional): Plot the distribution. Defaults to True.
        **kwargs: Keyword arguments to pass to plot_distribution.

    Returns:
        pd.DataFrame: DataFrame value counts summary.
    """
    if plot and data_type == "categorical":
        kwargs["nbins"] = data_frame[groupby_column].nunique()
    elif plot and data_type == "numerical":
        kwargs["marginal"] = "box"
        if not kwargs.get("nbins"):
            kwargs["nbins"] = 31
    if plot and not kwargs.get("title"):
        kwargs["title"] = f"{groupby_column} distribution"
    if plot:
        plot_distribution(
            data_frame,
            groupby_column,
            **kwargs,
        )
    summary: pd.DataFrame = (
        data_frame.groupby(groupby_column)
        .size()
        .to_frame()
        .reset_index()
        .rename(columns={0: "count"})
    )
    summary["percentage"] = round(summary["count"] / summary["count"].sum() * 100, 2)
    if data_type == "numerical":
        summary = summary[groupby_column].to_frame().describe()
    return summary
