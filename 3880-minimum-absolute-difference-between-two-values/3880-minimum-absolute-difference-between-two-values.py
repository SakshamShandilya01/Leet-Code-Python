class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index1 = []
        index2 = []

        for i in range(len(nums)):
            if nums[i] == 1:
                index1.append(i)

            if nums[i] == 2:
                index2.append(i)

        ans = float('inf')

        for x in index1:
            for y in index2:
                ans = min(ans,abs(x-y))
        if ans == float('inf'):
          return -1

          
        return ans
        