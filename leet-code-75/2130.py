from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        maximum = 0
        
        while head:
          arr.append(head.val)
          head = head.next
          
        for i in range(len(arr) // 2):
          sum = arr[i] + arr[len(arr) - i - 1]
          if sum > maximum: maximum = sum
        
        return maximum