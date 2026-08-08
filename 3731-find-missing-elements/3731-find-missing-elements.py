class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        lo, hi = min(nums),max(nums)
        res = []
        for x in range(lo,hi+1):
            if x not in num_set:
                res.append(x)
        return res
        