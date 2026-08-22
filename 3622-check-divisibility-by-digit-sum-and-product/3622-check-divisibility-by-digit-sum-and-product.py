class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digitS = 0
        digitP = 1
        s=n

        while n>0:
            digit = n%10
            digitS += digit
            digitP *= digit

            n = n//10
        return s%(digitS+digitP) == 0
        