from collections import deque

def solution(queue1,queue2):
    res = (sum(queue1)+sum(queue2))/2
    cnt = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    qu1 = deque(queue1)
    qu2 = deque(queue2)

    for i in range(100):
        if sum1 > res:
            sum1 -= qu1.popleft()
            cnt +=1
        elif sum1<res:
            qu1.append(qu2.popleft())
            sum1 += qu1[-1]
            cnt+=1
        else:
            return cnt
    return -1

print(solution([1, 2, 1, 2],[1, 10, 1, 2]))

