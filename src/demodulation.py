
"""
Digital demodulation module.

Implements a phase-based M-PSK receiver
for BPSK, QPSK and 8PSK.
"""

import numpy as np


def mpsk_demodulate(
    received_symbols: np.ndarray,
    M: int
) -> np.ndarray:
    """
    Detect M-PSK symbols and recover the original bits.

    Parameters
    ----------
    received_symbols : np.ndarray
        Complex received baseband symbols.
    M : int
        Modulation order (2, 4, or 8).

    Returns
    -------
    np.ndarray
        Recovered binary sequence.
    """

    if M not in (2, 4, 8):
        raise ValueError("M must be 2, 4, or 8.")

    received_symbols = np.asarray(received_symbols)

    if received_symbols.ndim != 1 or received_symbols.size == 0:
        raise ValueError("Input must be a non-empty 1D array.")

    if not np.all(np.isfinite(received_symbols)):
        raise ValueError("Received symbols must be finite.")

    if np.any(np.abs(received_symbols) == 0):
        raise ValueError("Cannot detect the phase of a zero-valued symbol.")

    # Number of bits represented by each symbol
    bits_per_symbol = int(np.log2(M))

    # Estimate received phase
    received_phase = np.angle(received_symbols)

    # Convert phase into symbol indices
    symbol_indices = np.rint(
        np.mod(received_phase, 2 * np.pi) * M / (2 * np.pi)
    ).astype(int) % M

    # Convert symbol indices back into binary groups
    shifts = np.arange(bits_per_symbol - 1, -1, -1)

    recovered_bits = (
        (symbol_indices[:, None] >> shifts) & 1
    )

    return recovered_bits.reshape(-1)


def bpsk_demodulate(received_symbols: np.ndarray) -> np.ndarray:
    return mpsk_demodulate(received_symbols, M=2)


def qpsk_demodulate(received_symbols: np.ndarray) -> np.ndarray:
    return mpsk_demodulate(received_symbols, M=4)


def psk8_demodulate(received_symbols: np.ndarray) -> np.ndarray:
    return mpsk_demodulate(received_symbols, M=8)
