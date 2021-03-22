class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
        cache = {}

        def dfs(i, m):
            if (i, m) in cache:
                return cache[(i, m)]

            if i + 2 * m >= n:
                cache[(i, m)] = piles[i]
                return cache[(i, m)]

            max_piles = piles[i] - min([dfs(i + x, max(x, m)) for x in range(1, 2 * m + 1)])
            cache[(i, m)] = max_piles
            return cache[(i, m)]

        return dfs(0, 1)
