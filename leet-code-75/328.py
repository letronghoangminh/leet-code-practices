
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        
        even_pointer = head
        odd_pointer = head.next
        backup_odd_pointer = odd_pointer
        
        while (even_pointer.next and even_pointer.next.next) or (odd_pointer.next and odd_pointer.next.next):
          if even_pointer.next.next: 
            even_pointer.next = even_pointer.next.next
            even_pointer = even_pointer.next
          if odd_pointer.next.next:
            odd_pointer.next = odd_pointer.next.next
            odd_pointer = odd_pointer.next
            
        odd_pointer.next = None
        even_pointer.next = backup_odd_pointer
        
        return head
