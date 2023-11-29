from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      arr1 = []
      arr2 = []
      def dfs(root, arr):
        if not root: return
        if not root.left and not root.right: 
          return arr.append(root.val)
        dfs(root.left, arr)
        dfs(root.right, arr)
      
      dfs(root1, arr1)
      dfs(root2, arr2)
      
      if arr1 == arr2: return True
      return False

      
          
    