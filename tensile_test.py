import numpy as np
import matplotlib.pyplot as plt

# Define Material Properties
E = 200e9           # Young's Modulus (Pascals)
sigma_y = 250e6     # Yield Strength (Pascals)
H = 10e9            # Hardening Modulus (Pascals)
epsilon_f = 0.2     # Failure Strain

# Specimen Geometry
L_0 = 0.1          # Initial Length (meters)
A_0 = 1e-4         # Initial Cross-sectional Area (square meters)


# Strain Increment Setup
strain = np.linspace(0, epsilon_f, 1000)
stress = np.zeros_like(strain)


# Constitutive Laws 
epsilon_y = sigma_y / E

for i, eps in enumerate(strain):
    if eps <= epsilon_y:
        stress[i] = E * eps
    else:
        stress[i] = sigma_y + H * (eps - epsilon_y)


# Calculate Force and Elongation
force = stress * A_0
elongation = strain * L_0


# Plotting
plt.figure(figsize=(8, 5))
plt.plot(strain, stress / 1e6)
plt.xlabel("Engineering Strain")
plt.ylabel("Engineering Stress (MPa)")
plt.title("Simulated Tensile Test")
plt.grid(True)
plt.show()
