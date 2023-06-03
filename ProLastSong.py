def change(x):
    x = list(x)
    answer = ""
    for i in range(len(x)-1):
        if i <len(x)-1:
            if x[i] == 'C' and x[i+1] == "#":
                x[i] = 'c'
                x.remove(x[i+1])
            elif x[i] == 'D' and x[i+1] == "#":
                x[i] = 'd'
                x.remove(x[i+1])
            elif x[i] == 'F' and x[i+1] == "#":
                x[i] = 'f'
                x.remove(x[i+1])
            elif x[i] == 'G' and x[i + 1] == "#":
                x[i] = 'g'
                x.remove(x[i + 1])
            elif x[i] == 'A' and x[i+1] == "#":
                x[i] = 'a'
                x.remove(x[i+1])
    for i in x:
        answer += i
    return answer
def time1(x):
    a,b = x.split(":")
    return int(a)*60+int(b)
def solution(m,musicinfos):
    change_m = change(m)
    p = []
    for music in musicinfos:
        s = music.split(",")
        p.append(s)
        for i in range(len(p)):
            p[i][3] = change(p[i][3])

    result = [[0 for i in range(2)]for j in range(len(p))]
    u = 0
    for i in range(len(p)):
        k = time1(p[i][1])-time1(p[i][0])
        answer = ''
        for j in range(k):
            if j>=len(p[i][3]):
                j = j%len(p[i][3])
            answer += p[i][3][j]
        if answer.find(change_m)!=-1:
            result[u][0] = k
            result[u][1] = p[i][2]
            u+=1
        else:
            continue
    MAX = []
    q = max(result)
    for i in range(len(result)):
        if int(result[i][0]) == q[0]:
            MAX.append(result[i][1])
    if result[0][0] != 0:
        return MAX[0]
    else:
        return "(None)"


print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF","12:00,12:16,QUU,CDEFGAB"]))