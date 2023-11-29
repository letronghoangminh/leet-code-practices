from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_nodes = []
        
        while head is not None:
          list_nodes.append(head)
          head = head.next
        
        middle_index = len(list_nodes) // 2

        if middle_index > 0:
          list_nodes[middle_index - 1].next = list_nodes[middle_index + 1] if len(list_nodes) > 2 else None
          list_nodes[middle_index].next = None
        else:
          return None
        
        return list_nodes[0]