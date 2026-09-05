class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1
        area = 0

        while low < high:
            width = high - low
            current_height = min(height[low], height[high])
            cur_area = width * current_height

            area = max(area, cur_area)

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return area