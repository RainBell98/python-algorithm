def find(key,x):
    for i in range(4):
        for j in range(3):
            if key[i][j] == x:
                return i,j


def solution(numbers,hand):
    key = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    result = []
    L_check = []
    R_check = []
    L_check.append(find(key,'*'))
    R_check.append(find(key,'#'))
    res = ''

    for i in range(len(numbers)):
        l1_res,l2_res,r1_res,r2_res,l_res,r_res = 0,0,0,0,0,0

        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            result.append('L')
            L_check.pop()
            L_check.append(find(key,str(numbers[i])))
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            result.append('R')
            R_check.pop()
            R_check.append(find(key,str(numbers[i])))
        else:
            for j in range(4):
                for k in range(3):
                    if key[j][k] == str(numbers[i]):
                        l1_res = j - L_check[0][0]
                        l2_res = k - L_check[0][1]
                        r1_res = j - R_check[0][0]
                        r2_res = k - R_check[0][1]
                        if l2_res < 0:
                            l2_res *= -1
                        elif l1_res <0:
                            l1_res *= -1
                        elif r2_res < 0:
                            r2_res *= -1
                        elif r1_res <0:
                            r1_res *= -1
                        l_res = l1_res+l2_res
                        r_res = r1_res+r2_res
                        if l_res<r_res:
                            result.append('L')
                            L_check.pop()
                            L_check.append(find(key, str(numbers[i])))
                        elif l_res>r_res:
                            result.append('R')
                            R_check.pop()
                            R_check.append(find(key, str(numbers[i])))
                        else:
                            if hand == 'right':
                                result.append('R')
                                R_check.pop()
                                R_check.append(find(key, str(numbers[i])))
                            else:
                                result.append('L')
                                L_check.pop()
                                L_check.append(find(key, str(numbers[i])))
    for i in range(len(result)):
        res += result[i]
    return res
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))