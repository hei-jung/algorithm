class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = s[0]   # s = "ac" 예시를 보고 기본값을 s의 첫 글자로 정했다.

        # 1글자
        for i in range(n):
            dp[i][i] = 1

        # 2글자
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                ans = s[i] + s[i+1]

        # 3글자
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if s[i]==s[j] and dp[i+1][j-1]==1:
                    dp[i][j] = 1
                    if len(ans) < k:
                        ans = s[i:j+1]

        return ans
