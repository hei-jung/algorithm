import sys
import heapq
input = sys.stdin.readline

min_heap = []  # 작은 -> 큰
max_heap = []  # 큰 -> 작은
for i in range(int(input())):
    x = int(input())
    if not max_heap:
        heapq.heappush(max_heap, -x)
    else:
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, -x)
        # max_heap 최댓값 > min_heap 최솟값일 경우 값 교환.
        if (-max_heap[0]) > min_heap[0]:
            max_top = -heapq.heappop(max_heap)
            min_top = heapq.heappop(min_heap)
            heapq.heappush(min_heap, max_top)
            heapq.heappush(max_heap, -min_top)
    print(-max_heap[0])
