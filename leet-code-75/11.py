class Solution:
    def maxArea(self, height: [int]) -> int:
        max = 0
        right_pointer = len(height) - 1
        left_pointer = 0
        
        while left_pointer < len(height) and right_pointer > -1:
          area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)

          if area > max: max = area
          if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
          else:
            right_pointer -= 1  

        return max

print(Solution().maxArea([1,1]))