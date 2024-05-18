

def solution(deposit, rate, threshold):
    step = 0
    while deposit < threshold:
        deposit = deposit + (deposit * rate / 100)
        step += 1
    return step
    
print(solution(100,20,170))
