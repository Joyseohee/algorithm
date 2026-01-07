class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n - 1

        while start <= end:
            mid_idx = int((start + end) / 2)

            if nums[mid_idx] == target:
                return mid_idx

            if nums[mid_idx] < target:
                start = mid_idx + 1
            else:
                end = mid_idx - 1

        return -1