class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = len(nums)
        p2 = 0

        while p2 < p1:
            if nums[p2] == val:
                tmp = nums[p1-1]
                nums[p1-1] = nums[p2]
                nums[p2] = tmp
                p1 -= 1
            else:
                p2 += 1

        return p1
