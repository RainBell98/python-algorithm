def solution(n):
    ans = 0
    if n%2 == 0:
        for i in range(n+1):
            if i%2 == 0:
                ans += i**2
    else:
        for i in range(n+1):
            if i%2 != 0:
                ans += i
    return ans
    