from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        countA = Counter(A.split())
        countB = Counter(B.split())
        
        ans = []
        
        for word in countA:
            if word not in countB:
                if countA[word] == 1:
                    ans.append(word)
            else:
                del countB[word]
        
        for word in countB:
            if countB[word] == 1:
                ans.append(word)
        
        return ans