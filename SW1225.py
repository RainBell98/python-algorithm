for i in range(10):
    T = int(input())
    a = list(map(int,input().split()))
    cnt = 1
    temp = 0
    check = False
    while check == False:
        if cnt > 5:
            cnt = 1
        temp = a[0]-cnt
        a.remove(a[0])
        a.append(temp)
        cnt += 1

        if a[-1]<=0:
            a[-1] = 0
            check = True
    print("#{}".format(i+1),end=" ")
    for k in range(len(a)):
        print(a[k],end=' ')
    print()
