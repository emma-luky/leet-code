class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_indices = {}
        t_indices = {}
        for i in range(len(s)):
            if s_indices.get(s[i]) is None:
                s_indices[s[i]] = i
            if t_indices.get(t[i]) is None:
                t_indices[t[i]] = i
            if s_indices[s[i]] != t_indices[t[i]]:
                return False
        return True
