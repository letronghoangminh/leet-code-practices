class Solution:
    def compress(self, chars: [str]) -> int:
        if len(chars) == 1: return 1
        
        mappings = []
        mappings.append({'key': chars[0], 'value': 1})
        
        for i in range(1, len(chars)):
          if chars[i] == chars[i - 1]:
            mappings[len(mappings) - 1]['value'] += 1
          else:
            mappings.append({'key': chars[i], 'value': 1})
          
        chars = []
        result = 0
        print(mappings)
        for i in range(len(mappings)):
          value = int(mappings[i]['value'])
          chars.append(mappings[i]['key'])
          
          if value > 1:
            result += 1 + len(str(mappings[i]['value']))
            chars += [*str(mappings[i]['value'])]
          else:
            result += 1
        
        print(chars)
        return result
      
print(Solution().compress(["a","a","b","b","c","c","c"]))