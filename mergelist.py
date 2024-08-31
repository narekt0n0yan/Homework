v1 = [12,3,44,5,56,6,87,8,] 
v2 = [23,45,67,74,74,7,75,845,8,45]
V = []
v1.sort()
v2.sort()

v1_index = 0
v2_index = 0
while   len(V) != len(v1) + len(v2):
    if v1[v1_index] > v2[v2_index]:
            V.append(v2[v2_index])
            if v2_index + 1  < len(v2):
                v2_index += 1
    else:
            V.append(v1[v1_index])
            if v1_index + 1 <len(v1):
                v1_index += 1





    print(V)
