# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
            
        if p is None or q is None:
            return False
            
        if p.val != q.val:
            return False
            
        check_left_side = self.isSameTree(p.left, q.left)
        check_right_side = self.isSameTree(p.right, q.right)
        
        if check_left_side and check_right_side:
            return True
        else:
            return False
        