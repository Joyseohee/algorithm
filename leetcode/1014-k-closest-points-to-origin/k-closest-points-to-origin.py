class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # x+y값이 가장 작은 거 k개
        # 정렬 알고리즘 O(NlogN) 10^4*log2_10^4 -> 10^5 -> 안정적

        points.sort(key = lambda x: x[0] ** 2 + x[1] ** 2)
        # print(points)

        return points[:k]


        