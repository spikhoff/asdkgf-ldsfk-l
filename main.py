import numpy as np
import matplotlib.pyplot as plt

# Define the Riemann zeta function for real values greater than 1
def zeta(s, n_terms=1000):
    return sum(1 / (n ** s) for n in range(1, n_terms + 1))

# Generate values of s from 1.1 to 3
s_values = np.linspace(1.1, 3, 100)
zeta_values = [zeta(s) for s in s_values]

# Plot the zeta function
plt.plot(s_values, zeta_values)
plt.xlabel('s')
plt.ylabel('ζ(s)')
plt.title('Riemann Zeta Function for Real Values of s > 1')
plt.grid(True)
plt.show()
