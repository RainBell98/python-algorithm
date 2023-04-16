N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    res = a+b
    if res >= 24:
        res -= 24
        print("#{}".format(i+1),res)
    else:
        print("#{}".format(i+1),res)