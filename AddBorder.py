def solution(picture):
    matrix = []
    first_row = '*' * (len(picture[0]) + 2)
    matrix.append(first_row)
    for i in picture:
        row = "*"
        row += i
        row += '*'
        matrix.append(row)
    matrix.append(first_row)
    return matrix



print(solution( ["abc",
                 "ded"]))



            