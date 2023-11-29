class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = [*s]
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_indexes = []
        
        for i in range(len(chars)):
          if chars[i].lower() in vowels: vowels_indexes.append(i)
          
          
        for i in range(len(vowels_indexes) // 2):
          chars[vowels_indexes[i]], chars[vowels_indexes[len(vowels_indexes) - i - 1]] = chars[vowels_indexes[len(vowels_indexes) - i - 1]], chars[vowels_indexes[i]]
        
        return "".join(chars)
      
print(Solution().reverseVowels('aA'))