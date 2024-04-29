def solution(a: list):
    output = []
    first_team = 0
    for i in a[::2]:
        first_team += i
    second_team = 0
    for j in a[1::2]:
        second_team += j
    output.append(first_team)
    output.append(second_team)
    return output

    