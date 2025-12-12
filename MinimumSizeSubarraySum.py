class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_length = float('inf')
        sum = 0
        count = 0
        l = 0
        r = 0
        while l < len(nums):
            if sum < target and r < len(nums):
                sum += nums[r]
                r += 1
                count += 1
            else:
                if sum >= target:
                    min_length = min(min_length, count)
                sum -= nums[l]
                l += 1
                count -= 1
        if min_length == float('inf'):
            return 0
        return min_length
