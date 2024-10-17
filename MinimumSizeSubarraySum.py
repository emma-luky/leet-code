class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        min_length = 0
        for num in nums:
            if(target <= 0):
                break
            target -= num
            min_length += 1
            print(target)
        if(target > 0):
            return 0
        return min_length
