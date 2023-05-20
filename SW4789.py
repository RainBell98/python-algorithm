T = int(input())
for i in range(T):
    p = list(map(int, input()))
    cnt = 0
    clap = 0

    for j in range(len(p)):
        clap += p[j]
        if p[j] == 0:
            pass
        else:
            if clap < j:
                cnt += j - clap
                clap += cnt

    print("#{}".format(i + 1), cnt)







