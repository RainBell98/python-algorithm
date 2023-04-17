T = int(input())
for i in range(T):
    a = int(input())
    p = [[0]*a for j in range(a)]
    is_check = True
    for j in range(a):
        k = list(map(str,input()))
        for i in range(len(k)):
            p[j][i] = k[i]
    for i in range(a):
        for j in range(a):
            if i>=4 or i ==0:
                if p[i][j] == 'o' and p[i + 1][j] == 'o' and p[i + 2][j] == 'o' and p[i + 3][j] == 'o' and p[i + 4][
                    j] == 'o':
                    is_check = True
                elif j>=4 or j ==0:
                    if p[i][j] == 'o' and p[i + 1][j + 1] == 'o' and p[i + 2][j + 2] == 'o' and p[i + 3][
                        j + 3] == 'o' and p[i + 4][j + 4] == 'o':
                        is_check = True
                    elif p[i][j] == 'o' and p[i - 1][j - 1] == 'o' and p[i - 2][j - 2] == 'o' and p[i - 3][j - 3] == 'o'and p[i - 4][j - 4] == 'o':
                        is_check = True
            elif j>=4 or j ==0:
                if p[i][j] == 'o' and p[i][j+1] == 'o'and p[i][j+2] == 'o'and p[i][j+3] == 'o'and p[i][j+4] == 'o':
                    is_check = True
                else:
                    is_check = False
    if is_check == True:
        print("#{}".format(i + 1), 'YES')
    else:
        print("#{}".format(i + 1), 'NO')


