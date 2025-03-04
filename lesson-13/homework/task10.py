import numpy as np

# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# Create a 3x3x3 array with random values
random_array_3x3x3 = np.random.rand(3, 3, 3)

# Create a 10x10 array with random values and find the minimum and maximum values
random_array_10x10 = np.random.rand(10, 10)
min_value = np.min(random_array_10x10)
max_value = np.max(random_array_10x10)

# Create a random vector of size 30 and find the mean value
random_vector_30 = np.random.rand(30)
mean_value = np.mean(random_vector_30)

# Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.rand(5, 5)
normalized_matrix = (random_matrix_5x5 - np.min(random_matrix_5x5)) / (np.max(random_matrix_5x5) - np.min(random_matrix_5x5))

# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
result_matrix = np.dot(matrix_5x3, matrix_3x2)

# Create two 3x3 matrices and compute their dot product
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product_matrix = np.dot(matrix_A, matrix_B)

# Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.rand(4, 4)
matrix_transpose = np.transpose(matrix_4x4)

# Print results
print("Vector:", vector)
print("3x3 Matrix:", matrix_3x3)
print("Identity Matrix:", identity_matrix)
print("Random 3x3x3 Array:", random_array_3x3x3)
print("10x10 Random Array:", random_array_10x10)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Random Vector of size 30:", random_vector_30)
print("Mean Value:", mean_value)
print("Normalized 5x5 Matrix:", normalized_matrix)
print("5x3 Matrix:", matrix_5x3)
print("3x2 Matrix:", matrix_3x2)
print("Matrix Product (5x3 * 3x2):", result_matrix)
print("Matrix A:", matrix_A)
print("Matrix B:", matrix_B)
print("Dot Product (A * B):", dot_product_matrix)
print("4x4 Matrix:", matrix_4x4)
print("Transpose of 4x4 Matrix:", matrix_transpose)