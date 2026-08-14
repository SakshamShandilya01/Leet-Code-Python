class Solution(object):
    def sortArrayByParity(self, nums):
        ans = []
        for i in nums:
            if(i%2==0):
                ans.append(i)
                continue
                
        for i in nums:
            if(i%2!=0):
                ans.append(i)
        return ans
        