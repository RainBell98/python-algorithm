T = int(input())
for i in range(T):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]<40:
            a[j] = 40
    res = sum(a)
    print("#{}".format(i+1),res//len(a))