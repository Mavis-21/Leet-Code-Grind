class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # Skip the duplicate
            else:
                curr = curr.next            # Move to the next distinct node
                
        return head
