T = int(input())
for i in range(T):
    s = input()
    s = list(s)
    s1 = ''
    s2 = ''
    s3 = ''
    s4 = ''
    k = []
    for j in range(len(s)):
        if j > len(s) // 2:
            s1 += s[j]
        else:
            s2 += s[j]
    for j in range(len(s)):
        if j > len(s) // 2 - 1:
            s3 += s[j]
        else:
            s4 += s[j]
    k.append(int(s1)+int(s2))
    k.append(int(s3)+int(s4))
    print("#{}".format(i+1),min(k))



