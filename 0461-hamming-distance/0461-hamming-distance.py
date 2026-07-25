class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        diff = x^y
        while diff:
            count += diff & 1
            diff>>=1
        return count
        
        