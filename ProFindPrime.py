from itertools import permutations
def prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
def solution(numbers):
    p = []
    number = list(map(int,numbers))
    numbers = list(numbers)
    for i in number:
        if prime(i):
            p.append(i)
    for i in range(2,len(numbers)+1):
        num = list(permutations(numbers,i))
        for j in num:
            res = ""
            for k in range(len(j)):
                res += j[k]
            if prime(int(res)):
                p.append(int(res))
    p = set(p)
    p = list(p)
    return len(p)