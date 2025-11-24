class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0 for _ in range(n + 1)]

        def tribo(n):
            if n == 0:
                return 0
            if n <= 2:
                return 1

            t3 = memo[n-3] if memo[n-3] > 0 else tribo(n-3)
            t2 = memo[n-2] if memo[n-2] > 0 else tribo(n-2)
            t1 = memo[n-1] if memo[n-1] > 0 else tribo(n-1)

            t = t3 + t2 + t1
            
            memo[n] = t

            return t

        return tribo(n)


        

        