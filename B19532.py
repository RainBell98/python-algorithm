n = list(map(int,input().split()))
a = n[0]
b = n[1]
c = n[2]
d = n[3]
e = n[4]
f = n[5]

for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x,y)
            break




