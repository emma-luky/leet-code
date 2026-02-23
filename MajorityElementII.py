class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appearances = {}
        ans = []
        n = len(nums)
        for num in nums:
            if num in appearances:
                appearances[num] += 1
            else:
                appearances[num] = 1
            if appearances[num] > n/3 and num not in ans:
                    ans.append(num)
        return ans
