# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p랑 q가 전부 root 왼쪽에 있다면 -> 왼쪽 노드만 탐색한다
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # p랑 q가 전부 root 오른쪽에 있다면 -> 오른쪽 노드만 탐색한다
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # 그것도 아니면 -> 노드를 찾고 return
        else:
            return root

    
        