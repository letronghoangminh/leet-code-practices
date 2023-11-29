class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        left_products = []
        right_products = []
        
        for i in range(len(nums)):
          if i == 0: 
            left_products.append(1)
          elif i == 1:
            left_products.append(nums[0])
          else:
            left_products.append(left_products[i - 1] * nums[i - 1])
          
        for i in range(len(nums) - 1, -1, -1):
          if i == len(nums) - 1: 
            right_products.append(1)
          elif i == len(nums) - 2:
            right_products.append(nums[len(nums) - 1])
          else:
            right_products.append(right_products[len(nums) - 1 - i - 1] * nums[i + 1])
        
        result = []
        for i in range(len(nums)):
          result.append(left_products[i] * right_products[len(nums) - 1 - i])
        
        return result
      