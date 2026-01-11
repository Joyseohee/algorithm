from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))    # 모든 0을 큐에 담음
                else:
                    mat[i][j] = -1


        # 모든 0에서 1로 가는 최단 거리를 찾아서 채움
        # bfs로 큐에서 꺼내서 확인
        dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
        
        while q:
            cx, cy = q.popleft()    # 현재 위치

            # 1의 자리에 먼저 닿는 0이 최단거리이므로 visited != -1이면 탐색 대상 X
            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy
                
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == -1: 
                    mat[nx][ny] = mat[cx][cy] + 1
                    q.append((nx, ny))

        return mat


        
        