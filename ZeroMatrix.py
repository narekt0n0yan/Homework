def zeromatrix(image: list):
    matrix_list = []
    for _ in range(len(image)): 
        a = []       
        for __ in range(len(image[0])):
            a.append(0)
        matrix_list.append(a)
    return matrix_list


print(zeromatrix([[7,4,0,1], 
                  [5,6,2,2], 
                  [6,10,7,8], 
                  [1,4,2,0]]))






