class Solution:
    def findDifference(self, nums1: [int], nums2: [int]) -> [[int]]:
        return [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]
        
print(Solution().findDifference([1,2,3,3], [1,1,2,2]))