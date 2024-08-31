def solution(inputString):
    dic = {}
    for i in inputString:
        if i not in dic:
            dic[i] = 1
            print(dic)
        else:
            dic[i] += 1
            print(dic)
    print(dic)
    odd = 0
    for j in dic.values():
        if j % 2 == 1:
            odd += 1
    return not odd >= 2
        
print(solution(''))
solution('aabb')