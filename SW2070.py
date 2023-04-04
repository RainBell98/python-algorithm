N = int(input())

for i in range(N):
    p = list(map(int,input().split()))
    if p[0]>p[1]:
        print("#"+str(i+1),">")
    elif p[0] == p[1]:
        print("#"+str(i+1),"=")
    else:
        print("#"+str(i+1),"<")


