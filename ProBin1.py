from collections import Counter
def solution(s):
    res = []
    s = list(s)
    ans = s.count("0")
    cnt = 0
    k = list(s)
    while len(k)!=1:
        answer = []
        for i in k:
            if i != "0":
                answer.append(i)
        k = list(format(len(answer),'b'))
        ans += k.count("0")
        cnt +=1
        if k[0] == "1":
            if len(k) == 1:
                break
    res.append(cnt)
    res.append(ans)

    return res