T = int(input())
for i in range(T):
    tc,tc2 = map(str,input().split())
    a = list(map(str,input().split()))
    for j in range(len(a)):
        if a[j] == 'ZRO':
            a[j] = 0
        elif a[j] == 'ONE':
            a[j] = 1
        elif a[j] == 'TWO':
            a[j] = 2
        elif a[j] == 'THR':
            a[j] = 3
        elif a[j] == 'FOR':
            a[j] = 4
        elif a[j] == 'FIV':
            a[j] = 5
        elif a[j] == 'SIX':
            a[j] = 6
        elif a[j] == 'SVN':
            a[j] = 7
        elif a[j] == 'EGT':
            a[j] = 8
        else:
            a[j] = 9
    a.sort()
    for j in range(len(a)):
        if a[j] == 0:
            a[j] = 'ZRO'
        elif a[j] == 1:
            a[j] = 'ONE'
        elif a[j] == 2:
            a[j] = 'TWO'
        elif a[j] == 3:
            a[j] = 'THR'
        elif a[j] == 4:
            a[j] = 'FOR'
        elif a[j] == 5:
            a[j] = 'FIV'
        elif a[j] == 6:
            a[j] = 'SIX'
        elif a[j] == 7:
            a[j] = 'SVN'
        elif a[j] == 8:
            a[j] = 'EGT'
        else:
            a[j] = 'NIN'
    print("#{}".format(i+1),end=" ")
    for j in range(len(a)):
        print(a[j],end=" ")
    print()