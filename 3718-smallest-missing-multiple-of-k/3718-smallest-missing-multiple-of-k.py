class Solution(object):
    def missingMultiple(self, nums, k):
        s = set(nums)
        i = 1
        while k*i in s:
            i+=1
        return k*i
        