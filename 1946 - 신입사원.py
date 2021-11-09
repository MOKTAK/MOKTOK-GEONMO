import sys
# 시간 초과 주의
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    scores = []
    for n in range(N):
        scores.append(list(map(int, input().split())))
    scores.sort(key=lambda x: x[0])
    inter = scores[0][1]
    ans = 1
    for score in scores:
        if inter > score[1]:
            ans += 1
            inter = score[1]
    print(ans)
        
    