class Solution(object):
    def findMedianSortedArrays_1(self, nums1, nums2):
        """
        先排序再找中位数
        p.s.不符合提题目的时间复杂度的要求
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = k = 0
        m, n = len(nums1), len(nums2)
        merge = []
        while i < m or j < n:
            if i == m:
                merge.append(nums2[j])
                j += 1
            elif j == n:
                merge.append(nums1[i])
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    merge.append(nums1[i])
                    i += 1
                else:
                    merge.append(nums2[j])
                    j += 1
        print(merge)
        return merge[(n + m) // 2] if (n + m) % 2 else (merge[(m + n) // 2] + merge[(m + n) // 2 - 1]) / 2

    def findMedianSortedArrays_2(self, nums1, nums2):
        """
        该方法基于更强的问题:如何寻找有序数组中第k小的元素
        核心原理是如果第k小的元素在a中的位置是i那么它在中的位置必然是k-i-1.简言之就是用二分查找两个数组中的第k//2小的元素,然后根据比较结果的大小选择舍弃较小项所在数组的前k//2项,
        最后递归查找第k-k//2小的元素,时间复杂度为 O(log(m+n))
        效率:50%
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findKth(a, m, b, n, k):
            if m > n:
                return findKth(b, n, a, m, k)
            if m == 0:
                return b[k - 1]
            if k == 1:
                return min(a[0], b[0])
            x = min(k // 2, m)
            y = k - x
            if a[x - 1] == b[y - 1]:
                return a[x - 1]
            elif a[x - 1] < b[y - 1]:
                return findKth(a[x:], m - x, b, n, k - x)
            else:
                return findKth(a, m, b[y:], n - y, k - y)

        m, n = len(nums1), len(nums2)
        if (n + m) % 2:
            return findKth(nums1, m, nums2, n, (n + m) // 2 + 1)
        else:
            return (findKth(nums1, m, nums2, n, (n + m) // 2) + findKth(nums1, m, nums2, n, (n + m) // 2 + 1)) / 2


def median(nums):
    l = len(nums)
    return nums[l // 2] if l % 2 else (nums[l // 2] + nums[l // 2 - 1]) / 2


if __name__ == '__main__':
    a = [1, 2]
    b = [3, 4]
    print(Solution().findMedianSortedArrays_1(a, b))
    print('------------')
    print(Solution().findMedianSortedArrays_2(a, b))
