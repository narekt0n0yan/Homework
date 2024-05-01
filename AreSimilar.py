def solution(a,b):
    A = sorted(a)
    B = sorted(b)
    var = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            var += 1
    if var > 2 :
        return False
    if A == B:
        return True
    return False
