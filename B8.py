N = list(map(str,input().split()))
cnt = 0
for i in range(len(N)):
    if N[i] == '=':
        if N[i-1] == 'c' or N[i-1] == 's':
            cnt += 1
        elif N[i-1] == 'z':
            if N[i-2] == 'd':
                cnt += 1
            else:
                cnt += 1

    elif N[i] == '-':
        if N[i-1] == 'c' or N[i-1] == 'd':
            cnt += 1

    elif N[i] == 'j':
        if N[i-1] == 'l' or N[i-1] == 'n':
            cnt += 1

print(cnt)