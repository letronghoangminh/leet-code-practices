class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        max_candies = max(candies)
        result = []
        
        for i in range(len(candies)):
          result.append(candies[i] + extraCandies >= max_candies)
        
        return result
      
print(Solution().kidsWithCandies([4,2,1,1,2], 1))