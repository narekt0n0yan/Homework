def solution(inputArray):
    max_product = 0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i+1] - inputArray[i]) > max_product:
            max_product = abs(inputArray[i+1] - inputArray[i])
            
    return max_product



print(solution([2, 4, 1, 0]))

