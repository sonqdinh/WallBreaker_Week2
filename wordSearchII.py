class Trie:
    def __init__(self):
        self.letters = dict()
        self.flag = False
        self.word = ''
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        if not words or len(board) == 0:
            return []
        
        ans = set()
        rows, cols = len(board), len(board[0])
        wordDict = Trie()
        
        def generate(word, n, trie):
            if n == len(word):
                trie.flag = True
                trie.word = word
            else:
                if word[n] not in trie.letters:
                    trie.letters[word[n]] = Trie()
                generate(word, n + 1, trie.letters[word[n]])
        
        def dfs(r, c, trie, visited):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] in trie.letters and (r, c) not in visited:
                if trie.letters[board[r][c]].flag:
                    ans.add(trie.letters[board[r][c]].word)
                    
                visited.add((r, c))
                
                dfs(r + 1, c, trie.letters[board[r][c]], visited)
                
                dfs(r - 1, c, trie.letters[board[r][c]], visited)
                
                dfs(r, c + 1, trie.letters[board[r][c]], visited)
                
                dfs(r, c - 1, trie.letters[board[r][c]], visited)
                
                visited.remove((r, c))

        for word in words:
            generate(word, 0, wordDict)
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, wordDict, set())
        
        return list(ans)
        
            
    