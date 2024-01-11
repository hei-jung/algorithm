import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if abs(festival_x - x) + abs(festival_y - y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                dist = abs(nx - x) + abs(ny - y)
                if dist <= 1000:  # 다음 50m 이동 가능한 지
                    q.append((nx, ny))
                    visited[i] = True
    print("sad")
    return

for _ in range(int(input())):
    n = int(input())  # 편의점 개수
    home_x, home_y = map(int, input().split())  # 상근이네 집
    store = []  # 편의점
    visited = [False] * n  # 편의점 방문 여부
    for _ in range(n):
        store_x, store_y = map(int, input().split())
        store.append((store_x, store_y))
    festival_x, festival_y = map(int, input().split())  # 페스티벌
    bfs(home_x, home_y)
