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

# Print results
print("Vector:", vector)
print("3x3 Matrix:", matrix_3x3)
print("Identity Matrix:", identity_matrix)
print("Random 3x3x3 Array:", random_array_3x3x3)
print("10x10 Random Array:", random_array_10x10)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)