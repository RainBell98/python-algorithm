T = int(input())
p = [20,40,60,80,100,120,140,160,180,200]

def score(x,y):
    dis = (x*x+y*y)**0.5
    res = 0
    for i in zip(p):
        if dis <= i:
            res = 11 - i/20
            return res
            break


for i in range(T):
    dart = int(input())
    res = 0
    for j in range(dart):
        x,y = map(int,input().split())
        res += score(x,y)
    print(res)

