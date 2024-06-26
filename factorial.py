import time
import sys

sys.setrecursionlimit(100000)
sys.set_int_max_str_digits(10000000)

def fuck(num: int) -> int:
    if num == 0:
        return 1
    return fuck(num-1) * num


start = time.time()
fuck(50000)
end = time.time()
print(end - start)

print('==================================')

def factorial(n: int) -> int:
    result = 1 
    for num in range(1,n+1):
        result = result * num
    return result      

start = time.time()  
factorial(50000)
end = time.time()
print(end - start)