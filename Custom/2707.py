from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        index = 0
        result = 0
        dictionary = sorted(dictionary, key=lambda x: -len(x))
        print(dictionary)
        
        while index < len(s):
          flag = False
          char = s[index]
          
          for i in dictionary:
            if i[0] == char and i == s[index:index + len(i)]: 
              index += len(i)
              flag = True
              break
            
          if not flag: 
            print(s[index], end="")
            result += 1
            index += 1
        
        return result
          