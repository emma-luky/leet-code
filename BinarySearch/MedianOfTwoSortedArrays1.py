# this is my first submission, used merged sort
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Append any remaining elements from nums1 (if any)
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Append any remaining elements from nums2 (if any)
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        length = len(merged)
        index = length // 2
        if length % 2 == 0:
            return (merged[index] + merged[index-1]) / 2
        else:
            return merged[index]
