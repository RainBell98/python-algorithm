import numpy as np
for i in range(1):
    T = int(input())
    p = [list(map(str,input()))for _ in range(100)]
    r1 = p[::-1]
    r2 = p[:,::-1]
    cnt1 = 0
    cnt2 = 0
    for j in range(100):
        for k in range(100):
            if p[j][k] == r2[j][k]:
                cnt1+=1
            else:
                cnt1 = 0
    for j in range(100):
        for k in range(100):
            if p[k][j] == r1[k][j]:
                cnt2+=1
            else:
                cnt2 = 0
    if cnt2<cnt1:
        print("#{}".format(T),cnt1)
    else:
        print("#{}".format(T),cnt2)