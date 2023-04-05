
N = int(input())

p = list(map(int,input().split()))
p.sort()
res = p[int(N/2)]
print(res)