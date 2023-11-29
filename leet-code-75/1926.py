from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        
        def checkBorder(position: List[int], row: int, column: int, entrance: List[int], maze: List[List[str]]) -> bool:
          if position == entrance: return False
          
          if maze[position[0]][position[1]] == '+':
            return False

          if (position[0] == row - 1 or position[0] == 0) or (position[1] == column - 1 or position[1] == 0): return True
          
          return False
        
        queue = deque()
        
        queue.append([entrance, 0])
        
        while len(queue) > 0:
          node = queue.popleft()
          position = node[0]
          step = node[1]

          if position[0] < 0 or position[0] >= len(maze) or position[1] < 0 or position[1] >= len(maze[0]) or maze[position[0]][position[1]] == '+': 
            continue
          if visited[position[0]][position[1]]: continue
        
          visited[position[0]][position[1]] = True

          if checkBorder(position, row=len(maze), column=len(maze[0]), entrance=entrance, maze=maze): 
            return step
          
          queue.append([[position[0] + 1, position[1]], step + 1])
          queue.append([[position[0], position[1] + 1], step + 1])
          queue.append([[position[0], position[1] - 1], step + 1])
          queue.append([[position[0] - 1, position[1]], step + 1])
        
        return -1
          
      
