# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_tmp = curr.next    #  3 -> 4 -> 5

            # 화살표 방향 전환
            # None <- 1 <- 2 <- 3 <- 4 <- 5
            curr.next = prev
            
            # 다음 작업 준비
            prev = curr
            curr = next_tmp

        return prev


        