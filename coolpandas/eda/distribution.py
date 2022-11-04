import pandas as pd

from coolpandas.plot import barplot, distplot


def plot_discrete_distribution(
    summary: pd.DataFrame,
    groupby_column: str,
    nbins: int = 100,
    title: str = "",
    subtitle: str = "",
) -> None:
    """Plot a discrete feature distribution.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        groupby_column (str): Column to group by.
        nbins (int, optional): Number of bins. Defaults to 10.
        title (str, optional): Title of the plot. Defaults to "".
        subtitle (str, optional): Subtitle of the plot. Defaults to "".
    """
    column: str = summary.columns[0]
    if not title:
        title = f"{column} distribution"
    if not subtitle:
        subtitle = f"Distribution for {summary.columns[0]} in DataFrame."
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
        text_auto=True,
        nbins=nbins,
    )
    fig.update_yaxes(tickformat=".3")
    fig.update_layout(
        yaxis={"ticksuffix": "%", "range": [0, 100]},
        yaxis_title="Percentage",
    )
    fig.show()


def plot_ordinal_distribution(summary: pd.DataFrame, subtitle: str = "") -> None:
    """Plot an ordinal feature distribution.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        subtitle (str, optional): Subtitle of the plot. Defaults to "".
    """
    column: str = summary.columns[0]
    if not subtitle:
        subtitle = f"Distribution for {summary.columns[0]} in DataFrame."
    fig = barplot(
        summary,
        x_axis=column,
        y_axis="percentage",
        title=f"{column} distribution",
        hover_data={
            "count": True,
        },
        labels={
            "count": "Count",
            "percentage": "Percentage",
        },
        subtitle=subtitle,
        text="count",
    )
    fig.update_layout(yaxis={"ticksuffix": "%", "range": [0, 100]})
    fig.update_traces(width=1)
    fig.show()


def get_groupby_ordinal_distribution(
    data_frame: pd.DataFrame,
    groupby_column: str,
    plot: bool = True,
    subtitle: str = "",
) -> pd.DataFrame:
    """Get the distribution overview of a DataFrame ordinal column grouped by size.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        groupby_column (str): Column to group by.
        plot (bool, optional): Plot the distribution. Defaults to True.
        subtitle (str, optional): Subtitle of the plot. Defaults to "".

    Returns:
        pd.DataFrame: DataFrame value counts summary.
    """
    summary: pd.DataFrame = (
        data_frame.groupby(groupby_column)
        .size()
        .to_frame()
        .reset_index()
        .rename(columns={0: "count"})
    )
    summary["percentage"] = round(summary["count"] / summary["count"].sum() * 100, 2)
    if plot:
        plot_ordinal_distribution(summary, subtitle=subtitle)
    return summary


def get_groupby_continuous_distribution(
    data_frame: pd.DataFrame,
    groupby_column: str,
    plot: bool = True,
    nbins: int = 31,
    title: str = "",
    subtitle: str = "",
) -> pd.DataFrame:
    """Get the distribution overview of a DataFrame continuous column grouped by size.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        groupby_column (str): Column to group by.
        plot (bool, optional): Plot the distribution. Defaults to True.
        nbins (int, optional): Number of bins. Defaults to 31.
        title (str, optional): Title of the plot. Defaults to "".
        subtitle (str, optional): Subtitle of the plot. Defaults to "".

    Returns:
        pd.DataFrame: DataFrame value counts summary.
    """
    if plot:
        plot_discrete_distribution(
            data_frame,
            groupby_column=groupby_column,
            nbins=nbins,
            title=title,
            subtitle=subtitle,
        )
    summary: pd.DataFrame = (
        data_frame.groupby(groupby_column)
        .size()
        .to_frame()
        .reset_index()
        .rename(columns={0: "count"})
    )
    summary["percentage"] = round(summary["count"] / summary["count"].sum() * 100, 2)
    return summary[groupby_column].to_frame().describe()
