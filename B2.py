N= int(input())

def cnt(N):
    if N==1:
        return 1
    elif N ==2:
        return 2
    elif N == 3:
        return 4
    else:
        return cnt(N-1)+cnt(N-2)+cnt(N-3)

for i in range(N):
    k = int(input())
    print(cnt(k))

