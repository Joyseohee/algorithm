class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        is_gretest = [False for _ in range(n)]

        # 사탕의 최댓값
        max_candy = max(candies)

        # 배열 순회하면서 extra를 더했을 때 > 최대값보다 큰지
        for idx, candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                is_gretest[idx] = True
        
        return is_gretest      
        