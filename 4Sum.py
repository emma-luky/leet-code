class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # [1,0,-1,0,-2,2]
        # [-2,-1,0,0,1,2]
        ans = []
        for a in range(len(nums)):
            for b in range(a+1, len(nums) - 1):
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        if [nums[a], nums[b], nums[c], nums[d]] not in ans:
                            ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        c += 1
        return ans
