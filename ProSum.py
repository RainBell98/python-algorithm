def solution(n):
    p = []
    for num in range(1,n+1):
        res = n/num
        if int(res)==res:
            p.append(num)
    return sum(p)