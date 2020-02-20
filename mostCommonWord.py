from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        
        for punc in "!?',;.":
            paragraph = paragraph.replace(punc, ' ')
        
        wordCount = Counter(paragraph.lower().split())
        
        mostCommon = 0
        ans = ''
        for word in wordCount:
            if word not in banned and wordCount[word] > mostCommon:
                mostCommon = wordCount[word]
                ans = word
        
        return ans