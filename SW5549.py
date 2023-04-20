T = int(input())
for i in range(T):
    n = list(input())
    if int(n[-1])%2 != 0:
        print("#{}".format(i+1),"Odd")
    else:
        print("#{}".format(i + 1), "Even")