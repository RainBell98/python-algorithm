N, M = map(int,input().split())

x = [0 for _ in range(N)]

for _ in range(M):
    a, b, c = map(int,input().split())
    for i in range(a-1, b):
        x[i] = c


print(*x)