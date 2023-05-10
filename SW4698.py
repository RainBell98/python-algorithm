n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
T = int(input())
for i in range(T):
    arr = []
    cnt = 0
    d,a,b = map(int,input().split())
    for j in primes:
        if a<=j<=b:
            while j:
                if j%10 == d:
                    cnt+=1
                    break
                else:
                    j//=10
    print("#{}".format(i+1),cnt)
