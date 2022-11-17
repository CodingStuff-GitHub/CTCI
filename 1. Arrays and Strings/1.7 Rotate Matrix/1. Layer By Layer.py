# INCOMPLETE SOLUTION START AGAIN MAYBE
# Four layers at a time can be rotated
# temp = top, top = right, right = left, left = temp
# Every layer will have one constant i.e row or column maybe differing by layer number.
# This will help other part i.e row or column which can be used to get single index in second loop
# Remember that it should only be done half times of toltal rows and columns

def rotate_matrix(matrix):
    N = len(matrix) - 1
    for layer in range(len(matrix)//2):
        for i in range(layer, N - layer):
            # Top into temp
            temp = matrix[layer][i]
            # Top <- Left
            matrix[layer][i] = matrix[N - i][layer]
            # Left <- Bottom
            matrix[N - i][layer] = matrix[N - layer][N - i]
            # Bottom <- Right
            matrix[N - layer][N - i] = matrix[i][N - layer]
            # Right <- Top(temp)
            matrix[i][N - layer] = temp
    return matrix


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print(rotate_matrix([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]]))

print(rotate_matrix([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]]))
