from typing import List


class TrieNode:
  def __init__(self) -> None:
    self.children = [None for _ in range(26)]
    self.isEnd = False


class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def charToIndex(self, char: str):
        return ord(char) - 97
      
    def insert(self, word: str):
        cur = self.root
        
        for i in word:
          index = self.charToIndex(i)
          if not cur.children[index]: cur.children[index] = TrieNode()

          cur = cur.children[index]
        cur.isEnd = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
          self.insert(word)

    def search(self, searchWord: str) -> bool:
        self.result = False

        def dfs(node, i, k):
          if node.isEnd and k == 0 and i == len(searchWord): self.result = True

          if k < 0 or i == len(searchWord): return

          else:
            index = self.charToIndex(searchWord[i])
              
            for child in range(len(node.children)):
              if node.children[child]: 
                if child == index: dfs(node.children[index], i + 1, k)
                else: dfs(node.children[child], i + 1, k - 1)
          
          
        dfs(self.root, 0, 1)
        return self.result
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
magicDictionary = MagicDictionary()
magicDictionary.buildDict(["hello","hallo","leetcode","judge"])
print(magicDictionary.search("hello"))