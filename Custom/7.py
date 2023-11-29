class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        n = abs(x)
        
        while n > 0:
          res = res * 10 + n % 10
          n //= 10
          
        if (res > 0 and res > pow(2, 31) - 1) or (res < 0 and res < pow(-2, 31)): return 0
        
        return res if x > 0 else -res;