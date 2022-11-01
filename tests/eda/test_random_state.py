"""Test random_state.py function."""
import os
import random

import numpy as np

from redpandas import eda


def test_random_state() -> None:
    """Test random_state function."""
    eda.random_state(0)
    assert random.getstate()[1][0] == 2147483648
    assert os.environ["PYTHONHASHSEED"] == "0"
    assert np.random.get_state()[1][0] == 0
