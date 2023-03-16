n = int(input())

a = []
for _ in range(n):
    p = int(input())
    if p==0:
        a.pop()
    else:
        a.append(p)

print(sum(a))