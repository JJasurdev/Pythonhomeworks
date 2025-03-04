import numpy as np

# Create a 5x5 random matrix
matrix = np.random.randint(1, 10, (5, 5))

# Compute row-wise sums
row_sums = np.sum(matrix, axis=1)

# Compute column-wise sums
col_sums = np.sum(matrix, axis=0)

# Print the results
print("Matrix:")
print(matrix)
print("\nRow-wise sums:")
print(row_sums)
print("\nColumn-wise sums:")
print(col_sums)
