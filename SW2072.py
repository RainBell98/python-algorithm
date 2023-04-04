N = int(input())
answer = 0
for i in range(N):
    p = map(int,input().split())
    for j in p:
        if j%2 != 0:
            answer += j
    print("#"+str(i+1),str(answer))
    answer = 0
