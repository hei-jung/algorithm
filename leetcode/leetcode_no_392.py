class Solution(object):
    def isSubsequence(self, s, t):
        n = len(s)
        if n == 0: return True
        i = 0
        for c in t:
            if s[i] == c: i += 1
            # subsequence 조건을 만족하면 더 이상 탐색하지 않도록 한다.
            # 시간 효율을 위해서!
            if i == n: break
        return True if i==n else False