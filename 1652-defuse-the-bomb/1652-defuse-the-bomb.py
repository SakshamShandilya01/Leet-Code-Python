class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans

        for i in range(n):
            s = 0
            if k > 0:
                for j in range(1, k + 1):
                    s += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    s += code[(i - j) % n]
            ans[i] = s
        return ans