class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            i_val = nums[i]
            for j in range(len(nums)):
                j_val = nums[j]
                if(i_val + j_val == target and i != j):
                    output.append(i)
                    output.append(j)
                    return output
        