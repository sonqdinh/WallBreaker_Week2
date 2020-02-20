class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def genKey(s):
            odd = [0]*26
            even = [0]*26
            for i in range(len(s)):
                if i % 2:
                    odd[ord(s[i]) - ord('a')] += 1
                else:
                    even[ord(s[i]) - ord('a')] += 1
            
            oddKey = evenKey = ''
            
            for i in range(26):
                if odd[i]:
                    oddKey += (chr(i + ord('a')) * odd[i])
                    
                if even[i]:
                    evenKey += (chr(i + ord('a')) * even[i])
            
            return oddKey + evenKey
        
        setAns = set()
        
        for s in A:
            setAns.add(genKey(s))
        
        return len(setAns)
        