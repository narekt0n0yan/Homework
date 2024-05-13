def solution(name:str):
    if len(name) == 0:
        return False

    if not name[0].isalpha() and name[0] != "_" :
        return False
     
    
    for i in range(len(name)):
        if not name[i].isalnum() and  name[i] != "_":
            return False
    return True
        

        
            