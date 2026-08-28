class Solution(object):
    def generateParenthesis(self, n):
        result = []
        pending = [("", 0, 0)] 

        while pending:
            current, open_count, close_count = pending.pop()

            if len(current) == 2 * n:
                result.append(current)
                continue

            if close_count < open_count:
                pending.append((current + ")", open_count, close_count + 1))

            if open_count < n:
                pending.append((current + "(", open_count + 1, close_count))

        return result