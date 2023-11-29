from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: return min(cost)
        min_costs = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
          min_costs.append(cost[i] + min(min_costs[i - 1] + min_costs[i - 2], min_costs[i - 2], min_costs[i - 1]))
        
        i += 1
        min_costs.append(min(min_costs[i - 1] + min_costs[i - 2], min_costs[i - 2], min_costs[i - 1]))
        return min_costs[-1]
        