from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        # clear path가 만들어질 수 없으면 -1
        if grid[0][0] or grid[-1][-1]: return -1

        q = deque([(0, 0)])
        visited = set([(0, 0)])
        count = 1  # clear path 길이
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()  # 현재 위치 좌표
                if i == n - 1 and j == n - 1:
                    return count
                for x, y in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                    if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][j + y] == 0 and (i + x, j + y) not in visited:
                        q.append((x + i, y + j))  # 다음 번지로 지정
                        visited.add((x + i, y + j))  # 방문 표시
            count += 1
        return -1
