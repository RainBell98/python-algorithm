def solution(x):
    a = str(x)
    a = list(a)
    d = 0
    for i in a:
        d += int(i)
    if x%d == 0:
        answer = True
    else:
        answer = False
    return answer
def solution2(a,b):
    answer = []
    if a>=b:
        temp = b
        b = a
        a = temp
    for i in range(a,b+1):
        answer.append(i)
    return sum(answer)

def solution3(num):
    cnt = 0
    for i in range(500):
        if num == 1:
            return cnt
        if num %2 == 0:
            num /= 2
            cnt+=1
        else:
            num = num*3+1
            cnt+=1
    return -1

def solution4(seoul):
    return "김서방은 "+str(seoul.index("Kim"))+"에 있다"

def solution5(arr,divisor):
    p = []
    for num in arr:
        if num%divisor==0:
            p.append(num)
    if len(p)>=1:
        p.sort()
        return p
    else:
        p.append(-1)
        return p
def solution6(absolutes,sings):
    p = []
    for i in range(len(sings)):
        if sings[i] == True:
            sings[i] = 1
        else:
            sings[i] = -1
        p.append(absolutes[i]*sings[i])
    return sum(p)
def solution7(phone_number):
    phone_number = list(phone_number)
    answer =''
    for i in len(phone_number):
        if i < len(phone_number)-4:
            answer+="*"
        else:
            answer+=i
    return answer

def solution8(numbers):
    p = []
    for i in range(10):
        if i not in numbers:
            p.append(i)
    return sum(p)
def solution9(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
    return arr
def solution10(s):
    s = list(s)
    answer = ''
    if len(s)%2 != 0:
        return s[int(len(s)/2)]
    else:
        for i in range(int(len(s)/2)-1,int(len(s)/2)+1):
            answer += s[i]
        return answer
def solution11(n):
    answer = ""
    for i in range(n):
        if i%2 != 0:
            answer += "박"
        else:
            answer += "수"
    return answer
def solution12(a,b):
    p = []
    for i in range(len(b)):
        p.append(a[i]*b[i])
    return sum(p)
def solution13_1(x):
    cnt =0
    for i in range(1,x+1):
        if x%i == 0:
            cnt+=1
    return cnt
def solution13(left,right):
    answer = 0
    for i in range(left,right+1):
        k = solution13_1(i)
        if solution13_1(i)%2 != 0:
            answer -= i
        else:
            answer+=i
    return answer
def solution14(s):
    answer = ''
    s = list(s)
    s.sort(reverse=True)
    for i in s:
        answer += i
    return answer
def solution15(price,money,count):
    p = 0
    for i in range(1,count+1):
        p += price*i
    if p<=money:
        return 0
    return p-money
def solution16(s):
    s = list(s)
    if len(s)== 4 or len(s) == 6:
        for i in s:
            if i.isnumeric() == False:
                return False
    else:
        return False
    return True
def solution17(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j]+=arr2[i][j]
    return arr1
def solution18():
    a, b = map(int, input().strip().split(" "))
    a = "*" * a
    for i in range(b):
        print(a)
import math
def lcm(x,y):
    return x*y//math.gcd(x,y)
def solution19(n,m):
    p = []
    p.append(math.gcd(n,m))
    p.append(lcm(n,m))
    return p
def solution20(n):
    answer = ''
    while n>0:
        n,m = divmod(n,3)
        answer += str(m)
    return int(answer,3)

#print(solution17([[1,2],[2,3]],[[3,4],[5,6]]))
