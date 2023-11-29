from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return
        
        def insert(root, node):
          if not root: return node
          
          if root.val < node.val:
            root.right = insert(root.right, node)
          elif root.val > node.val:
            root.left = insert(root.left, node)
            
          return root
        
        def create_bst(root):
          queue = deque()
          if root.left: queue.append(root.left)
          if root.right: queue.append(root.right)
          
          while len(queue) > 0:
            node = queue.popleft()
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            
            if root.left: insert(root.left, node)
            else: insert(root.right, node)
          
          return root.left if root.left else root.right

        def bst(root: TreeNode, key, prev: TreeNode):
          if not root: return
          
          if root.val == key:
            if prev.left == root: 
              prev.left = create_bst(root)
            else:
              prev.right = create_bst(root)

          if root.val < key: return bst(root.right, key, root)
          if root.val > key: return bst(root.left, key, root)
        
        if root.val == key: 
          return create_bst(root)
        bst(root, key, None)
        return root