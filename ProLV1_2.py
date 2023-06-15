def solution1(s):
    s = s.split(' ')
    answer = ''
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
    return answer[0:-1]
def solution2(d,budget):
    cnt = len(d)
    d.sort()
    s = sum(d)
    for i in range(len(d),0,-1):
        if budget > s:
            return cnt
        else:
            cnt-=1
            s -= d[-1]

import itertools
def solution3(number):
    p = itertools.combinations(number,3)
    p = list(p)
    cnt = 0
    for i in p:
        if sum(i) == 0:
            cnt+=1
    return cnt
def solution4(s,n):
    s = list(s)
    answer = ''
    for i in s:
        if ord(i)+n > 121 or 90<ord(i)+n<97:
            n -= 26
        if i != "":
            answer += chr(ord(i)+n)
    return answer
def solution5(t,p):
    k = []
    le = list(t)
    cnt = 0
    for i in range(len(le)):
        ans = ''
        if len(le)<len(p):
            break
        for j in range(len(p)):
            ans += le[j]
        le.pop(0)
        k.append(ans)
    for num in k:
        if int(num)<= int(p):
            cnt+=1
    return cnt
def solution6(strings,n):
    strings.sort()
    return sorted(strings,key = lambda  x:x[n])
print(solution6(["abce", "abcd", "cdx"],2))