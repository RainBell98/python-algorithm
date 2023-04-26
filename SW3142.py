T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    dh = n-m
    h = m-dh
    print("#{}".format(i+1),h,dh)
