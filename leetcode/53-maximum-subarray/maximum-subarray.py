import sys

class Solution:
    def maxSubArray(self, nums):
        # 초기값 설정: 첫 번째 원소로 시작
        max_sum = nums[0]      # 전체 최대 합 (우리가 반환할 결과)
        current_sum = nums[0]  # 현재 부분 배열의 합

        # 두 번째 원소부터 끝까지 순회
        for i in range(1, len(nums)):
            # 로직: (이전 합 + 현재 숫자) vs (현재 숫자) 중 큰 것을 선택
            # 즉, 이전 합이 마이너스여서 손해라면 현재 숫자부터 새로 시작함
            current_sum = max(nums[i], current_sum + nums[i])
            
            # 현재 계산된 합이 지금까지의 최대 합보다 크다면 갱신
            max_sum = max(max_sum, current_sum)
            
        return max_sum
        
        