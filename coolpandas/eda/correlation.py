import math

import pandas as pd

from coolpandas.plot import correlation_map


def get_correlation(
    data_frame: pd.DataFrame, method: str = "pearson", plot: bool = True, **kwargs
) -> pd.DataFrame:
    """Get the correlations of a DataFrame.

    Args:
        data_frame (pd.DataFrame): DataFrame to get correlations from.
        method (str, optional): Correlation method. Defaults to "pearson".
        plot (bool, optional): Plot the correlation map. Defaults to True.
        **kwargs: Keyword arguments to pass to pandas.DataFrame.corr.

    Returns:
        pd.DataFrame: Correlations.
    """
    correlation_matrix: pd.DataFrame = data_frame.corr(method=method)
    truncate: callable = lambda x: math.trunc(100 * x) / 100
    correlation_matrix = correlation_matrix.applymap(truncate)
    if plot:
        correlation_map(
            correlation_matrix, title=f"{method.capitalize()} correlation map", **kwargs
        ).show()
    return correlation_matrix
