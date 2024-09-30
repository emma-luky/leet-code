class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        sofar = 0
        i = 0
        lookup = {}
        
        for j in range(len(s)):
            if s[j] in lookup:
                i = max(i, lookup[s[j]] + 1)
            
            lookup[s[j]] = j
            cur = j - i + 1
            sofar = max(cur, sofar)
        
        return sofar
