def solution(code):
    answer = ''
    code = list(code)
    mode = 0
    for i in range(len(code)):
        if (code[i] ==1):
            mode = 1
            if(mode == 0 and code[i].isnumeric() == False):
                if(i%2==0):
                    answer+=code[i]
            elif(mode ==1 and code[i].isnumeric()== False):
                if(i%2!=0):
                    answer+= code[i]
        elif(code[i]==0):
            mode = 0
    return answer
print(solution("abc1abc1abc"))