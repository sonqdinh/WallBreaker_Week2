class TrieNode:
    def __init__(self):
        self.letter = [None] * 26
        self.flag = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for ch in word:
            index = ord(ch) - ord('a')
            if not trie.letter[index]:
                trie.letter[index] = TrieNode()
            trie = trie.letter[index]
        
        trie.flag = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for ch in word:
            index = ord(ch) - ord('a')
            if not trie.letter[index]:
                return False
            trie = trie.letter[index]
        
        return True if trie.flag else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not trie.letter[index]:
                return False
            trie = trie.letter[index]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)