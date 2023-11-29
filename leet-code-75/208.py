class TrieNode:
  def __init__(self) -> None:
    self.children = [None for _ in range(26)]
  
    self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def charToIndex(self, char):
      return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        cur = self.root
      
        for c in word:
          node = cur.children[self.charToIndex(c)]
          if node:
            cur = node
          else:
            cur.children[self.charToIndex(c)] = TrieNode()
            cur = cur.children[self.charToIndex(c)]
          
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
      
        for c in word:
          node = cur.children[self.charToIndex(c)]
          
          if node == None: return False
          
          cur = node

        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
      
        for c in prefix:
          node = cur.children[self.charToIndex(c)]
          
          if node == None: return False
          
          cur = node

        return cur is not None


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.search("wor"))
print(obj.startsWith("a"))