class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 1:
                continue

            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                
                if n == 0:
                    return True

        return False

        