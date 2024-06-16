class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)) :
            for j in range(len(nums)):
                if(i == j) :
                    continue
                if(nums[i] + nums[j] == target) :
                    result = [i, j]
                    break


        return result
                    

        