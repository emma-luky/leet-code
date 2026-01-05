class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, sum, temp):
            if sum == target:
                res.append(temp[:])
                return
            if index == len(candidates) or sum > target:
                return

            temp.append(candidates[index])
            backtrack(index, sum + candidates[index], temp)

            temp.pop()
            backtrack(index+1, sum, temp)
        backtrack(0, 0, [])
        return res
