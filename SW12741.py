T = int(input())
ans = []
for i in range(T):
    a,b,c,d = map(int,input().split())
    x = []
    y = []

    for j in range(a,b+1):
        x.append(j)
    for j in range(c,d+1):
        y.append(j)

    res = [j for j in x if j in y]
    if len(res) == 0:
        ans.append(len(res))
    else:
        ans.append(len(res)-1)

for i in range(T):
    print("#{}".format(i + 1), ans[i])