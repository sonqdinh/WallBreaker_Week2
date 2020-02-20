class Solution:
    def firstUniqChar(self, s: str) -> int:
        firstLetter = [-1] * 26
        
        for i, letter in enumerate(s):
            if firstLetter[ord(letter) - ord('a')] == -1:
                firstLetter[ord(letter) - ord('a')] = i
            elif firstLetter[ord(letter) - ord('a')] >= 0:
                firstLetter[ord(letter) - ord('a')] = -2
        
        firstUniq = len(s)
        
        for i in range(26):
            if firstLetter[i] >= 0:
                firstUniq = min(firstUniq, firstLetter[i])
        
        return -1 if firstUniq == len(s) else firstUniq