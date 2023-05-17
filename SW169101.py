T = int(input())
for i in range(T):
    n = int(input())
    cnt = 0
    for j in range(-n,n+1):
        for k in range(-n,n+1):
            if j**2 + k**2 <= n**2:
                cnt += 1
    print("#{}".format(i+1),cnt)



