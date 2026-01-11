# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            next_tmp = curr.next

            # 방향 전환
            curr.next = prev
            
            # 다음 작업을 위한 저장 값 변경
            prev = curr
            curr = next_tmp

        return prev


