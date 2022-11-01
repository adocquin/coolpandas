"""RedPandas main EDA functions."""
import pandas as pd

from .plot import barplot


def missing_values(data_frame: pd.DataFrame, plot: bool = True) -> pd.DataFrame:
    """Get columns missing values statistics for a DataFrame.

    Args:
        data_frame (pd.DataFrame): DataFrame to get missing values statistics.
        plot (bool, optional): Whether to plot the missing values statistics.
        Defaults to True.

    Returns:
        pd.DataFrame: Missing values statistics as DataFrame.
    """
    null_values: pd.Series = data_frame.isna().sum()
    null_data_frame: pd.DataFrame = (
        null_values.reset_index()
        .rename(columns={"index": "column", 0: "null_values"})
        .sort_values(by="null_values", ascending=False)
    )
    null_data_frame["percentage"] = round(
        null_data_frame["null_values"] / data_frame.shape[0] * 100, 2
    )
    null_data_frame = null_data_frame[null_data_frame["null_values"] > 0]
    if plot:
        fig = barplot(
            null_data_frame,
            x_axis="column",
            y_axis="percentage",
            title="Missing values",
            hover_data={
                "null_values": True,
            },
            labels={
                "column": "Column",
                "null_values": "Missing values",
                "percentage": "Percentage",
            },
            subtitle="Percentage of missing values per column",
        )
        fig.update_yaxes(range=[0, 100])
        fig.show()
    return null_data_frame
