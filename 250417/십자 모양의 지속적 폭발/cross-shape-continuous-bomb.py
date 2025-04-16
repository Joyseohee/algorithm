n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def find_first_idx(c):
    for i in range(n):
        if grid[i][c] != 0:
            return i
    return None

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def explode(row, col):
    if row is None:
        return
    
    dist = grid[row][col]
    if dist >= 1:
        grid[row][col] = 0

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for l in range(1, dist):
        for dx, dy in zip(dxs, dys):
            nr, nc = row + dy * l, col + dx * l
            if not in_range(nr, nc):
                continue
                
            grid[nr][nc] = 0

def drop():
    temp_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        last_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                temp_grid[last_row][j] = grid[i][j]
                last_row -= 1
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]


for _ in range(m):
    c = int(input()) - 1
    first_idx = find_first_idx(c)

    if first_idx is not None:
        explode(first_idx, c)
    
    drop()

for row in grid:
    for num in row:
        print(num,end=" ")
    print()

