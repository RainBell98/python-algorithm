T = int(input())
for i in range(T):
    n = int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    print("#{}".format(i+1))
    for j in range(8):
        print((n//money[j]),end=' ')
        n = n%money[j]
    print()




