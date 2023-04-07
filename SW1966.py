N = int(input())
print()
for i in range(1,N+1):
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    print("#",str(i).format(i),end=' ')
    for j in range(n):
        print(p[j],end=' ')
    print()
