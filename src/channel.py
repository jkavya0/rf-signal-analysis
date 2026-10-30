
"""
AWGN channel model.

Adds complex Gaussian noise to a transmitted
baseband signal at a specified sample SNR.
"""

import numpy as np


def add_awgn(
    signal: np.ndarray,
    snr_db: float,
    rng: np.random.Generator | None = None
) -> np.ndarray:
    """
    Add complex AWGN to a signal.

    Parameters
    ----------
    signal : np.ndarray
        Input complex baseband signal.
    snr_db : float
        Target signal-to-noise ratio in dB.
    rng : np.random.Generator, optional
        Random number generator for reproducibility.

    Returns
    -------
    np.ndarray
        Received signal containing AWGN.
    """

    signal = np.asarray(signal)

    if signal.ndim != 1 or signal.size == 0:
        raise ValueError("Signal must be a non-empty 1D array.")

    if not np.all(np.isfinite(signal)):
        raise ValueError("Signal must contain finite values.")

    if not np.isfinite(snr_db):
        raise ValueError("SNR must be finite.")

    if not np.iscomplexobj(signal):
        raise ValueError("Input signal must be complex.")

    if rng is None:
        rng = np.random.default_rng()

    # Calculate average signal power
    signal_power = np.mean(np.abs(signal) ** 2)

    if signal_power <= 0:
        raise ValueError("Signal power must be greater than zero.")

    # Convert SNR from dB to linear scale
    snr_linear = 10 ** (snr_db / 10)

    # Calculate required total complex noise power
    noise_power = signal_power / snr_linear

    # Generate independent Gaussian noise for I and Q
    noise = np.sqrt(noise_power / 2) * (
        rng.standard_normal(signal.size)
        + 1j * rng.standard_normal(signal.size)
    )

    # Received signal = transmitted signal + noise
    received_signal = signal + noise

    return received_signal
