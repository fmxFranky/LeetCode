class Solution(object):
    def longestPalindrome_1(self, s):
        """
        暴力搜索
        效率:最后一组数据过不了
        p.s.我懒得剪枝了
        :type s: str
        :rtype: str
        """
        ans = ''
        cur = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                t = s[i:j + 1]
                if t == t[::-1] and len(t) > cur:
                    cur = len(t)
                    ans = t
        return ans

    def longestPalindrome_2(self, s):
        """
        爆搜 v2.0
        :type s: str
        :rtype: str
        """
        ans = ''
        cur = 0
        n = len(s)
        if n == 1:
            return s
        for cen in range(n - 1):
            offset = 0
            while cen - offset >= 0 and cen + offset < n:
                left, right = cen - offset, cen + offset
                if s[left] != s[right]:
                    break
                offset += 1
            offset -= 1
            if 2 * offset + 1 > cur:
                cur = 2 * offset + 1
                ans = s[cen - offset:cen + offset + 1]
            if s[cen] == s[cen + 1]:
                offset = 0
                while cen - offset >= 0 and cen + 1 + offset < n:
                    left, right = cen - offset, cen + 1 + offset
                    if s[left] != s[right]:
                        break
                    offset += 1
                offset -= 1
                if 2 * offset + 2 > cur:
                    cur = 2 * offset + 2
                    ans = s[cen - offset:cen + offset + 2]
        return ans

    def longestPalindrome_3(self, s):
        """
        Manacher 算法
        效率:70%
        :type s: str
        :rtype: str
        """
        # 预处理字符串:在所有空隙中插入特殊字符,这样可以不再考虑是奇数回文还是偶数回文的问题
        t = '@' + '@'.join(s) + '@'
        # right 代表当前探测到得回文串的最右端, center 代表此时包含最右端字符的回文串的轴的位置
        right = center = 0
        # ans[i] 代表当前位置的最长回文长度
        ans = [0] * len(t)
        ct = cur = 0
        for i in range(len(t)):
            # 核心判断:根据 i 和 right 的关系可以直接判断 ans[i] 的最小值从而避免重复搜索
            ans[i] = min(ans[2 * center - i], right - i) if i < right else 1
            while i - ans[i] >= 0 and i + ans[i] < len(t) and t[i - ans[i]] == t[i + ans[i]]:
                ans[i] += 1
            # 更新辅助参数
            if i + ans[i] - 1 > right:
                right = i + ans[i] - 1
                center = i
            if ans[i] > cur:
                cur = ans[i]
                ct = i
        return t[ct - (cur - 1):ct + (cur - 1) + 1].replace('@', '')

    def longestPalindrome_4(self, s):
        """
        动态规划
        状态转移方程
            f(i,j) = True if s[i:j] == s[i:j+1][::-1] else False
            f(i,j) = f(i+1,j-1) and s[i]==s[j]
        边界条件:
            f(i,i) = True
            f(i,i+1) = s[i]==s[i+1]
        从状态转移方程中就可以看出迭代方向,注意!
        效率:最后一组跑不过去
        :type s: str
        :rtype: str
        """
        import numpy as np
        n = len(s)
        f = np.zeros((n, n), dtype=bool)
        # # numpy 版本
        # for j in range(n):
        #     for i in range(j,-1,-1):
        #         f[i][j] = True if s[i]==s[j] and (j-i<2 or f[i+1][j-1]) else False
        # head, tail = np.where(f==True)
        # ans = np.argmax(tail-head)
        # return s[head[ans]:tail[ans] + 1]

        # 普通版本
        x = y = 0
        cur = 0
        for j in range(n):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i < 2 or f[i + 1][j - 1]):
                    f[i][j] = True
                    if j - i + 1 > cur:
                        x, y = i, j
                        cur = j - i + 1
        return s[x:y + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome_4("abass"))
