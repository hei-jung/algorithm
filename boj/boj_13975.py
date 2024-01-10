import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    pq = list(map(int, input().split()))
    heapq.heapify(pq)
    s = 0  # 총 비용
    cnt = 1  # 합친 챕터 수
    while pq:
        if cnt == k:
            break
        c1 = heapq.heappop(pq)
        c2 = heapq.heappop(pq)
        x = c1 + c2
        heapq.heappush(pq, x)
        s += x
        cnt += 1
    print(s)
