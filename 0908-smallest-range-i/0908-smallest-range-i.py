class Solution(object):
    def smallestRangeI(self, nums, k):
        minv = nums[0]
        maxv = nums[0]

        for i in range(1,len(nums)):
            minv = min(minv,nums[i])
            maxv = max(maxv,nums[i])
        return max(0,(maxv-k)-(minv+k))
        