num = 1000000

def check(n):
    for i in range(2, num + 1):
        if num % i != 0:
            pass
        else:
            return 0
    return 1
for i in range(2,num+1):
    res = check(i)
    if res == 1:
        print(i,end=" ")
    else:
        pass


