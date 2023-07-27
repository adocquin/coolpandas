import math

import numpy as np
import pandas as pd

from coolpandas.plot import confusion_matrix


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
        fig = confusion_matrix(data_frame, **kwargs)
        fig.show()
    return correlation_matrix
