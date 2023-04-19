T = int(input())
for i in range(T):
    tc = int(input())
    p = []
    for j in range(tc):
        pay = int(input())

        if pay == 0:
            p.pop()
        else:
            p.append(pay)
    total = sum(p)
    print("#{}".format(i+1),total)