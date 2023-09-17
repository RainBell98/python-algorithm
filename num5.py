def solution(names):
    answer = []
    j = 0
    for i in range(len(names)):
        if i%5 ==0:
            answer.append(names[i])
    return answer
