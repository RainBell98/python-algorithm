def solution(answers):
    answer = []
    p = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            p[0] += 1
        if answers[i] == second[i%8]:
            p[1] += 1
        if answers[i] == third[i%10]:
            p[2] += 1
    MAX = max(p)
    for i in range(len(p)):
        if p[i] == MAX:
            answer.append(i+1)
    return answer
print(solution([1,2,3,4,5]))
