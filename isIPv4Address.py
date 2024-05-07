def solution(inputString):
    int_list = []
    var = 0
    inputString = inputString.split('.')
    print(inputString)
    for i in inputString:
        if i == '' or not i.isdigit() or len(inputString) != 4 :
            return False
        i = int(i)
        int_list.append(i)
    print(int_list)
    for j in int_list:
        if j > 255:
            var +=1
    print(var)
    if var > 0:
        return False
    return True

#print(solution('172.16.254.1'))    
print(solution(".254.255.0"))    
#print(solution("01.233.161.131"))    
#print(solution('172.16.254.1'))    
                

def solution1(arr: str):
    int_list = []
    var = 0
    arr = arr.split(".")    
    for i in range(len(arr)):    
        if arr[i][0] == '0' and len(arr[i]) > 1:
            return False
        if not arr[i].isdigit():
            return False
        integer = int(arr[i])
        int_list.append(integer)
    for integer in int_list:
        if integer > 255 or integer < 0 and len(int_list) != 4:
            return False
    return True
