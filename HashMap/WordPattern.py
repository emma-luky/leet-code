class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        usedWords = set()
        dictionary = {}
        for i in range(len(pattern)):
            if words[i] in usedWords:
                if pattern[i] not in dictionary or dictionary[pattern[i]] != words[i]:
                    return False
            elif pattern[i] in dictionary:
                if dictionary[pattern[i]] != words[i]:
                    return False
            else:
                usedWords.add(words[i])
                dictionary[pattern[i]] = words[i]
        return True
