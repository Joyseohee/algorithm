class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        p1 = 0
        p2 = 0

        while p1 != m and p2 != n:
            if nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1

        if p1 != m:
            nums3.extend(nums1[p1:m])
        else:
            nums3.extend(nums2[p2:n])

        nums1[:] = nums3
