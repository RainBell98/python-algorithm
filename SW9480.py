from itertools import combinations
def comb(s):
    p = []
    for j in range(97, 123):
        p.append(chr(j))
    for j in range(len(s)):
        if s[j] in p:
            p.remove(s[j])
    if len(p) == 0:
        return True
    else:
        return False


T = int(input())
for i in range(T):
    k = []
    n = int(input())
    s = []

    for j in range(n):
        s.append(input())
    cnt = 0

    for j in range(1,n+1):
        k = list(map(''.join,combinations(s,j)))
        for q in range(len(k)):
            if len(k[q])>=26:
                if comb(k[q]) == True:
                    cnt+=1

    print("#{}".format(i+1),cnt)


