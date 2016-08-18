class Solution(object):
    def convert(self, s, numRows):
        """
        把图一画然后观察规律即可
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row = [[] for _ in range(numRows)]
        ans = ''
        for i in range(len(s)):
            mod = i % (2 * numRows - 2)
            line = mod if mod < numRows else numRows - 2 - (mod % numRows)
            row[line].append(s[i])
        for num in range(numRows):
            ans += ''.join(row[num])
        return ans


if __name__ == '__main__':
    print(Solution().convert('0123456789', 4))
