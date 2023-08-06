def solution(a,b):
    res = 0
    if a%2 != 0 and b%2 != 0:
        res = a**2+b**2
    elif a%2 == 0 and b%2 != 0:
        res = (a+b)*2
    elif a%2 != 0 and b%2 == 0:
        res = (a+b)*2
    else:
        res = a-b
        if res<0:
            res *= -1
    return res
        