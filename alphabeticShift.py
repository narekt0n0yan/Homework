def solution(inputString:str):
    new_str = ''
    for i in range(len(inputString)):
        if inputString[i] == "z":
            new_str += 'a'
        else:
            new_str += chr(ord(inputString[i])+1)
    return new_str