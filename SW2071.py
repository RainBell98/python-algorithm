import math
N = int(input())
answer = 0
a=0
for i in range(N):
    p = list(map(int,input().split()))
    for j in range(10):
        a += p[j]
        answer = round(a/10)
    print("#"+str(i+1),answer)
    answer = 0
    a = 0

