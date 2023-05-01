T = int(input())
for i in range(T):
    tc = int(input())
    Funny = []
    for _ in range(tc):
        Funny.append(int(input()))
    cnt = 0
    while len(Funny)>=2:
        temp = Funny[1] - Funny[0]
        p = 1
        while True:
            p+= temp
            if p>max(Funny):
                break
            if p in Funny:
                Funny.remove(p)
        cnt+=1
    print("#{}".format(i+1),cnt)
