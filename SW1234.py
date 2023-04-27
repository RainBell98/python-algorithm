for i in range(10):
    a,b = map(str,input().split())
    p = []
    for j in p:
        if p and j == p[-1]:
            p.pop()
        else:
            p.append(j)
    print("#{}".format(i+1),end=" ")
    for j in range(len(p)):
        print(p[j],end="")
