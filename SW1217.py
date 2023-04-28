def mul(a,b,c):
    if b == 2:
        return a*c
    else:
        a = a*c
        b -= 1
        return mul(a,b,c)

for i in range(10):
    tc = int(input())
    a,b = map(int,input().split())
    c = a
    res = mul(a,b,c)
    print("#{}".format(i+1),res)
    print()
