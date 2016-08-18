class Solution(object):
    def isPalindrome(self, x):
        """
        不允许使用额外空间,所以只能用回文对称的性质来判断正反向"类二进制展开"的结果是否一致进而得到答案
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        l = 0
        a = b = 0
        y = x
        while x:
            print(y, l)

            a += (x % 10) * (2 ** l)
            x //= 10
            l += 1
        l -= 1
        while y:
            print(y, l)

            b += (y % 10) * (2 ** l)
            y //= 10
            l -= 1
        return True if a == b else False


if __name__ == '__main__':
    print(Solution().isPalindrome(-1201))
