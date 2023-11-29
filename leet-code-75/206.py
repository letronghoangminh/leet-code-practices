from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        next = head.next
        prev = head
        cur = head
        
        while head and next:
          prev = cur
          cur = next
          next = next.next
          cur.next = prev
        
        head.next = None
        print(head)
        print(prev)
        print(next)
        print(cur)

        return cur