class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countLetter = [0]*26
        
        for i in range(len(s)):
            countLetter[ord(s[i]) - ord('a')] -= 1
            countLetter[ord(t[i]) - ord('a')] += 1
        
        countLetter[ord(t[-1]) - ord('a')] += 1
        
        for i in range(26):
            if countLetter[i]:
                return chr(i + ord('a'))