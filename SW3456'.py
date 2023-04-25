T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())

    if a*b == a*c == b*c:
        res = a
    elif a*b == a*c != b*c:
        res = a
    elif a*b == b*c != a*c:
        res = b
    elif c*b == c*a != a*b:
        res = c
    print("#{}".format(i+1),res)






