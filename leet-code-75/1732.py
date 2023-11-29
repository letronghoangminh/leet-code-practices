class Solution:
    def largestAltitude(self, gain: [int]) -> int:
        points = [0]
        highest = 0
        
        for i in range(len(gain)):
          point = points[i] + gain[i]
          if point > highest: highest = point
          points.append(point)
          
        print(points)
        return highest

print(Solution().largestAltitude([52,-91,72]))