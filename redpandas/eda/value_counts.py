"""value_counts function for pandas DataFrame."""
import pandas as pd

from ..plot import barplot


def plot_value_counts(summary: pd.DataFrame) -> None:
    """Plot a DataFrame column value counts overview.

    Args:
        data_frame (pd.DataFrame): DataFrame to get value counts overview.
        column (str): Column to get value counts.
    """
    column: str = summary.columns[0]
    fig = barplot(
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
        subtitle=f"Value counts for {summary.columns[0]} in DataFrame.",
        text="count",
    )
    fig.update_layout(
        yaxis={"ticksuffix": "%", "range": [0, 100]},
        xaxis=dict(tickmode="array", tickvals=summary[column].values),
        showlegend=False,
    )
    fig.show()


def value_counts(
    data_frame: pd.DataFrame, column: str, plot: bool = True
) -> pd.DataFrame:
    """Get a DataFrame column value counts overview.

    Args:
        data_frame (pd.DataFrame): DataFrame to get value counts overview.
        column (str): Column to get value counts.

    Returns:
        pd.DataFrame: DataFrame value counts summary.
    """
    summary: pd.DataFrame = pd.DataFrame(data_frame[column].value_counts(dropna=False))
    summary.columns = ["count"]
    summary["percentage"] = round(
        data_frame[column].value_counts(dropna=False, normalize=True) * 100, 2
    )
    summary = summary.reset_index().rename(columns={"index": column})
    if plot:
        plot_value_counts(summary)
    return summary
