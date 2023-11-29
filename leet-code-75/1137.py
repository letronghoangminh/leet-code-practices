class Solution:
    def tribonacci(self, n: int) -> int:
      result = [0, 1, 1]
      
      for i in range(3, n + 1):
        result.append(result[i - 1] + result[i - 2] + result[i - 3])
        
      return result[n]
    