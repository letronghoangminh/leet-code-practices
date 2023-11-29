from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        self.rooms_visited = 0
        
        def dfs(room):
          visited[room] = True
          self.rooms_visited += 1
          keys = rooms[room]
          
          for key in keys:
            if not visited[key]: dfs(key)
          

        dfs(0)
        
        if self.rooms_visited == len(rooms): return True
        return False