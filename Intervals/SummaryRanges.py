class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if len(nums) == 0:
            return ranges
        previous = nums[0]
        end = None
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                if i == len(nums) - 2:
                    end = nums[i+1]
                continue
            else:
                if previous == nums[i]:
                    ranges.append(str(previous))
                #record end of previous
                else:
                    ranges.append(str(previous) + "->" + str(nums[i]))
                #record start next 
                previous = nums[i + 1]
        if end is None:
            ranges.append(str(previous))
        else:
            ranges.append(str(previous) + "->" + str(end))
        return ranges
