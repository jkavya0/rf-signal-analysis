
"""
Performance analysis module.

Provides BER calculation for digital communication systems.
"""

import numpy as np


def calculate_ber(
    transmitted_bits: np.ndarray,
    received_bits: np.ndarray
) -> float:
    """
    Calculate Bit Error Rate.

    BER = Number of erroneous bits / Total transmitted bits.
    """

    transmitted_bits = np.asarray(transmitted_bits)
    received_bits = np.asarray(received_bits)

    if transmitted_bits.ndim != 1 or received_bits.ndim != 1:
        raise ValueError("Bit sequences must be one-dimensional.")

    if transmitted_bits.size == 0:
        raise ValueError("Bit sequences cannot be empty.")

    if transmitted_bits.shape != received_bits.shape:
        raise ValueError("Bit sequences must have equal lengths.")

    if not np.all(np.isin(transmitted_bits, [0, 1])):
        raise ValueError("Transmitted data must be binary.")

    if not np.all(np.isin(received_bits, [0, 1])):
        raise ValueError("Received data must be binary.")

    # Count positions where transmitted and received bits differ
    error_count = np.count_nonzero(
        transmitted_bits != received_bits
    )

    # Calculate BER
    ber = error_count / transmitted_bits.size

    return float(ber)
