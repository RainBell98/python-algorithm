N = int(input())
def devide(n):
    cnt1, cnt2, cnt3, cnt4, cnt5 = 1, 1, 1, 1, 1


for i in range(N):
    n = int(input())
    cnt1, cnt2, cnt3, cnt4, cnt5 = 0, 0, 0, 0, 0
    while n!=1:
        if n%2 == 0:
            cnt1 +=1
            n = n/2
        elif n%3 == 0:
            cnt2 +=1
            n = n/3
        elif n%5 == 0:
            cnt3 +=1
            n = n/5
        elif n%7 == 0:
            cnt4 +=1
            n = n/7
        elif n%11 == 0:
            cnt5 +=1
            n = n/11

    print("#{}".format(i+1),cnt2,cnt3,cnt4,cnt5)