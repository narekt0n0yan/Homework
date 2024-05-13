def solution(cell1, cell2):
    return  (ord(cell1[0]) + ord(cell1[1]) - ord(cell2[0]) - ord(cell2[1])) % 2 == 0


