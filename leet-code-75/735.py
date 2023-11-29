class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stack = []
        
        for i in range(len(asteroids)):
          if asteroids[i] > 0: stack.append(asteroids[i])
          else:
            flag = True
            while len(stack) > 0 and stack[-1] > 0:
              if stack[-1] > abs(asteroids[i]): 
                flag = False
                break
              elif stack[-1] == abs(asteroids[i]): 
                stack.pop()
                flag = False
                break
              else: stack.pop()
            if flag: stack.append(asteroids[i])
            
          
        return stack
        
print(Solution().asteroidCollision([10,2,-5]))