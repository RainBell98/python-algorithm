N,K = map(int,input().split())
coin = [int(input()) for _ in range(N)]
coin.reverse()
ans = 0
for coin1 in coin:
    ans +=K
    K%=coin1

print(ans)