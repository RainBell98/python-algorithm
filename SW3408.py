T = int(input())
for i in range(T):
    n = int(input())
    s1 = 0
    s2 = 0
    s3 = 0
    for j in range(1,n+1):
        s1 += j
    for j in range(1,n*2+1):
        if j%2 != 0:
            s2 += j
        else:
            s3 += j
    print("#{}".format(i+1),s1,s2,s3)
