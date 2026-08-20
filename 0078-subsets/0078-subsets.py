class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        