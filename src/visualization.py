
import numpy as np
import matplotlib.pyplot as plt


def plot_constellation(symbols, title, filename):
    """
    Plot the constellation diagram of complex modulation symbols.
    """
    plt.figure(figsize=(6, 6))

    plt.scatter(
        np.real(symbols),
        np.imag(symbols),
        s=15,
        alpha=0.6
    )

    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)

    plt.xlabel("In-phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title(title)

    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()

    plt.savefig(filename, dpi=300)
    plt.close()


def plot_spectrum(signal, sample_rate, title, filename):
    """
    Plot the magnitude spectrum of a complex baseband signal.
    """
    num_samples = len(signal)

    spectrum = np.fft.fftshift(np.fft.fft(signal))
    frequencies = np.fft.fftshift(
        np.fft.fftfreq(num_samples, d=1 / sample_rate)
    )

    magnitude_db = 20 * np.log10(
        np.maximum(np.abs(spectrum) / num_samples, 1e-12)
    )

    plt.figure(figsize=(9, 4))

    plt.plot(frequencies, magnitude_db)

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title(title)

    plt.grid(True)
    plt.tight_layout()

    plt.savefig(filename, dpi=300)
    plt.close()
