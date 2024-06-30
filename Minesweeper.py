def solution(matrix: list):
    noChangematrix = matrix
    matrix_list = []
    for _ in range(len(matrix)): 
        a = []       
        for __ in range(len(matrix[0])):
            a.append(0)
        matrix_list.append(a)
    R = [[0,1],[0,-1],[1,1],[1,0],[1,-1],[-1,-1],[-1,0],[-1,1]]
    for i in range(len(noChangematrix)):
        for j in range(len(noChangematrix[i])):
            if noChangematrix[i][j] == True:
                for r in R:
                    if i+r[0] < 0  or j+r[1] < 0:
                        continue
                    elif i+r[0] >= len(matrix_list) or j+r[1] >= len(matrix_list[0]):
                        continue
                    matrix_list[i+r[0]][j+r[1]] += 1 

                    
                

    return matrix_list
    


print(solution([[True,False,False,True], 
                [False,False,True,False], 
                [True,True,False,True]]))