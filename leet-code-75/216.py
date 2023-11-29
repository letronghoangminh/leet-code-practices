from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtracking(prefix: int, k: int, digits: str):
          if k == 0:
            if prefix == n:
              res = sorted([int(x) for x in list(digits)])
              if res not in result: result.append(res)
          else:
            for i in range(1, 10):
              if str(i) not in digits: backtracking(prefix + i, k - 1, digits + str(i))
        
        backtracking(0, k, "")
        return list(result)
      
print(Solution().combinationSum3(3, 7))