def solution(n, firstNumber):
    list_n = []
    for i in range(n):
        list_n.append(i)

    if firstNumber in list_n[:len(list_n)//2:1]:
       return firstNumber + len(list_n)//2
    return firstNumber - len(list_n)//2


print(solution(10,5))

# melamojann