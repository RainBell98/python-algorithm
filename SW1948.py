from datetime import datetime
def month(p):
    d1 = datetime(year=2023,month=p[0],day=p[1])
    d2 = datetime(year=2023,month=p[2],day=p[3])
    return (d2-d1).days+1
N = int(input())
for i in range(N):
    p = list(map(int,input().split()))
    res = month(p)
    print("#"+str(i+1),res)
