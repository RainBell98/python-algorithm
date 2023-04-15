N = int(input())
for i in range(N):
    n = list(map(str,input()))
    cnt = 0
    for j in range(len(n)):
        if n[j] == 'x':
            cnt+=1
    if cnt>=8:
        print("#{}".format(i+1),'NO')
    else:
        print("#{}".format(i + 1), 'YES')
