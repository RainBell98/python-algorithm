import math
N = int(input())
al = []
bl = []
def is_True(a,b):
    for i, j in zip(a, b):
        s_len, t_len = len(i), len(j)
        n = lcm(s_len, t_len)
        x = int(n / s_len)
        y = int(n / t_len)
        if i * x == j * y: 
            return 1
        else:
            return 0


def lcm(a,b):
    return (a*b)//math.gcd(a,b)
for i in range(N):
    a,b = input().split()
    al.append(a)
    bl.append(b)

    if is_True(al,bl) == 1:
        print("#{}".format(i+1),'yes')
    else:
        print("#{}".format(i+1),'no')
