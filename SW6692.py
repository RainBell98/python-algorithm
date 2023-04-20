T = int(input())
for i in range(T):
    tc = int(input())
    total = 0
    for j in range(tc):
        a,b = map(float,input().split())
        total += a*b
    print("#{}".format(i+1),round(total,6))