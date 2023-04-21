T = int(input())
for i in range(T):
    a = [list(map(str,input()))for j in range(5)]
    print("#{}".format(i+1),end=" ")
    for j in range(len(a)):
        for k in range(5):
            if a[k][j] == '':
                pass
            else:
                print(a[k][j],end="")


