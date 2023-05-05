T = int(input())
p = []
for i in range(T):
    a = list(map(int,input().split()))

    if a[0]/a[1]>a[2]/a[3]:
        p.append("ALICE")
    elif a[0]/a[1]<a[2]/a[3]:
        p.append("BOB")
    else:
        p.append("DRAW")
for i in range(len(p)):
    print("#{}".format(i+1),p[i])