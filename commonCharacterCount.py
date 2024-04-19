def solution(s1, s2):
    var = 0
    first_dict = {}
    second_dict = {}
    for i in s1:
        if i in first_dict:
            first_dict[i] += 1
        else:
            first_dict[i] = 1
    for j in s2:
        if j in second_dict:
            second_dict[j] += 1
        else:
            second_dict[j] = 1
    for i in first_dict:
        for j in second_dict:
            if i == j:
                var += min(first_dict[i], second_dict[j])
    return var


print(solution("aabcc", "adcaa"))


