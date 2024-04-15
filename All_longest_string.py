def solution(inputArray: list):
    array = []
    max_str_len = len(inputArray[0])
    for string in inputArray:
        max_str_len = max(max_str_len, len(string))
    for j in inputArray:
        if len(j) == max_str_len:
            print(j)
            array.append(j)

    return array    


a = solution(["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"])

if a == ["aba", "vcd", "aba"]:
    print(True)
else:
    print(False)