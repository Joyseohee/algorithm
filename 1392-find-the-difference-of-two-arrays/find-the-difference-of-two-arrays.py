class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1= set()
        hash2= set()
        
        for num in nums1:
            hash1.add(num)

        for num in nums2:
            hash2.add(num)
        
        arr1=[]
        arr2=[]

        hash_c = hash1 & hash2
        
        arr1 = hash1 - hash_c
        arr2 = hash2 - hash_c

        return [arr1, arr2]