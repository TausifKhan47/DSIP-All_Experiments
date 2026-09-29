import numpy as np
import matplotlib.pyplot as plt

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Compute the FFT
fft_result = np.fft.fft(signal)

# Compute magnitude and phase spectrum
magnitude_spectrum = np.abs(fft_result)
phase_spectrum = np.angle(fft_result)

# Compute the IFFT
reconstructed_signal = np.fft.ifft(fft_result)

# Display results
print("Original Signal:")
print(signal)

print("\nFFT Result:")
print(fft_result)

print("\nMagnitude Spectrum:")
print(magnitude_spectrum)

print("\nPhase Spectrum:")
print(phase_spectrum)

print("\nReconstructed Signal:")
print(reconstructed_signal)

# Plot
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(signal)
plt.title("Original Signal")

plt.subplot(3, 1, 2)
plt.stem(magnitude_spectrum)
plt.title("Magnitude Spectrum")

plt.subplot(3, 1, 3)
plt.stem(phase_spectrum)
plt.title("Phase Spectrum")

plt.tight_layout()
plt.show()