class Solution:
    def equalPairs(self, grid: [[int]]) -> int:
        n = len(grid)
        cols = []
        rows = []
        
        for i in range(n):
          col = []
          for j in range(n):
            col.append(grid[j][i])
          cols.append(hash(tuple(col)))
          rows.append(hash(tuple(grid[i])))
          
        result = 0
        for i in range(n):
          for j in range(n):
            if rows[i] == cols[j]: 
              result += 1
            
        return result

print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))