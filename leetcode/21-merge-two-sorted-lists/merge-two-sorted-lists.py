# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 = n, list2 = m -> O(N)
        # 메모리 추가 사용 -> O(N)

        # stop 조건 -> 두 list 중 하나가 끝에 도달할 때
        if not list1:
            return list2
        if not list2:
            return list1

        # 재귀 호출
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2        