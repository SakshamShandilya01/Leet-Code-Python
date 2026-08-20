class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max = 0

        for i in sentences:

            words = i.split()
            count = len(words)

            if count>max:
                max = count
        return max

        