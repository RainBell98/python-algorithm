T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    res = (a*a/2)//(b*b/2)
    print("#{}".format(i+1),int(res))