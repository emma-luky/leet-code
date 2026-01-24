class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
            if t[i] in map:
                map[t[i]] -= 1
            else:
                map[t[i]] = -1
                
        for key, val in map.items():
            if val != 0:
                return False
        return True
