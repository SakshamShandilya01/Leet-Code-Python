class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicate = set()

        for i in nums:
            if(i in duplicate):
                return True

            else:
                duplicate.add(i)

        return False
                
        