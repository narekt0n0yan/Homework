def solution(n: int):
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            pass
        else:
            return False
    return True


