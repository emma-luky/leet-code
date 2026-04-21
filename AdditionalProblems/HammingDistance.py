class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        width = max(x.bit_length(), y.bit_length())
        xbin = format(x, f'0{width}b')
        ybin = format(y, f'0{width}b')
        count = 0
        for i in range(width):
            if xbin[i] != ybin[i]:
                count += 1
        return count
