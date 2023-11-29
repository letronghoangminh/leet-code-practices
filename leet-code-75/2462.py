from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_pointer, right_pointer = candidates, len(costs) - candidates
        total_cost = 0
        left_heap, right_heap = costs[:left_pointer], costs[right_pointer:]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        
        while k > 0:
          left = True

          if left_heap[0] <= right_heap[0]:
            print('left')
            print(left_heap)
            print(right_heap)
            total_cost += heapq.heappop(left_heap)
            left_pointer += 1
            left = True
            
            if left_pointer > abs(right_pointer):
              heapq.heappop(right_heap)
          else:
            print('right')
            print(left_heap)
            print(right_heap)
            total_cost += heapq.heappop(right_heap)
            right_pointer -= 1
            left = False

            if left_pointer > abs(right_pointer):
              heapq.heappop(left_heap)

          k -= 1

          if left_pointer == len(costs) or abs(right_pointer) > len(costs):
            break

          if left:
            heapq.heappush(left_heap, costs[left_pointer])
          else:
            heapq.heappush(right_heap, costs[right_pointer])

                
        if k > 0:
          for i in range(left_pointer - 1, len(costs)):
            heapq.heappush(left_heap, costs[i])
          
          total_cost += sum(heapq.nsmallest(k, left_heap))
        
        return total_cost
