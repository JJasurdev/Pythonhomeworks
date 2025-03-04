import numpy as np

# Create a 3x3 random matrix
matrix = np.random.randint(1, 10, (3, 3))

# Create a 3-element column vector
vector = np.random.randint(1, 10, (3, 1))

# Compute the matrix-vector product
result = np.dot(matrix, vector)

# Print the results
print("Matrix:")
print(matrix)
print("\nVector:")
print(vector)
print("\nMatrix-Vector Product:")
print(result)
