def solution(n,arr1,arr2):
    p = []
    k = []
    u = []
    for i in range(n):
        b = format(bin(arr1[i])[2:])
        c = format(bin(arr2[i])[2:])
        p.append(b)
        k.append(c)
        b = list(b)
        c = list(c)
        temp = ''
        p[i] = ('0'*(n-len(b)))+p[i]
        k[i] = ('0'*(n-len(c)))+k[i]
        for j in range(n):
            if p[i][j] == '1' or k[i][j] == '1':
                temp += "#"
            else:
                temp +=" "
        u.append(temp)
    return u


