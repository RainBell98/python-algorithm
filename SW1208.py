for j in range(10):
    T = int(input())
    a = list(map(int,input().split()))

    for i in range(T):
        a.sort(reverse=True)
        a[0] -= 1
        a[-1] += 1
    res = max(a) - min(a)
    print("#{}".format(j+1),res)