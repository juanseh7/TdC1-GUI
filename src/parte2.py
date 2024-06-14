import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Define the components
R = 50  # Ohms
C = 4.7e-8  # Farads
L = 0.001  # Henries

# Define the transfer function H(s)
# RC measuring on C --- Figura 2
# numerator = [1]
# denominator = [R * C, 1]
# system = ctl.TransferFunction(numerator, denominator)

# CR measuring on R --- Figura 3
# numerator = [R * C, 0]
# denominator = [R * C, 1]
# system = ctl.TransferFunction(numerator, denominator)

# RLC measuring on C --- Figura 4
# numerator = [1]
# denominator = [L * C, R * C, 1]
# system = ctl.TransferFunction(numerator, denominator)

# RCL measuring on L --- Figura 5
# numerator = [L * C, 0, 0]
# denominator = [L * C, R * C, 1]
# system = ctl.TransferFunction(numerator, denominator)

# CLR measuring on R --- Figura 6
# numerator = [R, 0]
# denominator = [L * C, R * C, 1]
# system = ctl.TransferFunction(numerator, denominator)

# RCL measuring on CL --- Figura 7
numerator = [L * C, 0, 1]
denominator = [L * C, R * C, 1]
system = ctl.TransferFunction(numerator, denominator)

# Compute the frequency response
frequencies = np.logspace(1, 6, 1000)  # from 10 Hz to 1 MHz
mag, phase, omega = ctl.bode(system, frequencies, plot=False)

f = omega / (2 * np.pi)  # Convert rad/s to Hz
mag = 20 * np.log10(mag)  # Convert to dB
phase = phase * (180 / np.pi) # Convert rad to degrees

# Plot the magnitude response
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(f, mag)
plt.title('Frequency Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.yticks(np.arange((int(min(mag)/10) - 1) * 10, (int((max(mag)+1)/10) + 1) * 10, 20))
plt.grid(True, which="both", ls="--")

# Plot the phase response
plt.subplot(2, 1, 2)
plt.semilogx(f, phase)  
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [°]')
plt.yticks(np.arange((int(min(phase)/10) - 1) * 10, (int((max(phase)+1)/10) + 1) * 10, 30))
plt.grid(True, which="both", ls="--")

plt.tight_layout()
plt.show()
