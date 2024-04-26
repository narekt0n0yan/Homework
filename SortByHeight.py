

def solution(a: list):
    new_list = []
    index_list = []
    for i in range(len(a)):
        if a[i] != -1:
            new_list.append(a[i])
        else:
            index_list.append(i)

    
    for _ in range(len(new_list)):
        for i in range(len(new_list)-1):
            if new_list[i] > new_list[i+1]:
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
    
    for i in index_list:
        new_list.insert(i, -1)
    return new_list


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))


