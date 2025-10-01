import math, statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_combined = nums1 + nums2
        nums_combined.sort()
        average = 0
        print(nums_combined)
        n = len(nums_combined)
        print(n)
        if n % 2 != 0:
            median_index = math.ceil(n/2) - 1
            return nums_combined[median_index]
        else:
            median_index_1 = (n//2) - 1
            median_index_2 = median_index_1 + 1
            median = (nums_combined[median_index_1] + nums_combined[median_index_2])/2
            return float(median)
            