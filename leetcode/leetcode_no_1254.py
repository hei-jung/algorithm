class Solution(object):
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            grid[i][j] = -1
            flag = True
            if i - 1 >= 0 and grid[i - 1][j] == 0:
                flag &= dfs(i - 1, j)
            if i + 1 < m and grid[i + 1][j] == 0:
                flag &= dfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == 0:
                flag &= dfs(i, j - 1)
            if j + 1 < n and grid[i][j + 1] == 0:
                flag &= dfs(i, j + 1)
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                flag = False
            return flag

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1

        return count
