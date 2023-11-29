from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
          other = target - nums[i]
          if map.get(other) is not None: return [i, map[other]]
          map[nums[i]] = i
        
        