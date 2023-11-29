from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = []
        
        for i in range(len(nums1)):
          pq.append([nums1[i], nums2[i]])
          
        sorted_pq = sorted(pq, key=lambda x: -x[1])
        result = 0
        heap = []
        sum = 0
        
        for i in range(len(sorted_pq)):
          sum += sorted_pq[i][0]
          heapq.heappush(heap, sorted_pq[i][0])

          if len(heap) == k:
            result = max(sum * sorted_pq[i][1], result)
            sum -= heapq.heappop(heap)
          
        return result

