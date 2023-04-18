T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    check = True
    while b != 1:
        if b%2 != 1:
            check = False
        b = b//2
    if check == True:
        print("#{}".format(i+1),"ON")
    else:
        print("#{}".format(i+1),"OFF")

