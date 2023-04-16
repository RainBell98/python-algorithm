N = int(input())
for i in range(N):
    a,b = map(int,input().split())

    if a>=10 or b>=10:
        print("#{}".format(i+1),-1)
    else:
        res = a*b
        print("#{}".format(i+1),res)