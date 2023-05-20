T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    check = True
    for j in range(a):
        if b%2 != 1:
            check = False
    if check == False:
        print("#{}".format(i+1),"ON")
    else:
        print("#{}".format(i+1),"OFF")

