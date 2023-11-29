from math import ceil
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr: List[int], pivot):
          l, r = 0, len(arr)
          
          while l < r:
            mid = l + (r - l) // 2

            if arr[mid] >= pivot: r = mid
            else: l = mid + 1
          
          return l

        result = []        
        potions.sort()
        
        for i in spells:
          result.append(len(potions) - binary_search(potions, ceil(success / i)))
          
        return result
