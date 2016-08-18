class Solution(object):
    def reverse(self, x):
        """
        题目要求考虑 int32溢出的情况
        :type x: int
        :rtype: int
        """
        s = str(x)
        sig = -1 if s[0] == '-' else 1
        if s[0] == '-':
            s = s.replace('-', '')
        ans = int(s[::-1]) * sig
        return 0 if ans < -2 ** 31 or ans > 2 ** 31 else ans
if __name__ == '__main__':
    print(Solution().reverse(30033))