class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        len_num = len(nums)
        if len_num < 3: return False

        left_mins = []
        right_max = []

        for i in range(len_num - 1):
          if i == 0: 
            left_mins.append(0)
          elif i == 1:
            left_mins.append(nums[0]) 
          else:
            left_mins.append(left_mins[i - 1] if left_mins[i - 1] < nums[i - 1] else nums[i - 1])
        
        for i in range(len_num - 1, -1, -1):
          if i == len_num - 1:
            right_max.append(0)
          elif i == len_num - 2:
            right_max.append(nums[len_num - 1])
          else:
            right_max.append(right_max[len_num - i - 2] if right_max[len_num - i - 2] > nums[i + 1] else nums[i + 1])
        
        print(left_mins)
        print(right_max)
        for i in range(1, len_num -1):
          if left_mins[i] < nums[i] and right_max[len_num - i - 1] > nums[i]: return True

        return False

print(Solution().increasingTriplet([4,5,2147483647,1,2]))
          