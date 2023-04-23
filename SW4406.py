T = int(input())
for i in range(T):
    a = list(map(str,input()))
    p = []
    for j in range(len(a)):
        if a[j] == 'a' or a[j] == 'e' or a[j] == 'i' or a[j] == 'o' or a[j] == 'u':
            pass
        else:
            p.append(a[j])
    print("#{}".format(i+1),end=" ")
    for j in range(len(p)):
        print(p[j],end="")
    print()