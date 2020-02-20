class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = dict()
        hashSet = set()
        
        for i in range(len(s)):
            if s[i] not in hashMap:
                if t[i] in hashSet:
                    return False
                hashMap[s[i]] = t[i]
                hashSet.add(t[i])
            else:
                if hashMap[s[i]] != t[i]:
                    return False
        
        return True