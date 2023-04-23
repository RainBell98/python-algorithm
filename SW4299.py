T = int(input())
for i in range(T):
    d,h,m = map(int,input().split())
    t_w = 11*24*60+11*60+11
    t_res = d*24*60+h*60+m
    res = t_res-t_w
    if res < 0:
        res = -1
    print("#{}".format(i+1),res)
