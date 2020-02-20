class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        nJewels = 0
        
        for s in S:
            if s in jewels:
                nJewels += 1
        
        return nJewels