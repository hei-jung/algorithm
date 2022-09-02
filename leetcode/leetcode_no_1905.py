class Solution(object):
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])
        count = 0

        def dfs(i, j):
            flag = True  # 겹치는 섬이면 True, 아니면 False
            grid2[i][j] = -1  # 방문 표시

            # grid2[i][j]가 1이 아니면 섬이 아님
            if grid1[i][j] != 1:
                flag = False

            # 이웃하는 칸과 섬을 이루는지, 그게 grid1에서도 같은지 확인
            if i - 1 >= 0 and grid2[i - 1][j] == 1:
                flag &= dfs(i - 1, j) & grid1[i - 1][j]
            if i + 1 < m and grid2[i + 1][j] == 1:
                flag &= dfs(i + 1, j) & grid1[i + 1][j]
            if j - 1 >= 0 and grid2[i][j - 1] == 1:
                flag &= dfs(i, j - 1) & grid1[i][j - 1]
            if j + 1 < n and grid2[i][j + 1] == 1:
                flag &= dfs(i, j + 1) & grid1[i][j + 1]

            return flag

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1

        return count
