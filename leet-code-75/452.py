from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1

        points.sort(key=lambda x: x[1])
        
        arrows = len(points)
        cur_max = points[0][1]
        
        for i in range(1, len(points)):
          if cur_max >= points[i][0] and cur_max <= points[i][1]:
            arrows -= 1
          else:
            cur_max = points[i][1]
        
        return arrows
      
print(Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))