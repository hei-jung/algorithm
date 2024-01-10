import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in range(n):
        if len(pq) < n:
            heapq.heappush(pq, tmp[i])
        elif pq[0] < tmp[i]:
            heapq.heappop(pq)
            heapq.heappush(pq, tmp[i])
print(heapq.heappop(pq))
