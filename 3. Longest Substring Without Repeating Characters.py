class Solution(object):
    def lengthOfLongestSubstring_1(self, s):
        """
        i,j 分别是待求 substring 的 head 和 tail,从头开始判断, 一旦发现重复的元素就更新 i, 否则更新 j. 同时并维护 maxLength
        效率:20%
        :type s: str
        :rtype: int
        """
        i = j = 0
        n = len(s)
        ans = 0
        while i < n and j < n:
            if s[j] not in s[i:j]:
                j += 1
            else:
                i += s[i:j].find(s[j])+1
            ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    slt = Solution()
    print(slt.lengthOfLongestSubstring_1('absabsbb'))
