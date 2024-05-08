def solution(arr: str):
    int_list = []
    var = 0
    arr = arr.split(".")    
    for i in range(len(arr)):   
        if not arr[i].isdigit():
            return False 
        if arr[i][0] == '0' and len(arr[i]) > 1:
            return False
        integer = int(arr[i])
        int_list.append(integer)
    for integer in int_list:
        if integer > 255 or len(int_list) != 4:
            return False
    return True

# print(solution('172.16.254.1'))    
# print(solution(".254.255.0"))    
# print(solution("01.233.161.131"))    
# print(solution('172.16.254.1'))   
print(solution('156..'))
