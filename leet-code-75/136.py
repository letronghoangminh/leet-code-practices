from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        max_num = defaultdict()
        
        for i in nums:
          if max_num.get(i): max_num[i] += 1
          else: max_num[i] = 1
          
        for k,v in max_num.items():
          if v == 1: return k
        
        
        