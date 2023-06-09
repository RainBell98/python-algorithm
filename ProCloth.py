def solution(clothes):
    cnt = dict()
    arr = []
    answer = 1
    for a,b in clothes:
        if b not in cnt:
            cnt[b] = 0
        cnt[b]+=1
    for a in cnt.values():
        answer *= a+1
    return answer-1