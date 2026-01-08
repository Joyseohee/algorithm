# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def calc_depth(root, depth):
            if not root:
                return depth

            left = calc_depth(root.left, depth + 1)
            right = calc_depth(root.right, depth + 1)
            return max(left, right)

        def diff_depth(root):
            if not root:
                return True

            if not diff_depth(root.left):
                return False
            if not diff_depth(root.right):
                return False

            left = calc_depth(root.left, 0)
            right = calc_depth(root.right, 0)

            if abs(left - right) > 1:
                return False

            return True
            
        
        return diff_depth(root)

        
            

        