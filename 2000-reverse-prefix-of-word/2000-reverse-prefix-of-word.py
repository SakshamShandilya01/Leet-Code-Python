class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        result=[]
        if ch in word:
            for i in range(word.index(ch),-1,-1):
                result.append(word[i])
            result.append(word[word.index(ch)+1:])
         
        return  ''.join(result) if result else word