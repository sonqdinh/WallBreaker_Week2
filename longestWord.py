class Solution:
    def longestWord(self, words: List[str]) -> str:
        maxAns = ['']
        words = set(words)
        
        def generate(word):
            
            if len(word) > len(maxAns[0]):
                maxAns[0] = word
            elif len(word) == len(maxAns[0]) and word < maxAns[0]:
                maxAns[0] = word
            
            for i in range(26):
                letter = chr(ord('a') + i)
                if word + letter in words:
                    generate(word + letter)
        
        generate('')
        return maxAns[0]