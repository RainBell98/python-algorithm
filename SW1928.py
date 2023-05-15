N = int(input())
for i in range(N):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = []
    MAX = 0
    if len(a)<=len(b):
        for k in range(len(b)-len(a)+1):
            res = 0
            for j in range(len(a)):
                res += a[j]*b[j+1]
            if res>MAX:
                MAX = res
    else:
        for k in range(len(a)-len(b)+1):
            res = 0
            for j in range(len(b)):
                res += a[j+1] * b[j]
            if res>MAX:
                MAX = res
    print(MAX)



