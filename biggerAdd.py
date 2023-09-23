def solution(a, b):
    answer2 = str(a)+str(b)
    answer1 = str(b) +str(a)
    if int(answer1)>=int(answer2):
        return int(answer1)
    return  int(answer2)