class Solution:
    def longestSubarray(self, nums: [int]) -> int:
        left = right = 0
        k = 1
        
        for right in range(len(nums)):
          if nums[right] == 0:
            k -= 1
          if k < 0:
            if nums[left] == 0:
              k += 1
            left += 1
        print(right, left)
        return right - left


print(Solution().longestOnes([1,1,1]))
        
