class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        isNegative, i, result = False, 0, 0
        while i < len(str) and str[i] == ' ': i += 1
        if len(str) == i: return 0
        isNegative = str[i]=='-'
        i += 1 if str[i]=='-' or str[i]=='+' else 0
        cnt = 0
        while i < len(str) and cnt <= 10:
            t = ord(str[i]) - ord('0')
            if 0 <= t <= 9:
                result = result * 10 + t
            else:
                break
            i += 1
            cnt += 1
        result = -result if isNegative else result
        if result >= 2147483647:
            return 2147483647
        elif result <= -2147483648:
            return -2147483648
        else:
            return result
