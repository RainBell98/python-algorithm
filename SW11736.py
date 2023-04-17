T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for j in range(len(a)):
        if j>=1 and j<len(a)-1:
            if a[j-1]<a[j]<a[j+1] or a[j-1]>a[j]>a[j+1]:
                cnt += 1
    print("#{}".format(i+1),cnt)

