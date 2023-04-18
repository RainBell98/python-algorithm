T = int(input())
for i in range(T):
    p = list(map(str,input()))
    p.reverse()
    for j in range(len(p)):
        if p[j] == 'q':
            p[j] = 'p'
        elif p[j] == 'p':
            p[j] = 'q'
        elif p[j] == 'd':
            p[j] = 'b'
        else:
            p[j] = 'd'
    print("#{}".format(i+1),end=' ')
    for j in range(len(p)):
        print(p[j],end='')
    print()