class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n + 1
        mid = (l + r) // 2
        
        while True:
          res = guess(mid)
          if res == 0: return mid
          elif res == -1:
            r = mid
            mid =  (l + r) // 2
          else:
            l = mid
            mid =  (l + r) // 2
            