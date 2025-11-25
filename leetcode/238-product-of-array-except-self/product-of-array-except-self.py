class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        n = len(nums)

        answer = [0 for _ in range(n)]

        left = 1
        for i in range(n):
            left *= nums[i]
            answer[i] = left
        
        right = 1
        for i in range(n-1, -1, -1):
            right *= nums[i + 1] if i < n -1 else 1
            left = answer[i - 1] if i > 0 else 1
    
            answer[i] = left * right

        return answer