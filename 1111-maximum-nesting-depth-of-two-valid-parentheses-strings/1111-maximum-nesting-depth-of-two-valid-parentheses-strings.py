class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        depth = 0
        ans = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == '(':
                depth += 1
                ans[i] = depth % 2
            else:
                ans[i] = depth % 2
                depth -= 1
        return ans