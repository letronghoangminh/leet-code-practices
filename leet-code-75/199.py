from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
      
        queue = [[root, 0]]
        result = [None] * 100
        
        while not len(queue) == 0:          
          node = queue.pop(0)
          
          result[node[1]] = node[0].val
          
          if node[0].left: queue.append([node[0].left, node[1] + 1])
          if node[0].right: queue.append([node[0].right, node[1] + 1])
          
        return result[:result.index(None)]