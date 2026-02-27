class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        counts = {}
        target = len(arr)/4
        for num in arr:
            if num in counts:
                counts[num] += 1
                if counts[num] > target:
                    return num
            else:
                counts[num] = 1
