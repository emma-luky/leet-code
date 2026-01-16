class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        sentence = ""
        for i in range(len(words) - 1, 0, -1):
            sentence += words[i] + " "
        sentence += words[0]
        return sentence
