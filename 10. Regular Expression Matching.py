class Solution(object):
    def isMatch(self, s, p):
        """
        动态规划
        注意边界条件和'*'的条件讨论
        效率:32%
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s)+1,len(p)+1
        dp = [[False for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = True if (j > 0 and p[j-1]=='*' and dp[0][j-2]) or j==0 else False
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1]=='*':
                    dp[i][j]=dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (p[j-2]=='.' or s[i-1]==p[j-2]))
                else:
                    dp[i][j] = (s[i-1]==p[j-1] or p[j-1]=='.') and dp[i-1][j-1]
        return dp[m-1][n-1]
if __name__ == '__main__':
    Solution().isMatch('aa','a')