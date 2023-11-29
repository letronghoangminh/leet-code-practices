class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = root
        self.depth = 1
        
        def dfs(root: TreeNode, depth: int):
          if not root: return 0
          if root == p: 
            sum = 1 + dfs(root.left, depth + 1) + dfs(root.right, depth + 1)
          elif root == q: 
            sum = 2 + dfs(root.left, depth + 1) + dfs(root.right, depth + 1)
          else:
            sum = dfs(root.left, depth + 1) + dfs(root.right, depth + 1)

          if root.val == 5:
            print(sum)

          if sum == 3 and depth > self.depth:
            self.lca = root
            self.depth = depth

          return sum
        
        dfs(root, 1)
        
        return self.lca