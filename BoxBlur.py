from ZeroMatrix import zeromatrix
def solution(image: list):
    matrix_list = []
    for _ in range(len(image) - 2): 
        a = []       
        for __ in range(len(image[0]) - 2):
            a.append(0)
        matrix_list.append(a)
    
    
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[0])):
            matrix_list[i][j] = (image[i + 1][j + 1] 
                                 + image[i][j + 1] 
                                 + image[i + 2][j + 1] 
                                 + image[i + 1][j] 
                                 + image[i + 1][j + 2] 
                                 + image[i + 2][j + 2]
                                 + image[i + 2][j] 
                                 + image[i][j + 2] 
                                 + image[i][j]) // 9
    return matrix_list

    
print(solution([[36, 0, 18, 9, 9, 45, 27], 
                [27, 0, 54, 9, 0, 63, 90], 
                [81, 63, 72, 45, 18, 27, 0], 
                [0, 0, 9, 81, 27, 18, 45], 
                [45,  45, 27, 27, 90, 81, 72], 
                [45, 18, 9, 0, 9, 18, 45], 
                [27, 81, 36, 63, 63, 72, 81]]))

print(solution([[7, 4, 0, 1], 
                [5, 6, 2, 2], 
                [6, 10, 7, 8], 
                [1, 4, 2, 0]]))

