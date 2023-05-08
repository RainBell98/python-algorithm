def res(x):
    p = list(x)
    for j in range(len(p)):
        p[j] = int(p[j])
    b = sum(p)
    if b<10:
        return b
    else:
        b = str(b)
        return res(b)

T = int(input())
a = []
for i in range(T):
    p = input()
    a.append(res(p))

for i in range(T):
    print("#{}".format(i+1),a[i])
