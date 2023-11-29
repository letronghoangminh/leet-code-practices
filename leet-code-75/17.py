from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def build_list(digits: str):
          map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
          }
          
          result = []
          
          for c in digits:
            result.append(map[c])
            
          return result

        def permute(level, s, digit):
          if level == 1:
            return s[digit]
          
          else:
            return [
              y + x
              for y in permute(1, s, digit)
              for x in permute(level - 1, s, digit + 1)
            ]

        if len(digits) == 0: return []
      
        return permute(len(digits), build_list(digits), 0)

print(Solution().letterCombinations("2"))