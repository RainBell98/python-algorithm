def solution(n,stages):
    total = len(stages)
    p = []
    s = []
    for i in range(1,n+1):
        cnt = 0
        for j in range(total):
            if stages[j] == i:
                cnt+=1
        if cnt == 0:
            p.append(0)
        else:
            p.append(cnt/total)
        total -= cnt

    s = sorted(p,reverse=True)
    k = []
    for i in range(len(p)):
        k.append(p.index(s[i])+1)
        p[p.index(s[i])] =2
    return k
for i in range(1):
    print(solution(5,[2,1,2,6,2,4,3,3]))
