class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # sorted, so no point checking further
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # i, not i+1: reuse allowed
                path.pop()

        backtrack(0, target, [])
        return result