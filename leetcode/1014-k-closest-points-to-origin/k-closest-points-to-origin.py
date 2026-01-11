import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_heap = []

        for x, y in points:
            dist = - (x ** 2 + y ** 2)
            heapq.heappush(k_heap, (dist, [x, y]))

            if len(k_heap) > k:
                heapq.heappop(k_heap)

        return [point for dist, point in k_heap]


        