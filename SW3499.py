import math
T = int(input())
for i in range(T):
    tc = int(input())
    a = list(map(str,input().split()))
    p = []
    l = []
    for j in range(math.ceil(len(a)/2),len(a)):
        p.append(a[j])
    for j in range(len(p)):
        a.remove(p[j])

    print("#{}".format(i+1),end=" ")
    for j in range(len(a)):
        try:
            print(a[j],end=" ")
            print(p[j],end=" ")
        except:
            continue
    print()