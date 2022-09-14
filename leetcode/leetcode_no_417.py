class Solution(object):
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pacific = []
        atlantic = []

        def dfs(r, c, visited, prev):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited:
                return

            if heights[r][c] < prev:
                return

            visited.append((r, c))

            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n - 1, atlantic, heights[r][n - 1])

        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m - 1, c, atlantic, heights[m - 1][c])

        return list(set(pacific) & set(atlantic))