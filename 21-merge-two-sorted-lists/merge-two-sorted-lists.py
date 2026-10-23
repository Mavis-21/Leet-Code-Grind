class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy_node = ListNode(-1)
        current_node = dummy_node
        
        pointer_one = list1
        pointer_two = list2
        
        while pointer_one is not None and pointer_two is not None:
            if pointer_one.val <= pointer_two.val:
                current_node.next = pointer_one
                pointer_one = pointer_one.next
            else:
                current_node.next = pointer_two
                pointer_two = pointer_two.next
            current_node = current_node.next
            
        if pointer_one is not None:
            current_node.next = pointer_one
        else:
            current_node.next = pointer_two
            
        return dummy_node.next
        