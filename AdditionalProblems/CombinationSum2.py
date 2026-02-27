class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(temp, candidates, difference, index):
            if difference < 0:
                return
            if difference == 0:
                res.append(temp.copy())
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    if difference < candidates[i]:
                        break
                    temp.append(candidates[i])
                    backtrack(temp, candidates, difference - candidates[i], i + 1)
                    temp.pop()
        candidates.sort()
        backtrack([], candidates, target, 0)
        return res
