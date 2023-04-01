import sys
n = int(input())
p = []
a = set()
for i in range(n):
    name,work = sys.stdin.readline().split()
    p.append([name,work])
    if work == "enter":
        a.add(name)
    else:
        a.remove(name)

a = sorted(a,reverse=True)
for i in range(len(a)):
    print(a[i])


