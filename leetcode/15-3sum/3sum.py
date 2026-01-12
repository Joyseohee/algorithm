class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n - 2):  # 하나는 지정하고 나머지 2개를 찾음
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 포인터 설정 : left는 현재보다 뒤(중복 제거), right는 맨 뒤에서부터(이미 중복 제거된 상태이므로)
            left, right = i + 1, n - 1
            print(f"left={left}, right={right}, nums[{i}]={nums[i]}")

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # 필요한 값이면 정답 리스트에 추가
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result











        