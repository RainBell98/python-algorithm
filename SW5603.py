T = int(input())
for i in range(T):
    num = int(input())
    p = []
    for j in range(num):
        p.append(int(input()))
    p.sort()
    res = int(sum(p)//num)
    cnt = 0
    for j in range(num):
        if res<p[j]:
            cnt += p[j] - res
    print("#{}".format(i+1),cnt)



