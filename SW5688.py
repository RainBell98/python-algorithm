import math
T = int(input())
for i in range(T):
    n = int(input())
    a = -1
    for j in range(1,n):
        if j**3 == n:
            a = j
            break

    print("#{}".format(i+1),a)



