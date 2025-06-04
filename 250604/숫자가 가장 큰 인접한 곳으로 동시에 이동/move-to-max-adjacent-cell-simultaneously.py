n, m, t = map(int, input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
bids = [[0 for _ in range(n)] for _ in range(n)]
next_pos = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = map(int,input().split())
    bids[r-1][c-1] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for x in range(n):
        for y in range(n):
            if bids[x][y] == 0:
                continue

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    continue

                if grid[nx][ny] > grid[x][y]:
                    next_pos[nx][ny] += 1
                    next_pos[x][y] = 0
                    break
    
    for i in range(n):
        for j in range(n):
            if next_pos[i][j] == 1:
                bids[i][j] = 1
                next_pos[i][j] = 1
            else:
                bids[i][j] = 0
                next_pos[i][j] = 0
            
for _ in range(t):
    move()


print(sum([sum(bids[i]) for i in range(n)]))