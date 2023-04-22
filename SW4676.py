T = int(input())
for i in range(T):
    p = list(map(str,input()))
    num = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    for j in range(len(a)):
        p.insert(a[j],"-")
    print("#{}".format(i+1),end=' ')
    for j in range(len(p)):
        print(p[j],end="")
