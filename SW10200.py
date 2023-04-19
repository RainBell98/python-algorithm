T = int(input())
for i in range(T):
    n,a,b = map(int,input().split())
    Min = 0
    Max = 0
    if a>=b:
        Max = b
    else:
        Max = a
    if (a+b)-n<0:
        Min = 0
    #elif n-(a+b) == 0:
        #Min =
    else:
        Min = (a+b)-n

    print("#{}".format(i+1),Max,Min)
