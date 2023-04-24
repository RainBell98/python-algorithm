T = int(input())
for i in range(T):
    p = list(map(str,input()))
    a = p[::3]
    b = p[1::3]
    c = p[2::3]
    check = True
    S_cnt = 0
    D_cnt = 0
    H_cnt = 0
    C_cnt = 0
    for j in range(len(p),3):
        for k in range(len(p),3):
            if a[j] == p[k]:
                if b[j] == p[k+1]:
                    if c[j] == p[k+2]:
                        if a[j] == 'S':
                            S_cnt += 1
                        elif a[j] == 'D':
                            D_cnt += 1
                        elif a[j] == 'H':
                            H_cnt += 1
                        else:
                            C_cnt += 1
                    else:
                        check = False
                else:
                    check = False
            else:
                check = False


    if check == False:
        print("#{}".format(i+1),'ERROR')
    else:
        print("#{}".format(i+1),13-S_cnt,13-D_cnt,13-H_cnt,13-C_cnt)



