class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowels = 0
        current = 0
        
        for i in range(0, k):
          if s[i] in vowels: current += 1
        
        max_vowels = current

        for i in range(1, len(s) - k + 1):
          if s[i - 1] in vowels:
            current -= 1
          if s[i + k - 1] in vowels:
            current += 1 
          if current > max_vowels: 
            max_vowels = current
        
        return max_vowels

print(Solution().maxVowels('ibpbhixfiouhdljnjfflpapptrxgcomvnb', 33))