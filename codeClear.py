def solution(code):
    answer = ''
    code = list(code)
    mode = 0
    
    for i in range(len(code)):
        if(code[i].isnumeric() == True):
            mode+=1
        if(mode%2 ==0  and code[i].isnumeric() == False):
            if(i%2==0):
                answer+=code[i]
        elif(mode%2!= 0 and code[i].isnumeric()== False):
            if(i%2!=0):
                answer+= code[i]
    if(answer == ""):
        return "EMPTY"
    return answer
print(solution("abc1abc1abc"))