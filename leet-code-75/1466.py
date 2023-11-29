from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        # adj = [[]] * n

        for connection in connections:
            adj[connection[0]].append([connection[1], 1])
            adj[connection[1]].append([connection[0], -1])
        visited = [False] * n
        self.changes = 0
        print(adj)
        # [[(2, -1)], [(2, 1)], [(1, -1), (0, 1)]]
        # [[(2, 1), (1, -1), (0, 1), (2, -1)], [(2, 1), (1, -1), (0, 1), (2, -1)], [(2, 1), (1, -1), (0, 1), (2, -1)]]


              
        def dfs(city):
          visited[city] = True
          for neighbor in adj[city]:
            if not visited[neighbor[0]]:
              if neighbor[1] == 1: 
                self.changes += 1 
              dfs(neighbor[0])

        dfs(0)
          
        return self.changes