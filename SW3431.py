T = int(input())
for i in range(T):
    l,u,x = map(int,input().split())
    if l<=x<=u:
        print("#{}".format(i+1),0)
    elif x<l:
        print("#{}".format(i+1),l-x)
    elif u<x:
        print("#{}".format(i+1),-1)