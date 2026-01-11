class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        # Base Case: 원소가 하나만 남았을 때
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # 1. 왼쪽 절반에서의 최대 합 (재귀)
        left_max = self.helper(nums, left, mid)
        
        # 2. 오른쪽 절반에서의 최대 합 (재귀)
        right_max = self.helper(nums, mid + 1, right)
        
        # 3. 가운데를 걸치는 부분의 최대 합 (별도 계산)
        cross_max = self.cross_sum(nums, left, right, mid)
        
        # 세 가지 경우 중 가장 큰 값 반환
        return max(left_max, right_max, cross_max)

    def cross_sum(self, nums, left, right, mid):
        # [중심 -> 왼쪽]으로 가면서 최대 합 구하기
        # 주의: 반드시 mid를 포함해서 왼쪽으로 뻗어나가야 함
        left_sub_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sub_sum = max(left_sub_sum, curr_sum)
            
        # [중심 -> 오른쪽]으로 가면서 최대 합 구하기
        # 주의: 반드시 mid+1을 포함해서 오른쪽으로 뻗어나가야 함
        right_sub_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sub_sum = max(right_sub_sum, curr_sum)
            
        # 두 방향의 최대 합을 더해서 반환
        return left_sub_sum + right_sub_sum