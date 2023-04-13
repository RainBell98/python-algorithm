N = int(input())
def is_Prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for i in range(N):
    n = int(input())
    x = 0
    y = 0
    for x in range(1,1000000001):
        for y in range(1,1000000001):
            if is_Prime(x) == False and is_Prime(y) == False:
                if x-y == n:
                    print(x,y)
                    break
        break