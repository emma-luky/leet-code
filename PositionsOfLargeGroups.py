class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        left = 0
        right = 1
        size = 1
        res = []
        while right < len(s):
            if s[right] == s[left]:
                right += 1
                size += 1
            else:
                if size >= 3:
                    res.append([left, right - 1])
                size = 1
                left = right
                right = left + 1
        if size >= 3:
            res.append([left, right - 1])
        return res
