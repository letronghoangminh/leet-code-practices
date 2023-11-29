from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        max_sum = -10000000
        max_depth = 1
        cur_sum = 0
        cur_depth = 1
        
        queue.append([root, 1])
        
        while not len(queue) == 0:
          node = queue.popleft()
          
          if node[0].left: queue.append([node[0].left, node[1] + 1])
          if node[0].right: queue.append([node[0].right, node[1] + 1])
          if node[1] == cur_depth:
            cur_sum += node[0].val
          else:
            if cur_sum > max_sum:
              max_sum = cur_sum
              max_depth = cur_depth
            cur_sum = node[0].val
            cur_depth = node[1]
            
        if cur_sum > max_sum:
          max_sum = cur_sum
          max_depth = cur_depth
            
        return max_depth
          