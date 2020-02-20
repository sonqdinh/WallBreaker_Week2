class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        hashMap = {}
        sList = str.split()
        visited = set()
        if len(pattern) != len(sList):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in hashMap:
                    if sList[i] in visited:
                        return False
                    hashMap[pattern[i]] = sList[i]
                    visited.add(sList[i])
                else:
                    if hashMap[pattern[i]] != sList[i]:
                        return False
            return True