N = int(input())
for i in range(N):
    p,q,r,s,w = list(map(int,input().split()))
    a_price = p*w
    if r<w:
        b_price = q+(w-r)*s
    else:
        b_price = q

    if a_price>b_price:
        print("#{}".format(i+1),b_price)
    else:
        print("#{}".format(i + 1), a_price)