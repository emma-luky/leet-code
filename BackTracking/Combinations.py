class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(combo, index):
            if len(combo) == k:
                res.append(combo[:])
                return
            if index == n:
                return
            
            combo.append(index + 1)
            backtrack(combo, index + 1)
            combo.pop()
            backtrack(combo, index + 1)
            
        backtrack([], 0)
        return res
