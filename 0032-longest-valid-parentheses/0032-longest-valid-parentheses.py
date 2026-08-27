class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        open_count = close_count = 0
        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count == close_count:
                max_len = max(max_len, 2 * close_count)
            elif close_count > open_count:
                open_count = close_count = 0

        open_count = close_count = 0
        for ch in reversed(s):
            if ch == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count == close_count:
                max_len = max(max_len, 2 * open_count)
            elif open_count > close_count:
                open_count = close_count = 0

        return max_len