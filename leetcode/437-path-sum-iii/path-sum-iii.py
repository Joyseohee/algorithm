from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(root, curr_sum) -> int:
            if not root:
                return 0

            curr_sum += root.val
            need = curr_sum - targetSum
            curr_prefix = prefix_count[need]

            prefix_count[curr_sum] += 1

            left_prefix = dfs(root.left, curr_sum)
            right_prefix = dfs(root.right, curr_sum)

            prefix_count[curr_sum] -= 1

            return curr_prefix + left_prefix + right_prefix

        return dfs(root, 0)