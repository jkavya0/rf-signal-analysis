
import numpy as np
import pytest

from src.modulation import (
    bpsk_modulate,
    qpsk_modulate,
    psk8_modulate,
)


def test_bpsk_output():
    bits = np.array([0, 1])
    symbols = bpsk_modulate(bits)

    assert len(symbols) == 2
    np.testing.assert_allclose(np.abs(symbols), 1.0)


def test_qpsk_output():
    bits = np.array([0, 0, 0, 1, 1, 0, 1, 1])
    symbols = qpsk_modulate(bits)

    assert len(symbols) == 4
    np.testing.assert_allclose(np.abs(symbols), 1.0)



def test_8psk_output():
    bits = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1])
    symbols = psk8_modulate(bits)

    assert len(symbols) == 3
    np.testing.assert_allclose(np.abs(symbols), 1.0)



def test_invalid_modulation_input():
    with pytest.raises(ValueError):
        qpsk_modulate(np.array([0, 1, 0]))
