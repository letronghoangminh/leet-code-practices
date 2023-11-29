from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, flag, total):
          if not root: return total

          return max(dfs(root.left, False, total + 1 if flag else 1), dfs(root.right, True, total + 1 if not flag else 1))

        return dfs(root, None, 0) - 1