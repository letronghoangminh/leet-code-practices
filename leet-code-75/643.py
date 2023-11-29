class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = sum(nums[:k])

        for i in range(1, len(nums) - k + 1):
          cur_sum = cur_sum - nums[i - 1] + nums[i + k - 1]
          if cur_sum > max_sum: 
            max_sum = cur_sum
        
        return max_sum / k

print(Solution().findMaxAverage([-1], 1))