def solution(numbers,target):
    p = [0]
    for i in numbers:
        k = []
        for j in p:
            k.append(j+1)
            k.append(j-1)
        p = k
    cnt = 0
    for i in range(len(p)):
        if p[i] == target:
            cnt+=1
    return cnt
print(solution([4, 1, 2, 1],4))

