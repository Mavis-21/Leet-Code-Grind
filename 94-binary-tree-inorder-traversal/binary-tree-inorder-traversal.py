class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        stack = []
        current = root
        
        # Traverse until we've visited all nodes and the stack is empty
        while current is not None or stack:
            # Reach the left most Node of the current Node
            while current is not None:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point, so we pop from stack
            current = stack.pop()
            result.append(current.val)
            
            # Now, we visit the right subtree
            current = current.right
            
        return result  