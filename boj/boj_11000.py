import sys
import heapq
input = sys.stdin.readline

n = int(input())  # 수업의 수
pq = []
for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(pq, (s, t))

classroom = []  # 강의실 모음
_, t0 = heapq.heappop(pq)
heapq.heappush(classroom, t0)
while pq:
    ti = heapq.heappop(classroom)
    sj, tj = heapq.heappop(pq)
    if ti <= sj:  # Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.
        heapq.heappush(classroom, tj)  # 끝나는 시간 업데이트
    else:
        heapq.heappush(classroom, ti)
        heapq.heappush(classroom, tj)

print(len(classroom))  # 강의실 개수 출력
