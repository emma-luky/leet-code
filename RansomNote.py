class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = {}
        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for c in ransomNote:
            if c in letters:
                if letters[c] == 0:
                    return False
                letters[c] -= 1
            if c not in letters:
                return False
        return True
