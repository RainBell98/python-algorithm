import math
N = int(input())
for i in range(N):
    n,d = map(int,input().split())
    res = n/(d*2+1)
    print("#{}".format(i+1),math.ceil(res))