N = int(input())
def devide(n):
    for i in range(1,10):
        for j in range(1,10):
            if i*j == n:
                return 1



for i in range(N):
    n = int(input())
    if devide(n) == 1:
        print("#{}".format(i+1),'Yes')
    else:
        print("#{}".format(i + 1), 'No')