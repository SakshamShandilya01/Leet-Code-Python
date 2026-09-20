class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i, ch in enumerate(s):
            ans += (ord('z') - ord(ch) + 1) * (i + 1)
        return ans