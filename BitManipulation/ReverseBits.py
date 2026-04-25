class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, '032b')
        reverse = "".join(reversed(binary))
        return int(reverse, 2)
