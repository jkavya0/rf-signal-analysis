
import numpy as np
import pytest

from src.analysis import calculate_ber


def test_zero_ber():
    transmitted = np.array([0, 1, 0, 1])
    received = np.array([0, 1, 0, 1])

    assert calculate_ber(transmitted, received) == 0.0


def test_nonzero_ber():
    transmitted = np.array([0, 1, 0, 1])
    received = np.array([0, 0, 0, 1])

    assert calculate_ber(transmitted, received) == 0.25


def test_invalid_input_lengths():
    transmitted = np.array([0, 1, 0])
    received = np.array([0, 1])

    with pytest.raises(ValueError):
        calculate_ber(transmitted, received)
