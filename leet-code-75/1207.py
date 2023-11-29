class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        mapping = {}
        
        for i in arr:
          if mapping.get(str(i)) is None: mapping[str(i)] = 1
          else: mapping[str(i)] += 1
          
        values = mapping.values()
        
        if len(values) > len(set(values)): return False
        return True
      
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))