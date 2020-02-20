class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        set_MorseCode = set()
        
        for word in words:
            code = ''
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            set_MorseCode.add(code)
                
        return len(set_MorseCode)
            