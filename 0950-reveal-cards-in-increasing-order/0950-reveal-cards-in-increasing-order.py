class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        deck.sort()
        idx = deque(range(n))

        ans = [0] * n
        for val in deck:
            ans[idx.popleft()] = val
            if idx:
                idx.append(idx.popleft())
        return ans