def solution(n):
    p = []
    for num in range(1,n+1):
        res = n/num
        if int(res)==res:
            p.append(num)
    return sum(p)
def solution(n):
    n = str(n)
    n = list(n)
    n.reverse()
    n = list(map(int,n))

    return n
from collections import Counter
def solution(s):
    s = s.upper()
    counter = Counter(s)
    if counter["P"] == counter["Y"]:
        return True
    else:
        return False
def solution(n):
    for i in range(1,n+1):
        if n/i == i:
            return (i+1)**2
    return -1
def solution(s):
    s = list(s)
    a = []
    if s[0].isnumeric:
        for i in range(len(s)):
            a.append(s[i])
    else:
        for i in range(1,len(s)):
            a.append(s[i])
    answer = ''
    for i in range(len(a)):
        answer += a[i]
    answer = int(answer)
    if s[0].isnumeric:
        return answer
    return '-'.join(answer)
def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse=True)
    for i in n:
        answer += str(i)
    return int(answer)