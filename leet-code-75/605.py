class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        if n <= 0 or len(flowerbed) == 0: return True
        if flowerbed[0] == 0 and len(flowerbed) == 1: return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            print(n)
            
        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1

        if n <= 0 or len(flowerbed) == 0: return True
        for i in range(1, len(flowerbed) - 1):
            if n == 0: return True
            
            if flowerbed[i - 1:i + 2] == [0, 0, 0]:
                flowerbed[i] = 1
                n -= 1
        return False

print(Solution().canPlaceFlowers([0,0,1,0,0], 1))