class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert both lists to sets
        set1 = set(nums1)
        set2 = set(nums2)
        # Get the elements that are in set1 but not in set2
        ans1 = list(set1 - set2)
        # Get the elements that are in set2 but not in set1
        ans2 = list(set2 - set1)
        # Return the results as a list of two lists
        return [ans1, ans2]
