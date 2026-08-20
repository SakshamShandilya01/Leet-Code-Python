class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        arr = []

        for row in grid:
            for x in row:
                arr.append(x)

        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]

        ans = []

        for i in range(0, len(arr), n):
            ans.append(arr[i:i+n])

        return ans
        