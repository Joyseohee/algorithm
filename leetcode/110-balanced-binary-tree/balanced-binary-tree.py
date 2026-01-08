# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # 높이를 계산하면서 동시에 균형 여부를 체크하는 헬퍼 함수
        def check_height(node) -> int:
            # 기저 사례: 노드가 없으면 높이는 0
            if not node:
                return 0
            
            # 왼쪽 자식의 높이 체크
            left_height = check_height(node.left)
            if left_height == -1:  # 왼쪽 서브트리가 이미 불균형이면
                return -1          # 즉시 -1 반환 (Pruning)
            
            # 오른쪽 자식의 높이 체크
            right_height = check_height(node.right)
            if right_height == -1: # 오른쪽 서브트리가 이미 불균형이면
                return -1          # 즉시 -1 반환 (Pruning)
            
            # 현재 노드에서 균형 체크 (높이 차이가 1 초과인지)
            if abs(left_height - right_height) > 1:
                return -1
            
            # 균형이 맞다면, 현재 노드의 높이를 반환 (자식 중 큰 높이 + 1)
            return max(left_height, right_height) + 1
            
        # 결과가 -1이면 False, 아니면 True
        return check_height(root) != -1