class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        leftsum = 0
        
        totalSum = sum(nums)
          
        for i in range(len(nums)):
          if leftsum * 2 + nums[i] == totalSum: return i
          leftsum += nums[i]
        
        return -1

print(Solution().pivotIndex([2,1,-1]))