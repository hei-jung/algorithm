import sys
import heapq
input = sys.stdin.readline

n = int(input())  # 숙제 개수
pq1 = []  # 데드라인 기준
for _ in range(n):
    d, r = map(int, input().split())  # 데드라인, 보상(컵라면 수)
    heapq.heappush(pq1, (d, r))
pq2 = []  # 보상 기준
while pq1:
    d, r = heapq.heappop(pq1)
    if len(pq2) < d:  # 문제 풀이 여부
        heapq.heappush(pq2, r)
    elif pq2[0] < r:  # 보상이 더 큰 문제 선택
        heapq.heappop(pq2)
        heapq.heappush(pq2, r)
print(sum(pq2))
