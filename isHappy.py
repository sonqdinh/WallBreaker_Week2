class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            nxt = 0
            while n:
                nxt += (n % 10) ** 2
                n //= 10
            return nxt
        
        found = set()
        while n != 1 and n not in found:
            found.add(n)
            n = happy(n)
        
        return True if n == 1 else False