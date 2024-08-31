
def poisk(n): 
    v = [13,5,6,76,7,10,20,30,45,34,87,65,87]
    v.sort()
    start = 0
    stop = len(v) - 1
    result = 0

    while start <= stop : 
        mid = (stop + start) // 2
        if v[mid] == n: 
            return mid +1 
        elif v[mid] < n:
            start = mid + 1
        else :
            stop = mid - 1 
    return False
    
        
        
print(poisk(45))