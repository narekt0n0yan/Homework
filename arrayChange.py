def solution(inputArray):
    var = 0
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            var += inputArray[i]-inputArray[i+1]+1
            inputArray[i+1] += inputArray[i] - inputArray[i+1] + 1
    return var
    

print(solution([1,1,1]))
            