import sys
import heapq

input = sys.stdin.readline
MAX = sys.maxsize


def dijkstra(x):
    pq = []
    heapq.heappush(pq, (x, 0))
    dp[x] = 0
    while pq:
        x, c = heapq.heappop(pq)
        if dp[x] < c:
            continue
        for nx, nc in graph[x]:
            if dp[nx] > c + nc:
                dp[nx] = c + nc
                nodes[nx] = x
                heapq.heappush(pq, (nx, dp[nx]))


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    src, dst, cost = map(int, input().split())
    graph[src].append((dst, cost))
src, dst = map(int, input().split())
dp = [MAX] * (n + 1)
nodes = [i for i in range(n + 1)]
dijkstra(src)
print(dp[dst])

path = [str(dst)]
i = dst
while i != src:
    i = nodes[i]
    path.append(str(i))
print(len(path))
print(' '.join(reversed(path)))
