class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        position = []

        for i in range(len(nums)):
            if(nums[i]==target):
                position.append(i)
        
        return position

        