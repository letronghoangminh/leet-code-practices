from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_hours(speed: int):
          result = 0
          for i in piles:
            result += ceil(i / speed)
            
          return result
        
        l, r = 1, max(piles) + 1
        
        min_speed = float('inf')

        while l < r: 
          mid = l + (r - l) // 2
          hours = calc_hours(mid)
          if hours <= h:
            if mid < min_speed: min_speed = mid
            r = mid
          elif hours > h: l = mid + 1
          
        return min_speed if min_speed != float('inf') else ceil(piles[0] / h)