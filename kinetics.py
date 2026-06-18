import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. Define the Differential Equation (dA/dt = -k * A)
def reaction_model(A, t, k):
    dAdt = -k * A
    return dAdt

# 2. Set Parameters (Initial state)
A0 = 1.0  # Initial concentration of A (mol/L)
k = 0.5   # Reaction rate constant (1/s)

# Time points: 0 to 10 seconds, divided into 50 points
t = np.linspace(0, 10, 50)

# 3. Solve the ODE using SciPy
A_t = odeint(reaction_model, A0, t, args=(k,))

print("Calculated Concentration at t=10s: " + str(round(A_t[-1][0], 4)) + " mol/L")

# 4. Plot the results
plt.plot(t, A_t, color='red', linewidth=2, label='Reactant A decay')
plt.xlabel('Time (seconds)')
plt.ylabel('Concentration (mol/L)')
plt.title('First-Order Reaction Kinetics')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('kinetics_plot.png')
print("Simulation complete. Graph saved as 'kinetics_plot.png'")
