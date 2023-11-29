from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        total_oranges = 0
        rotten_oranges = 0
        queue = deque()
        
        for i in range(len(grid)):
          for j in range(len(grid[i])):
            if grid[i][j] == 0: visited[i][j] = True
            if grid[i][j] == 1:
              total_oranges += 1 
            if grid[i][j] == 2: 
              total_oranges += 1
              rotten_oranges + 1
              queue.append([[i, j], 0])
        
        if total_oranges == rotten_oranges: return 0
        
        while len(queue) > 0:
          orange = queue.popleft()
          position = orange[0]
          time = orange[1]
          
          if position[0] < 0 or position[0] >= len(grid) or position[1] < 0 or position[1] >= len(grid[0]) or visited[position[0]][position[1]]: continue

          visited[position[0]][position[1]] = True
          rotten_oranges += 1
          
          if rotten_oranges == total_oranges: 
            return time
          
          queue.append([[position[0] + 1, position[1]], time + 1])
          queue.append([[position[0] - 1, position[1]], time + 1])
          queue.append([[position[0], position[1] + 1], time + 1])
          queue.append([[position[0], position[1] - 1], time + 1])
          
        return -1
