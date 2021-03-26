class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        cnt = 0

        # 1글자
        for i in range(n):
            dp[i][i] = 1
            cnt += 1

        for k in range(1, n):
            for i in range(k, n):
                if k > 2:  # 4글자 이상
                    if s[i - k] == s[i] and dp[i - k + 1][i - 1] == 1:
                        dp[i - k][i] = 1
                        cnt += 1
                else:  # 2, 3글자
                    if s[i - k] == s[i]:
                        dp[i - k][i] = 1
                        cnt += 1

        return cnt
