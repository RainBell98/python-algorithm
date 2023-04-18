T = int(input())
for i in range(T):
    p = list(map(str,input()))
    a = []
    for j in range(len(p)):
        if p[j] in a:
            a.remove(p[j])
        else:
            a.append(p[j])
    a.sort()
    if len(a) == 0:
        print("#{}".format(i+1),"Good")
    else:
        print("#{}".format(i + 1),end=' ')
        for k in range(len(a)):
            print(a[k],end='')
        print()