
N = int(input())
p = []
for i in range(N):
    n = list(map(str,input()))
    #LenList = list(n)
    cnt = 0
    for j in range(97,122):
        p.append(chr(j))
    for k in range(len(n)):
        if n[k] != p[k]:
            break
        else:
            cnt += 1
    print("#{}".format(i+1),cnt)
