N = int(input())
print()
for i in range(N):
    people = int(input())
    d = list(map(int,input().split()))
    res = 0
    cnt = 0
    for k in range(len(d)):
        if d[k] < 0:
            d[k] = d[k] * -1
    res = min(d)
    for s in range(len(d)):
        if res == d[s]:
            cnt+=1
    print("#{}".format(i+1),res,cnt)

