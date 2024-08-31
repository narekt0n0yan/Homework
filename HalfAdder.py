def useHalfAdder(a, b):
    a = str(a)
    b = str(b)
    result = str()
    s = 0
    if len(a) != len(b):
        nuls = abs(len(a)-len(b))
        if len(a) > len(b):
            b = str("0" * nuls) + b
        else:
            a = str("0" * nuls) + a
    for i in range(len(a) - 1, -1, -1):
        if i != 0:
            if int(a[i]) + int(b[i]) + s <= 9:
                result = str(int(a[i]) + int(b[i]) + s) + result
                s = 0
            else:
                
                result = str(int(a[i]) + int(b[i]) + s)[1] + result
                s = 1
        else:
            result = str(int(a[i]) + int(b[i]) + s) + result
    
    return result
    
print(useHalfAdder(100, 87))