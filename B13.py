n,m = map(int,input().split())
cnt = 0
ls = []

for i in range(n):
    ls.append(int(input()))

ls.reverse()

for i in range(n):
    if m-ls[i] >=0:
        cnt += m//ls[i]
        m = m%ls[i]

    if m == 0: break

print(cnt)