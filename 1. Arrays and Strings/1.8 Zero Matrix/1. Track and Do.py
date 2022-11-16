import itertools


def zero_matrix(matrix):
    rows_with_zeros = []
    columns_with_zeros = []
    # Count the zeros and add them in rows and columns with zeros
    for i, j in itertools.product(range(len(matrix)), range(len(matrix))):
        if matrix[i][j] == 0:
            rows_with_zeros.append(i)
            columns_with_zeros.append(j)

    # Loop through the length and convert columns and rows to zero
    for p in range(len(matrix)):
        for q in columns_with_zeros:
            matrix[p][q] = 0
        for q in rows_with_zeros:
            matrix[q][p] = 0
    return matrix


print(zero_matrix([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(zero_matrix([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
