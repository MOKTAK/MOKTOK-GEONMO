M, N = map(int, input().split())

friends = []

for _ in range(N):
    friends.append(int(input()))

 
# 정렬이 핵심, 부족한 캔디를 나눠야 하니 
# 캔디를 많이 원하는 애들이
# 자기가 본래 원하던 것보다 더 적게 부족해야함
#  1 5
#  30 20 10 5 4라고 하면
#  68개 부족
#  부족한 것을 배분할 때 큰 것부터 하면
#  30 20 10 5 3이 되버림
#  작은 것 부터 하면
#  29 20 10 5 4가 되어 최소를 만들 수 있음
friends.sort()
remain = sum(friends) - M
for i, candy in enumerate(friends):
    friends[i] = min(candy, remain // (len(friends)-i))
    remain -= friends[i]
anger = 0
for candy in friends:
    anger += candy ** 2

print(anger % (2**64))