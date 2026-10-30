
import numpy as np

from src.channel import add_awgn


def test_awgn_preserves_signal_length():
    signal = np.ones(1000, dtype=complex)

    received = add_awgn(
        signal,
        snr_db=10,
        rng=np.random.default_rng(42),
    )

    assert len(received) == len(signal)


def test_awgn_changes_signal():
    signal = np.ones(1000, dtype=complex)

    received = add_awgn(
        signal,
        snr_db=10,
        rng=np.random.default_rng(42),
    )

    assert not np.array_equal(received, signal)


def test_awgn_achieves_approximately_requested_snr():
    signal = np.ones(100000, dtype=complex)

    received = add_awgn(
        signal,
        snr_db=10,
        rng=np.random.default_rng(42),
    )

    noise = received - signal

    measured_snr = 10 * np.log10(
        np.mean(np.abs(signal) ** 2) /
        np.mean(np.abs(noise) ** 2)
    )

    assert abs(measured_snr - 10) < 0.2
