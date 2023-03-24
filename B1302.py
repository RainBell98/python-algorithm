d = dict()
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book]+=1
    else:
        d[book] = 1

m = max(d.values())

p = []
for k, v in d.items():
    if v == m:
        p.append(k)
p.sort()
print(p[0])