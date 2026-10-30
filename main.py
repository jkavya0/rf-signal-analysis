from src.demodulation import (
    bpsk_demodulate,
    qpsk_demodulate,
    psk8_demodulate
)
import numpy as np
from src.analysis import calculate_ber

from src.modulation import (
    bpsk_modulate,
    qpsk_modulate,
    psk8_modulate
)
from src.visualization import plot_constellation, plot_spectrum
# Test binary input
bits = np.array([
    0, 0, 0,
    0, 1, 0,
    1, 1, 0,
    1, 0, 1
])

# Generate modulated symbols
bpsk_symbols = bpsk_modulate(bits)
qpsk_symbols = qpsk_modulate(bits)
psk8_symbols = psk8_modulate(bits)

# Display results
print("Input bits:", bits)

print("\nBPSK symbols:")
print(bpsk_symbols)

print("\nQPSK symbols:")
print(qpsk_symbols)

print("\n8PSK symbols:")
print(psk8_symbols)

# Verify unit magnitude
assert np.allclose(np.abs(bpsk_symbols), 1.0)
assert np.allclose(np.abs(qpsk_symbols), 1.0)
assert np.allclose(np.abs(psk8_symbols), 1.0)

print("\nAll modulation tests passed!")

from src.channel import add_awgn
from src.modulation import qpsk_modulate

# ----------------------------------
# AWGN CHANNEL VALIDATION
# ----------------------------------

# Generate a large random binary sequence
rng = np.random.default_rng(42)

num_bits = 120_000

random_bits = rng.integers(
    0, 2, num_bits
)

# Generate 60,000 QPSK symbols
tx_signal = qpsk_modulate(random_bits)

print("\nAWGN CHANNEL VALIDATION")
print("Number of transmitted symbols:", len(tx_signal))

snr_levels = [20, 10, 5, 0]

for index, snr_db in enumerate(snr_levels):

    channel_rng = np.random.default_rng(100 + index)

    # Pass signal through AWGN channel
    rx_signal = add_awgn(
        tx_signal,
        snr_db,
        rng=channel_rng
    )

    # Extract noise
    noise = rx_signal - tx_signal

    # Calculate signal power
    signal_power = np.mean(
        np.abs(tx_signal) ** 2
    )

    # Calculate noise power
    noise_power = np.mean(
        np.abs(noise) ** 2
    )

    # Calculate measured SNR
    measured_snr = 10 * np.log10(
        signal_power / noise_power
    )

    print(
        f"Target: {snr_db:2d} dB | "
        f"Measured: {measured_snr:.2f} dB"
    )

print("\nAWGN validation completed!")

# ----------------------------------
# RECEIVER AND DEMODULATION TEST
# ----------------------------------

print("\nRECEIVER VALIDATION")

rng = np.random.default_rng(42)

# Generate binary input
test_bits = rng.integers(0, 2, 1200)

modulation_functions = {
    "BPSK": (bpsk_modulate, bpsk_demodulate),
    "QPSK": (qpsk_modulate, qpsk_demodulate),
    "8PSK": (psk8_modulate, psk8_demodulate)
}

for name, (modulate, demodulate) in modulation_functions.items():

    # Ensure bit length is valid for each modulation
    bits_per_symbol = int(np.log2(
        {"BPSK": 2, "QPSK": 4, "8PSK": 8}[name]
    ))

    bits = test_bits[:(
        len(test_bits) // bits_per_symbol
    ) * bits_per_symbol]

    # Transmitter
    tx_symbols = modulate(bits)

    # Ideal channel: no noise
    rx_symbols = tx_symbols.copy()

    # Receiver
    recovered_bits = demodulate(rx_symbols)

    # Verify recovered bits
    errors = np.sum(bits != recovered_bits)

    print(
        f"{name}: "
        f"Transmitted bits = {len(bits)}, "
        f"Recovered bits = {len(recovered_bits)}, "
        f"Bit errors = {errors}"
    )

    assert np.array_equal(bits, recovered_bits)

print("\nAll receiver tests passed!")

# ----------------------------------
# BER PERFORMANCE ANALYSIS
# ----------------------------------

import matplotlib.pyplot as plt

print("\nBER PERFORMANCE ANALYSIS")

# Modulation schemes
modulations = {
    "BPSK": (bpsk_modulate, bpsk_demodulate, 1),
    "QPSK": (qpsk_modulate, qpsk_demodulate, 2),
    "8PSK": (psk8_modulate, psk8_demodulate, 3)
}

# Test SNR values
snr_values = np.arange(0, 15, 2)

# Number of transmitted bits
num_bits = 120_000

# Generate reproducible binary data
rng = np.random.default_rng(42)
test_bits = rng.integers(0, 2, num_bits)

# Store BER results
ber_results = {}

for name, (modulate, demodulate, bits_per_symbol) in modulations.items():

    # Ensure input length is divisible by bits per symbol
    valid_length = (
        num_bits // bits_per_symbol
    ) * bits_per_symbol

    bits = test_bits[:valid_length]

    ber_values = []

    for snr_db in snr_values:

        # Transmitter
        tx_symbols = modulate(bits)

        # AWGN channel
        channel_rng = np.random.default_rng(
            1000 + int(snr_db) + bits_per_symbol * 100
        )

        rx_symbols = add_awgn(
            tx_symbols,
            snr_db,
            rng=channel_rng
        )

        # Receiver
        recovered_bits = demodulate(rx_symbols)

        # Calculate BER
        ber = calculate_ber(
            bits,
            recovered_bits
        )

        ber_values.append(ber)

        print(
            f"{name:5s} | "
            f"SNR: {snr_db:2d} dB | "
            f"BER: {ber:.6f}"
        )

    ber_results[name] = ber_values


# ----------------------------------
# Plot BER versus SNR
# ----------------------------------

plt.figure(figsize=(9, 6))

for name, ber_values in ber_results.items():

    # Replace zero BER with NaN for logarithmic plotting
    plot_values = [
        value if value > 0 else np.nan
        for value in ber_values
    ]

    plt.semilogy(
        snr_values,
        plot_values,
        marker="o",
        label=name
    )

plt.title("BER Performance of Digital Modulation Schemes")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

plt.savefig(
    "results/ber_comparison.png",
    dpi=300
)

plt.close()
print("BER plot saved successfully!")

print("\nBER analysis completed!")
# Visualisation experiment
rng = np.random.default_rng(42)

num_bits = 2000
bits = rng.integers(0, 2, num_bits)

# Generate QPSK symbols
symbols = qpsk_modulate(bits)

# Add noise
received = add_awgn(symbols, snr_db=5, rng=rng)

# Plot transmitted and received constellation
plot_constellation(
    symbols[:500],
    "QPSK Transmitted Constellation",
    "results/qpsk_transmitted.png"
)

plot_constellation(
    received[:500],
    "QPSK Received Constellation (5 dB SNR)",
    "results/qpsk_received.png"
)

# Plot frequency spectrum
plot_spectrum(
    received,
    sample_rate=100000,
    title="QPSK Complex Baseband Spectrum",
    filename="results/qpsk_spectrum.png"
)

print("Constellation and spectrum plots saved.")