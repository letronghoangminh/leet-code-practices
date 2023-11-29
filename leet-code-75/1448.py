class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, maximum):
          if not root: return 0
          if root.val >= maximum:
            return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
          return dfs(root.left, maximum) + dfs(root.right, maximum)
        
        return dfs(root, root.val)