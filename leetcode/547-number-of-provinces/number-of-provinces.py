class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        provinces = 0
        
        visited = [0 for _ in range(n)]

        def dfs(i):
            visited[i] = 1

            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    dfs(j)

        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                provinces += 1

        return provinces
