class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()

        n = len(merged)
        mid = n // 2

        if n % 2 == 0:
            median = (merged[mid - 1] + merged[mid]) / 2.0
        else:
            median = merged[mid]

        return median