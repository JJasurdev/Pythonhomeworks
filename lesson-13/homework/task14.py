import numpy as np

# Define a 3x3 matrix A
A = np.array([[2, -1, 3], 
              [1, 0, 2], 
              [4, 1, 5]])

# Define a 3x1 column vector b
b = np.array([[5], 
              [3], 
              [10]])

# Solve for x
x = np.linalg.solve(A, b)

# Print the solution
print("Solution vector x:")
print(x)
