import numpy as np
import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Define x values
x = np.linspace(-2, 2, 400)

# Top-left: f(x) = x^3
axes[0, 0].plot(x, x**3, color='b')
axes[0, 0].set_title('$f(x) = x^3$')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('y')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

# Top-right: f(x) = sin(x)
x_sin = np.linspace(0, 2 * np.pi, 400)
axes[0, 1].plot(x_sin, np.sin(x_sin), color='r')
axes[0, 1].set_title('$f(x) = \sin(x)$')
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('y')
axes[0, 1].grid(True, linestyle='--', alpha=0.6)

# Bottom-left: f(x) = e^x
x_exp = np.linspace(-2, 2, 400)
axes[1, 0].plot(x_exp, np.exp(x_exp), color='g')
axes[1, 0].set_title('$f(x) = e^x$')
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('y')
axes[1, 0].grid(True, linestyle='--', alpha=0.6)

# Bottom-right: f(x) = log(x+1) for x >= 0
x_log = np.linspace(0, 10, 400)
axes[1, 1].plot(x_log, np.log(x_log + 1), color='m')
axes[1, 1].set_title('$f(x) = \log(x+1)$')
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('y')
axes[1, 1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

# Scatter Plot of 100 random points
plt.figure(figsize=(8, 6))
x_scatter = np.random.uniform(0, 10, 100)
y_scatter = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)
plt.scatter(x_scatter, y_scatter, c=colors, cmap='viridis', alpha=0.75, edgecolors='black')

# Customize the plot
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.title('Scatter Plot of Random Points', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)

# Show the scatter plot
plt.show()
