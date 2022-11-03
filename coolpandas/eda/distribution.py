import pandas as pd

from coolpandas.plot import barplot, distplot


def plot_discrete_distribution(summary: pd.DataFrame, nbins: int = 10) -> None:
    """Plot a discrete feature distribution.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        nbins (int, optional): Number of bins. Defaults to 10.
    """
    column: str = summary.columns[0]
    fig = distplot(
        summary,
        x_axis=column,
        y_axis="percentage",
        title=f"{column} value counts",
        hover_data={
            "count": True,
        },
        labels={
            "count": "Count",
            "percentage": "Percentage",
        },
        subtitle=f"Distribution of {summary.columns[0]} in DataFrame.",
        nbins=nbins,
        text_auto=True
        # text="count",
    )
    fig.update_layout(yaxis={"ticksuffix": "%", "range": [0, 100]})
    fig.show()


def plot_ordinal_distribution(summary: pd.DataFrame) -> None:
    """Plot an ordinal feature distribution.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
    """
    column: str = summary.columns[0]
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
        subtitle=f"Distribution for {summary.columns[0]} in DataFrame.",
        text="count",
    )
    fig.update_layout(yaxis={"ticksuffix": "%", "range": [0, 100]})
    fig.update_traces(width=1)
    fig.show()


def get_groupby_ordinal_distribution(
    data_frame: pd.DataFrame,
    groupby_column: str,
    plot: bool = True,
) -> pd.DataFrame:
    """Get the distribution overview of a DataFrame ordinal column grouped by size.

    Args:
        data_frame (pd.DataFrame): DataFrame to get distribution overview.
        groupby_column (str): Column to group by.

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
        plot_ordinal_distribution(summary)
    return summary
