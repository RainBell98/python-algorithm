T = int(input())
for i in range(T):
    p = list(map(str,input()))
    a = b = 1
    for j in p:
        if j == 'L':
            b += a
        else:
            a += b
    print("#{}".format(i+1),a,b)