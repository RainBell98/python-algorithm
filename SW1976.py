N = int(input())
hour = 0
for i in range(N):
    n,m,k,p = map(int,input().split())
    minu = m+p
    if minu>=60:
        hour = 1
        minu -= 60
    hour += n+k
    if hour >= 13:
        hour -= 12

    print("#"+str(i+1),hour,minu)
    hour = 0