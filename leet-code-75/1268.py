from typing import List


class TrieNode:
  def __init__(self) -> None:
    self.children = [None for _ in range(26)]
  
    self.isEnd = False

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
          
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
      
        for c in word:
          node = cur.children[self.charToIndex(c)]
          
          if node == None: return False
          
          cur = node

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
      
        for c in prefix:
          node = cur.children[self.charToIndex(c)]
          
          if node == None: return False
          
          cur = node

        return cur is not None
      
    def searchPrefix(self, prefix: str) -> List[str]:
        result = []
        root = self.root

        for c in prefix:
          node = root.children[self.charToIndex(c)]
          if node == None: return []
          root = node
        
        def dfs(word, prefix):
          if word.isEnd: 
            result.append(prefix)
          for i in range(len(word.children)):
            if word.children[i]:
              if len(result) != 3: dfs(word.children[i], prefix + chr(97 + i))
        
        dfs(root, prefix)
        return result

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        
        trie = Trie()
        
        for prod in products:
          trie.insert(prod)
          
        for i in range(len(searchWord)):
          result.append(trie.searchPrefix(searchWord[:i + 1]))
          
        return result
        
print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))