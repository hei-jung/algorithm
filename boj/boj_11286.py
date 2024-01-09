import sys
import heapq
input = sys.stdin.readline

pq = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if pq:
            _, min = heapq.heappop(pq)
            print(min)
        else:
            print(0)
    else:
        heapq.heappush(pq, (abs(x), x))
