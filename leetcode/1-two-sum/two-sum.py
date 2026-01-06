class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        nums_map = {}
        
        for i in range(n):
            compelete_num = target - nums[i]
            
            if compelete_num in nums_map:
                return [nums_map[compelete_num], i]
            
            nums_map[nums[i]] = i

        return []