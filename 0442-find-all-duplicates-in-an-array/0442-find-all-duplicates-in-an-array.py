class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0:
                ans.append(abs(x))
            else:
                nums[i] = -nums[i]
        return ans