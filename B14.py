
cnt = int(input())

def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

for i in range(cnt):
    n, m = map(int, input().split())
    print(n*m/gcd(n,m))




