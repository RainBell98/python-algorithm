def solution(dartResult):
    dartResult = list(dartResult)
    p = []
    res = 0
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            p.append(int(dartResult[i-1]))
        elif dartResult[i] == 'D':
            p.append(int(dartResult[i - 1]) ** 2)
        elif dartResult[i] == 'T':
            p.append(int(dartResult[i - 1]) ** 3)
        elif dartResult[i] == '0'and dartResult[i-1]=='1':
            dartResult[i] = '10'

        elif dartResult[i] == '*':
            if p[-1] != p[0]:
                p[-1] = p[-1]*2
                p[-2] = p[-2]*2
            else:
                p[-1] = p[-1]*2
        elif dartResult[i] == '#':
            tmp = p[-1]
            p.append(p[-1]*(-1))
            p.append(tmp*(-1))
    for i in range(len(p)):
        res += p[i]

    return p
print(solution('1D#2S*3S'))