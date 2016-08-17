class Solution(object):
    def twoSum_1(self, nums, target):
        """
        遍历 nums 检查 target-nums[i] 是否在 nums 中并且和 i 不重复,找到满足条件的 i 后直接返回
        效率:36%
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        reversed_nums = nums[::-1]
        n = len(nums)
        for num in nums:
            if target-num in nums:
                x, y = nums.index(num), n-1-reversed_nums.index(target-num)
                if x-y:
                    return [x, y]

    def twoSum_2(self, nums, target):
        """
        先考虑特殊情况: target 偶数且解为 target/2,此时直接查找解在 list 中的位置
        如果不是特殊情况,则取 nums 和 target-nums 的交集得到两个因子在查找它们在 list 中的位置并排序
        效率:73%
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        from collections import Counter
        if target % 2 == 0 and Counter(nums)[target/2] == 2:
            a = nums.index(target/2)
            b = nums.index(target/2, a+1)
            return [a, b]
        else:
            factors = list(set(nums) & set([target-num for num in nums]))
            if target/2 in factors:
                factors.remove(target/2)
            a = nums.index(factors[0])
            b = nums.index(factors[1])
            return [a, b] if a < b else [b, a]

    def twoSum_3(self, nums, target):
        """
        遍历 nums 同时维护一个储存 target-num 的所在位置的 hash_map,发现已经存在的元素就当前遍历元素的位置和差的位置
        效率:43%
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hd = {}
        for i, num in enumerate(nums):
            if num in hd:
                return [hd[num], i]
            else:
                hd[target-num] = i


if __name__ == '__main__':
    slt = Solution()
    nums = [3,2,4,0,0]
    target = 5
    print(slt.twoSum_2(nums=nums, target=target))

