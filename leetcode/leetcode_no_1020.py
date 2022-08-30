class Solution(object):
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0  # grid 테두리랑 이어져 있는 지역 중에서 탐색 끝난 곳
            if i - 1 >= 0 and grid[i - 1][j]: dfs(i - 1, j)
            if i + 1 < m and grid[i + 1][j]: dfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1]: dfs(i, j - 1)
            if j + 1 < n and grid[i][j + 1]: dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j]:
                    dfs(i, j)

        # 남아있는 1 합산
        return sum(sum(grid[i]) for i in range(m))
