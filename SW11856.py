N = int(input())

for i in range(N):
    a = list(map(str,input()))
    a.sort()

    if a[0] != a[2]:
        if a[0] == a[1] and a[2] == a[3]:
            print("#{}".format(i+1),'Yes')
        else:
            print("#{}".format(i + 1), 'No')
    else:
        print("#{}".format(i + 1), 'No')

