class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_text = ''.join(char for char in s if char.isalnum()).lower()
        print(clean_text)
        j = len(clean_text) - 1
        for i in range(len(clean_text)):
            if clean_text[i] != clean_text[j]:
                return False
            if i == j:
                break
            j -= 1
        return True
