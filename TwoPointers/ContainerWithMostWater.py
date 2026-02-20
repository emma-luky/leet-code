class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = min(height[left], height[right]) * (right - left)
        while (left < right):
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            curr = min(height[left], height[right]) * (right - left)
            maximum = max(maximum, curr)
        return maximum
