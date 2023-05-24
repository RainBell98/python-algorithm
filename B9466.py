import sys
sys.setrecursionlimit(10**6)
T = int(input())
def dfs(x):
    global zzac
    visited[x] = 1
    info.append(x)
    w = student[x]
    if visited[w] == 1:
        if w in info:
            zzac += info[info.index(w):]
        return
    else:
        dfs(w)

for tc in range(T):
    n = int(input())
    student = [0]+list(map(int,input().split()))
    visited = [0]*(n+1)
    zzac = []

    for i in range(1,n+1):
        if visited[i] == 0:
            info = []
            dfs(i)
    print(n-len(zzac))
