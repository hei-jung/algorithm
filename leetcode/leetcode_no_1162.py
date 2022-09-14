from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        m, n = len(grid), len(grid[0])
        dist = -1

        # land 좌표만 가져오기
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])

        # 전부 water 또는 전부 land 이면 -1
        if len(q) == 0 or len(q) == m * n: return dist

        # 모든 좌표를 방문할 때까지 실행
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()  # land 좌표를 가져옴
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
                    # 인접 칸이 water 이면 해당 좌표 저장
                    if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] == 0:
                        q.append((x + i, y + j))
                        grid[x + i][y + j] = -1  # 방문 표시
            dist += 1  # 인접 칸 이동 횟수만큼 거리가 늘어남

        return dist
