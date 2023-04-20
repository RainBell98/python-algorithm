import sys
T = int(input())
for i in range(T):
    d,a,b,f = map(float,sys.stdin.readline().split())
    f_dis = 0

    while d != 0:
        d -= a+b
        f_dis += f
    print(f_dis)