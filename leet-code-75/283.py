class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return

        left_pointer = -1
        
        for i in range(len(nums)):
          if nums[i] == 0:
            left_pointer = i
            break
        
        if left_pointer == -1: return
        
        for i in range(1, len(nums)):
          if nums[i] != 0 and i > left_pointer:
            for j in range(left_pointer, i + 1):
              nums[j], nums[left_pointer] = nums[left_pointer], nums[j]
            left_pointer += 1

print(Solution().moveZeroes([1,0,1]))
