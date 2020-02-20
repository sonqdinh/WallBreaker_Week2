from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        sCount = Counter(s)
        
        sList = list(sCount.keys())
        
        sList.sort(key = lambda x: -sCount[x])
        
        ans = ''
        for ch in sList:
            ans += ch * sCount[ch]
        
        return ans