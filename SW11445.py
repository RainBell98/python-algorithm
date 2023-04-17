T = int(input())
for i in range(T):
    P = list(map(str,input().replace(" ","")))
    Q = list(map(str,input().replace(" ","")))
    check = True
    check_point = 0
    if len(P)<=len(Q):
        for j in range(len(P)):
            if P[j] == Q[j]:
                pass
            else:
                check = False
                check_point = j
                break
        if check == True:
            if Q[len(P)] != 'a':
                print("#{}".format(i+1),'Y')
            else:
                print("#{}".format(i + 1), 'N')
        else:
            if Q[check_point+1] != 'a':
                print("#{}".format(i + 1), 'Y')
            else:
                print("#{}".format(i + 1), 'N')
    else:
        for j in range(len(Q)):
            if P[j] == Q[j]:
                pass
            else:
                check = False
                check_point = j
                break
        if check == True:
            if Q[len(P)] != 'a':
                print("#{}".format(i+1),'Y')
            else:
                print("#{}".format(i + 1), 'N')
        else:
            if Q[check_point+1] != 'a':
                print("#{}".format(i + 1), 'Y')
            else:
                print("#{}".format(i + 1), 'N')


