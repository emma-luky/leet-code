class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = []
        freq = {}
        for c in words[0]:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
                    
        for i in range(1, len(words)):
            currFreq = {}
            for c in words[i]:
                if c in currFreq:
                    currFreq[c] += 1
                else:
                    currFreq[c] = 1 
            for key in list(freq.keys()):
                if key not in currFreq:
                    del freq[key]
                else:
                    freq[key] = min(freq[key], currFreq[key])
                    
        ans = []
        for key,val in freq.items():
            for i in range(val):
                ans.append(key)
                
        return ans
