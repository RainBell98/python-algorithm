def solution(n):
    n = n ** (1/2)
    if n == int(n):
        return 1
    else:
        return 2