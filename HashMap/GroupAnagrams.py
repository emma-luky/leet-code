class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
