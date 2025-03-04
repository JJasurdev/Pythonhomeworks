import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 10]])

# Calculate the determinant
determinant = np.linalg.det(matrix)

# Print the determinant
print("Matrix:")
print(matrix)
print("\nDeterminant:", determinant)
