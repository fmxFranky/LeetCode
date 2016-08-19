class Solution(object):
    def maxArea_1(self, height):
        """
        爆搜
        :type height: List[int]
        :rtype: int
        """
        v = 0
        x, y = 0, 1
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if v < (j - i) * min(height[i], height[j]):
                    v = (j - i) * min(height[i], height[j])
                    x, y = i, j
        return v, x, y

    def maxArea_2(self, height):
        """
        设置头尾两个指针,根据贪心原理可以发现要想找到更优解可以从当前较短的板子向中间寻找比这个板子长的板子,同时更新更优解
        :type height: List[int]
        :rtype: int
        """

        def vol(i, j):
            return min(height[i], height[j]) * (j - i)

        left = 0
        right = len(height) - 1
        ans = 0
        while right > left:
            ans = max(ans, vol(left, right))
            l, r = height[left], height[right]
            if l > r:
                while r >= height[right] and right > left:
                    right -= 1
            else:
                while l >= height[left] and right > left:
                    left += 1
        return ans


if __name__ == '__main__':
    a = [1,2,3]
    # print(Solution().maxArea_1(a))
    print(Solution().maxArea_2(a))
