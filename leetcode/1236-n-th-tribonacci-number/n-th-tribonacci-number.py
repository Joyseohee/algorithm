class Solution:
    def tribonacci(self, n: int) -> int:
        # T0, T1, T2 직접 처리
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        t0, t1, t2 = 0, 1, 1  # T0, T1, T2
        
        # i: 3 ~ n
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        
        return t2
