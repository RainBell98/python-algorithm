N = int(input())

rule = ['3','6','9']
for i in range(1,N+1):
    n = str(i)
    cnt = 0
    for j in range(len(n)):
        if n[j] in rule:
            cnt += 1
    if cnt > 0:
        n = '-' * cnt
    print(n, end=' ')