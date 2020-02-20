from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
#         if len(s) < len(p):
#             return []
        
#         pCount = Counter(p)
#         sCount = Counter(s[:len(p)])
        
#         ans = []
        
#         for i in range(0, len(s) - len(p) + 1):
#             if len(sCount - pCount) == 0:
#                 ans.append(i)
            
#             sCount[s[i]] -= 1
#             if i + len(p) < len(s):
#                 sCount[s[i + len(p)]] += 1
        
#         return ans
        def check(arr):
            for i in range(26):
                if arr[i]:
                    return False
            return True
    
        if len(s) < len(p):
            return []
        
        ans = []
        
        counter = [0]*26
        for ch in p:
            counter[ord(ch) - ord('a')] += 1
        
        for ch in s[:len(p)]:
            counter[ord(ch) - ord('a')] -= 1
        
        for i in range(0, len(s) - len(p) + 1):
            if check(counter):
                ans.append(i)
            
            counter[ord(s[i]) - ord('a')] += 1
            if i + len(p) < len(s):
                counter[ord(s[i + len(p)]) - ord('a')] -= 1
        
        return ans