
def solution(k,m,score):
    score.sort(reverse=True)
    res = 0
    for i in range(len(score)//m):
        res += score[i*m+m-1]*m
    return res