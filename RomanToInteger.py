class Solution:
    def romanToInt(self, s: str) -> int:
        # for i in range(len(str) - 1, 0, -1):
        for i in range(len(str)-1):
            if str[i] == 'I':
                if str[i + 1] == 'V' or str[i + 1] == 'X':
                    total -= 1
                else:
                    total += 1
            elif str[i] = 'V':
                total += 5
            elif str[i] = 'X':
                if str[i + 1] == 'L' or str[i + 1] == 'C':
                    total -= 10
                else:
                    total += 10
