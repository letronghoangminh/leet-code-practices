class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        
        words.reverse()
        
        return " ".join(words)

print(Solution().reverseWords("a good   example"))