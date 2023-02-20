import sys
res = [0]*(10**6+1)
res[1] = 0

for i in range(2,10**6+1):
    if i % 6 == 0:
        res[i] = min(res[i//3]+1,res[i//2]+1,res[i-1]+1)
    elif i % 3 == 0:
        res[i] = min(res[i//3]+1,res[i-1]+1)
    elif i % 2 == 0:
        res[i] = min(res[i//2]+1,res[i-1]+1)
    else:
        res[i] = res[i-1]+1

print(res[int(input())])