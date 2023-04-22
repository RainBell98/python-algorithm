T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())

    if a<b:
        print("#{}".format(i+1),c//a)
    else:
        print("#{}".format(i + 1), c // b)