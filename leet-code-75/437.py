from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
      self.result = 0
      def dfs(root: TreeNode, arr: List[int]):
        if not root: return 0
        arr.append(root.val)
        local_sum = 0
        
        for i in range(len(arr) - 1, -1, -1):
          local_sum += arr[i]
          if local_sum == targetSum: self.result += 1
        
        dfs(root.left, arr.copy())
        dfs(root.right, arr.copy())
        
      dfs(root, [])
      return self.result