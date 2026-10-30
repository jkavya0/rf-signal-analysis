
import numpy as np

tx = np.fromfile("tx_bits.dat", dtype=np.uint8)
rx = np.fromfile("rx_bits.dat", dtype=np.uint8)

max_offset = 100
best_errors = len(rx)
best_offset = 0
best_length = 0

for offset in range(-max_offset, max_offset + 1):

    if offset >= 0:
        length = min(len(tx) - offset, len(rx))
        tx_part = tx[offset:offset + length]
        rx_part = rx[:length]
    else:
        length = min(len(tx), len(rx) + offset)
        tx_part = tx[:length]
        rx_part = rx[-offset:-offset + length]

    errors = np.count_nonzero(tx_part != rx_part)

    if errors < best_errors:
        best_errors = errors
        best_offset = offset
        best_length = length

print("TX bits:", len(tx))
print("RX bits:", len(rx))
print("Best alignment offset:", best_offset)
print("Compared bits:", best_length)
print("Bit errors:", best_errors)
print("BER:", best_errors / best_length)
