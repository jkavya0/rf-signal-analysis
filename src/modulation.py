
"""
Digital modulation module.

Implements M-PSK modulation for:
    - BPSK (M=2)
    - QPSK (M=4)
    - 8PSK (M=8)

The output is a complex baseband I/Q signal.
"""

import numpy as np


def mpsk_modulate(bits: np.ndarray, M: int) -> np.ndarray:
    """
    Map binary input data to M-PSK complex symbols.

    Parameters
    ----------
    bits : np.ndarray
        Binary input sequence containing only 0s and 1s.
    M : int
        Modulation order (2, 4, or 8).

    Returns
    -------
    np.ndarray
        Complex baseband modulation symbols.
    """

    # Validate modulation order
    if M not in (2, 4, 8):
        raise ValueError("M must be 2, 4, or 8.")

    # Convert input to NumPy array
    bits = np.asarray(bits)

    # Validate binary input
    if bits.ndim != 1 or not np.all(np.isin(bits, [0, 1])):
        raise ValueError("Input must be a 1D binary array.")

    # Number of bits represented by each symbol
    bits_per_symbol = int(np.log2(M))

    # Number of input bits must be divisible by bits per symbol
    if len(bits) % bits_per_symbol != 0:
        raise ValueError(
            f"Number of bits must be divisible by {bits_per_symbol}."
        )

    # Group binary data into symbols
    bit_groups = bits.reshape(-1, bits_per_symbol)

    # Convert each binary group into an integer symbol index
    weights = 2 ** np.arange(bits_per_symbol - 1, -1, -1)
    symbol_indices = bit_groups @ weights

    # Map symbol indices to phase values
    phase = 2 * np.pi * symbol_indices / M

    # Generate complex I/Q modulation symbols
    symbols = np.exp(1j * phase)

    return symbols


def bpsk_modulate(bits: np.ndarray) -> np.ndarray:
    """Generate BPSK modulation symbols."""
    return mpsk_modulate(bits, M=2)


def qpsk_modulate(bits: np.ndarray) -> np.ndarray:
    """Generate QPSK modulation symbols."""
    return mpsk_modulate(bits, M=4)


def psk8_modulate(bits: np.ndarray) -> np.ndarray:
    """Generate 8PSK modulation symbols."""
    return mpsk_modulate(bits, M=8)
