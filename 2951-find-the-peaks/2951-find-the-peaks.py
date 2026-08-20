class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(mountain)

        for i in range(1,n-1):

            if(mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]):
                ans.append(i)

        return ans
        