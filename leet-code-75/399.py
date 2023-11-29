from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map = defaultdict(dict)
        
        for (divided, divisor), value in zip(equations, values):
            map[divided][divisor] = value
            map[divisor][divided] = 1.0 / value
            
        self.result = []
        
        def dfs(divided, divisor):
          if self.visited.get(divided): return 0
          
          self.visited[divided] = True
          if map[divided].get(divisor): return map[divided][divisor]
          
          else:
            for key in map[divided].keys():
              result = map[divided][key] * dfs(key, divisor)
              if result is not None and result != 0: return result
          return 0
        
        for query in queries:
          self.visited = {}
          if query[0] not in map.keys() or query[1] not in map.keys():
            self.result.append(-1.0)
          else:
            if query[0] == query[1]: 
              self.result.append(1.0)
              continue
            result = dfs(query[0], query[1])
            self.result.append(result if result != 0 else -1.0)

        return self.result
