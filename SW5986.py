def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
T = int(input())
for i in range(T):
    a = 0
    n = int(input())
    p = []
    for j in range(2,n+1):
        if prime(j) == True:
            p.append(j)
    for j in p:
        for k in p:
            for s in p:
                if j+k+s == n:
                    if j>=k>=s:
                        a += 1

    print("#{}".format(i+1),a)


