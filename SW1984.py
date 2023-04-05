import math
N = int(input())

for i in range(N):
    p = list(map(int,input().split()))
    p.sort()
    answer = 0
    a = 0
    for j in range(2,9):
        a += p[j]
    answer = round(a/8)
    print("#"+str(i+1),answer)
