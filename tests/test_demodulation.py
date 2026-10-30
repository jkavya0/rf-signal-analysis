
import numpy as np

from src.modulation import (
    bpsk_modulate,
    qpsk_modulate,
    psk8_modulate,
)

from src.demodulation import (
    bpsk_demodulate,
    qpsk_demodulate,
    psk8_demodulate,
)


def test_bpsk_demodulation():
    bits = np.array([0, 1, 1, 0])
    symbols = bpsk_modulate(bits)

    recovered = bpsk_demodulate(symbols)

    np.testing.assert_array_equal(recovered, bits)


def test_qpsk_demodulation():
    bits = np.array([0, 0, 0, 1, 1, 0, 1, 1])
    symbols = qpsk_modulate(bits)

    recovered = qpsk_demodulate(symbols)

    np.testing.assert_array_equal(recovered, bits)



def test_8psk_demodulation():
    bits = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1])
    symbols = psk8_modulate(bits)

    recovered = psk8_demodulate(symbols)

    np.testing.assert_array_equal(recovered, bits)

