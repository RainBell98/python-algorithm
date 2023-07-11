import sys
sys.setrecursionlimit(10**7)

def solution(n):
    cnt = 0
    for i in range(1,n+1):
        answer = 0
        for j in range(i,n+1):
            answer += j
            if answer<n:
                continue
            elif answer>n:
                break
            else:
                cnt+=1
                break
    return cnt