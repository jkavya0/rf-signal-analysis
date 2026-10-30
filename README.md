# Digital RF Signal Simulation and Modulation Analysis

A digital communication and Software-Defined Radio (SDR) simulation project developed using Python and GNU Radio.

## Project Overview

This project explores digital modulation techniques, communication channels, receiver processing, and signal performance analysis. It combines Python-based simulations with GNU Radio flowgraphs to demonstrate key concepts in digital communications.

## Implemented Features

- **Digital modulation:** BPSK, QPSK, 8-PSK and 16-QAM signal generation.
- **Channel simulation:** Additive White Gaussian Noise (AWGN) channel modelling.
- **Receiver processing:** Demodulation and matched-filtering experiments.
- **Performance analysis:** Bit Error Rate (BER) analysis and comparison of modulation schemes.
- **Signal visualisation:** Time-domain signals, frequency spectra, constellation diagrams and BER plots.
- **GNU Radio experiments:** QPSK and 16-QAM transmitter/channel/receiver flowgraphs.

## Project Structure

```text
rf-signal-analysis/
├── experiments/
│   ├── qpsk_sdr_simulation.grc.grc
│   ├── qpsk_sdr_simulation.py
│   ├── qam16_sdr_simulation.grc.grc
│   ├── qam16_sdr_simulation.py
│   └── calculate_ber.py
├── results/
│   ├── ber_comparison.png
│   ├── qpsk_received.png
│   ├── qpsk_spectrum.png
│   └── qpsk_transmitted.png
├── src/
│   ├── modulation.py
│   ├── channel.py
│   ├── demodulation.py
│   ├── analysis.py
│   └── visualization.py
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- GNU Radio
- GNU Radio Companion
- Git

## Running the Python Simulation

Clone the repository and install dependencies:

```bash
git clone https://github.com/jkavya0/rf-signal-analysis.git
cd rf-signal-analysis

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Run the main simulation:

```bash
python main.py
```

Run the tests:

```bash
pytest
```

## GNU Radio Experiments

The `experiments/` directory contains GNU Radio Companion flowgraphs and their generated Python scripts for QPSK and 16-QAM simulations.

Open the `.grc` flowgraphs in GNU Radio Companion to inspect and run the transmitter, channel and receiver chains.

## Project Objective

The objective is to gain practical experience with digital modulation, RF communication system simulation, SDR workflows, receiver signal processing and communication-system performance analysis.
