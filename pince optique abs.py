import numpy as np

def F(r, z):
    # Define constants
    n_p = 1.55 # Example value, you should replace it with the actual value
    n_m = 1.33  # Example value, you should replace it with the actual value
    d = 1.0e-7  # Example value, you should replace it with the actual value
    c = 3.0e8  # Speed of light
    w_0 = 2400e-9  # Example value, you should replace it with the actual value
    lambda_ = 1200e-9  # Example value, you should replace it with the actual value
    P_0 = 50.0  # Example value, you should replace it with the actual value

   # Calculate the function
    part1 = np.pi * n_p * d**3 * (((n_p / n_m)**2 - 1) / (4 * c * (((n_p / n_m)**2) + 2)))
    part2 = np.exp(-2 * np.abs(r)**2 / (w_0**2 + np.abs(z) * lambda_ / (np.pi * n_m)))
    part3 = (-8 * P_0**2 * np.abs(r)) / (np.pi * w_0**3 * (1 + (np.abs(z)**2 * lambda_**2) / (np.pi * w_0**2 * n_m))**(3/2))
    part4 = ((-2 * P_0**2 * lambda_**2) / (np.pi**2 * w_0**3 * n_m * (1 + (np.abs(z)**2 * lambda_**2) / (np.pi * w_0**2 * n_m))**(3/2))) + (2 * np.abs(r)**2 * lambda_ / (np.pi * n_m * (w_0**2 + np.abs(z) * lambda_ / (np.pi * n_m))**2))
    
    # Return the vector components as separate arrays
    return part1 * part2 * np.array([part3, part4])

import matplotlib.pyplot as plt

# Define range for z and r
z_values = np.linspace(-100e-6, 100e-6, 1000)
r_values = np.linspace(-20e-6, 20e-6, 1000)

# Create meshgrid for z and r
Z, R = np.meshgrid(z_values, r_values)

# Calculate F for each combination of z and r
result = F(R, Z)

# Plot
plt.figure(figsize=(10, 6))
plt.contourf(Z, R, np.linalg.norm(result, axis=0), levels=50, cmap='viridis')
plt.colorbar(label='|F|')
plt.xlabel('z (m)')
plt.ylabel('r (m)')
plt.title('Valeur de F')
plt.grid(True)
plt.show()
