import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(key=lambda x: -x)
ans = 0
for coin in coins:
    if coin > K:
        continue
    while coin <= K:
        ans += K // coin
        K %= coin
    if K == 0:
        break
print(ans)
