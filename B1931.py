N = int(input())
cnt = 1
p = []
for i in range(N):
    n,m = map(int,input().split())
    p.append([n,m])

p.sort(key = lambda x: x[0])
p.sort(key = lambda x: x[1])

end = p[0][1]
for i in range(1,N):
    if p[i][0]>=end:
        cnt += 1
        end = p[i][1]

print(cnt)


