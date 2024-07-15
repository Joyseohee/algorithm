class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 뒤에서부터 오면서 남겨야하면 담고 아니면 포인터 옮기기
        if len(nums) < 2:
            return len(nums)

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k
