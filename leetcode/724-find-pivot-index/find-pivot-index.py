class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        right_pre = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):
            right_sum = right_pre[i + 1] if i < n - 1 else 0
            right_pre[i] = right_sum + nums[i]

        left = 0
        for i in range(n):
            left += nums[i - 1] if i > 0 else 0
            right = right_pre[i + 1] if i < n - 1 else 0
            if left == right:
                return i

        return -1
            

        