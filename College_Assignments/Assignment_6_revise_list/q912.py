# Define two 2D matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Initialize an empty matrix to store the result
result_matrix = []

# Iterate through rows
for i in range(len(matrix1)):
    # Initialize a new row to store the sum of corresponding elements
    row = []
    for j in range(len(matrix1[i])):
        # Add corresponding elements from both matrices
        row.append(matrix1[i][j] + matrix2[i][j])
    # Append the row to the result matrix
    result_matrix.append(row)

# Output the result matrix
print("Resultant Matrix after Addition:")
for row in result_matrix:
    print(row)
