T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    score = list(map(int,input().split()))
    score.sort(reverse=True)
    res = 0
    for j in range(k):
        res += score[j]
    print("#{}".format(i+1),res)