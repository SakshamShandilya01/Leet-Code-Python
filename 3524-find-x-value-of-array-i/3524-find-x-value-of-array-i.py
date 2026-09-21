class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0] * k
        cnt = [0] * k
        for x in nums:
            m = x % k
            nxt = [0] * k
            for r in range(k):
                nxt[(r * m) % k] += cnt[r]
            nxt[m] += 1
            cnt = nxt
            for r in range(k):
                res[r] += cnt[r]
        return res