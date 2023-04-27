T = int(input())
for i in range(T):
    a = list(map(str,input()))
    n = '0'
    cnt = 0

    for j in range(len(a)):
        if a[j] != n:
            n = a[j]
            cnt+=1
    print("#{}".format(i+1),cnt)