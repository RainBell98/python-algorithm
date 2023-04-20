T = int(input())
for i in range(T):
    check = True
    wi = [0, 0, 0, 0, 0, 0, 0, 0]
    le = [0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    s = [[list(input().strip())] for _ in range(8)]
    for j in range(8):
        for k in range(8):
            if s[j][k] == 'O':
                wi[j] += 1
                le[k] += 1
                cnt += 1
                if wi[j] >=2 or le[k]>=2:
                    check = False
    if cnt == 8:
        pass
    else:
        check = False
    if check == True:
        print("#{}".format(i+1),'yes')
    else:
        print("#{}".format(i+1),'no')




