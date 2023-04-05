N = int(input())
answer = 0
for i in range(N):
    p = map(int,input().split())
    answer = max(p)
    print("#"+str(i+1),str(answer))
    answer = 0
