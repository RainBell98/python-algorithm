N = int(input())
p =[]
for i in range(N):
    a = str(input())
    p.append(a)
    res = p[i][::-1]

    if res == p[i]:
        print("#"+str(i+1),'1')
    else:
        print("#"+str(i+1),'0')
