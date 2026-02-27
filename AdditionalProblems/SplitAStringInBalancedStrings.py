class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced = 0
        count = 0
        for c in s:
            if c == 'R':
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                count += 1
        return count
