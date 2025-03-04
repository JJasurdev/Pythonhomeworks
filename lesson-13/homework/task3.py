import numpy as np

# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# Print results
print("Vector:", vector)
print("3x3 Matrix:", matrix_3x3)
print("Identity Matrix:", identity_matrix)
