class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        n = len(nums)

        left_prefix = [0 for _ in range(n)]
        right_prefix = [0 for _ in range(n)]

        answer = [0 for _ in range(n)]

        left, right = 1, 1
        for i in range(n):
            left *= nums[i]
            left_prefix[i] = left

            right *= nums[n-1-i] 
            right_prefix[n-1-i] = right

        for i in range(n):
            left_product = left_prefix[i - 1] if i > 0 else 1
            right_product = right_prefix[i + 1] if i < n-1 else 1
            
            answer[i] = left_product * right_product

        return answer