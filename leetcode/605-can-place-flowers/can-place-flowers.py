class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        planted_count = 0

        if length == 1:
            planted_count = 1 if flowerbed[0] == 0 else 0
            return planted_count >= n

        # 화단을 순회하면서 양 옆에 인접한 꽃이 없다면 꽃을 추가
        for i in range(length):
            if flowerbed[i] == 1:
                continue
            
            if i == 0 and flowerbed[1] == 0:
                flowerbed[i] = 1
                planted_count += 1

            elif i == length - 1 and flowerbed[length - 2] == 0:
                flowerbed[i] = 1
                planted_count += 1

            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                planted_count += 1
            
        return planted_count >= n

        