class Solution(object):
    def numIslands(self, grid):
        count = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1": return
            grid[i][j] = "X"  # 이미 탐색한 지역임을 표시
            dfs(i - 1, j)  # 상
            dfs(i + 1, j)  # 하
            dfs(i, j - 1)  # 좌
            dfs(i, j + 1)  # 우

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
