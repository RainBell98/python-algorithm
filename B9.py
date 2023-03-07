N = int(input())

def F(n):
    if n==0:
        return 1
    else:
        return n*F(n-1)

print(F(N))