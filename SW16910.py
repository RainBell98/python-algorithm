from itertools import combinations_with_replacement
import numpy as np
T = int(input())
for i in range(T):
    n = int(input())
    p = []
    cnt = 0
    for j in range(n+1):
        p.append(j)
    for j in range(0,n*(-1)-1,-1):
        p.append(j)

    m = list(combinations_with_replacement(p,2))
    m = set(m)
    m = list(m)

    for j in range(len(m)):
        res = sum(m[j])
        res2 = (res ** 2) - 2*(np.prod(m[j]))
        if res2 <= res*res:
            cnt += 1
    print(cnt)

   # print(cnt)



