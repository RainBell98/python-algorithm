import sys
N = int(input())

for _ in range(N):
    n , m = map(int,sys.stdin.readline().split())
    print(n+m)