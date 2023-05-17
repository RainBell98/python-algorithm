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
    k = []
    for j in range(1,1000000001):
        if is_Prime(j) == False:
            k.append(j)
    for x in k:
        for y in k:
            if x-y == n:
                print(x,y)
                break
        break