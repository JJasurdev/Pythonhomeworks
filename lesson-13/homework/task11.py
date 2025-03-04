import numpy as np

# Create a 3x3 matrix
matrix = np.array([[2, 3, 1], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Calculate the determinant
determinant = np.linalg.det(matrix)

# Print the determinant
print("Matrix:")
print(matrix)
print("\nDeterminant:", determinant)
