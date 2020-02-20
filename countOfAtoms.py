from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        if not formula:
            return ''
        
        stack = [Counter()]
        
        N = len(formula)
        i = 0
        
        while i < N:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                
                while i < N and formula[i].isdigit():
                    i += 1
                
                multiply = int(formula[i_start: i] or 1)
                
                for atom, count in top.items():
                    stack[-1][atom] += multiply * count
                
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower():
                    i += 1
                
                atom = formula[i_start: i]
                
                i_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                
                count = int(formula[i_start: i] or 1)
                stack[-1][atom] += count
        
        atomCount = stack.pop()
        
        return ''.join([atom + (str(atomCount[atom]) if atomCount[atom] > 1 else '') for atom in sorted(atomCount.keys())])