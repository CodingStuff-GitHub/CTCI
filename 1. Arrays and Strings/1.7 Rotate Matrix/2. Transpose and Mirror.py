def rotate_matrix(matrix):
    # Transpose a matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse the row of the matrix
        matrix[i].reverse()
    return matrix


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8],
      [9, 10, 11, 12], [13, 14, 15, 16]]))
