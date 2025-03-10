import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Histogram of 1000 random values from a normal distribution
plt.figure(figsize=(8, 6))
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color='c', alpha=0.7, edgecolor='black')

# Customize the plot
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histogram of Normally Distributed Data', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)

# Show the histogram
plt.show()

# 3D Surface Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Define x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig.colorbar(surf)

# Customize the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot: $f(x, y) = \cos(x^2 + y^2)$')

# Show the 3D plot
plt.show()

# Bar Chart of Sales Data
plt.figure(figsize=(8, 6))
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['b', 'r', 'g', 'c', 'm']
plt.bar(products, sales, color=colors, alpha=0.7, edgecolor='black')

# Customize the plot
plt.xlabel('Products', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Sales Data for Different Products', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Show the bar chart
plt.show()