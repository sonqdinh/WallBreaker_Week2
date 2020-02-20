from collections import Counter

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        count = Counter(candies)
        
        kind = list(count.keys())
        
        kind.sort(key = lambda x: count[x])
        
        nKind = 0
        
        for i in kind:
            nKind += 1
            if nKind > len(candies) // 2:
                return nKind - 1
        
        return nKind