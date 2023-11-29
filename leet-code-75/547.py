from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        self.provinces = 0
        
        def dfs(province):
          visited[province] = True
          
          for i in range(len(isConnected[province])):
            if visited[i]: continue
            if isConnected[province][i] == 1 and not visited[i]: dfs(i)
        
        
        for i in range(len(isConnected)):
          if visited[i]: continue
          
          self.provinces += 1
          dfs(i)
          
        return self.provinces

        