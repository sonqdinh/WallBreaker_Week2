class ListNode:
    def __init__(self, val = -1, nxt = None):
        self.val = val
        self.next = nxt
        
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = [ListNode() for _ in range(1000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            index = key % 1000
            it = self.hashSet[index]
            newNode = ListNode(key, it.next)
            it.next = newNode

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = key % 1000
            it = self.hashSet[index]
            while it.next.val != key:
                it = it.next
            it.next = it.next.next
            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % 1000
        it = self.hashSet[index]
        
        while it:
            if it.val == key:
                return True
            it = it.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)