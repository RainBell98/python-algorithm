
import itertools
def solution1(numbers):
    answer = []
    a = itertools.combinations(numbers,2)
    a = list(a)
    for i in range(len(a)):
        answer.append(sum(a[i]))
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer
def solution2(food):
    answer = ''
    for j in range(1,len(food)):
        answer += str(j)*(food[j]//2)
    return answer+"0"+answer[::-1]
def solution3(a,b,n):
    coke = 0
    while n>=a:
        coke += (n//a)*b
        n = (n//a)*b
        n+=n%a
    return coke
def solution4(name,yearning,photo):
    answer = []
    for i in range(len(photo)):
        res = 0
        for j in range(len(name)):
            for k in range(len(photo[i])):
                if photo[i][k] == name[j]:
                    res+=yearning[j]
        answer.append(res)
    return answer
import datetime
def solution5(a,b):
    date = 'MON TUE WED THU FRI SAT SUN'.split()
    return date[datetime.datetime(2016, a, b).weekday()]

def solution6(k,score):
    answer = []
    res = []
    for i in range(len(score)):
        if len(res)<k:
            res.append(score[i])
        else:
            if score[i]>min(res):
                res.remove(min(res))
                res.append(score[i])
        answer.append(min(res))
    return answer

print(solution6(3,[10, 100, 20, 150, 1, 100, 200]))