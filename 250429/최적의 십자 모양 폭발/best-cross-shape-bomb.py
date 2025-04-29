n=int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

max_count=0

def copy_grid(old_grid):
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[i][j] = old_grid[i][j]
    return new_grid

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_max(new_grid):
    count = 0
    for i in range(n):
        for j in range(1,n):
            if new_grid[i][j]==0:
                continue
            if new_grid[i][j] == new_grid[i][j-1]:
                count+=1
    
    for j in range(n):
        for i in range(1,n):
            if new_grid[i][j]==0:
                continue
            if new_grid[i][j] == new_grid[i-1][j]:
                count+=1

    return count


def explode(dist, row, col):
    global grid, max_count

    dxs, dys = [0,-1,0,1],[1,0,-1,0]
    new_grid = copy_grid(grid)
    new_grid[row][col] = 0
    for d in range(1,dist):
        for dx,dy in zip(dxs,dys):
            nx,ny = col + d*dx, row + d*dy
            if not in_range(nx,ny):
                continue
            
            new_grid[ny][nx] = 0

    for j in range(n):
        tmp = [new_grid[i][j] for i in range(n) if new_grid[i][j]!=0]
        for i in range(n):
            new_grid[i][j] = tmp.pop() if tmp else 0
    
    max_count = max(find_max(new_grid), max_count)


for i in range(n):
    for j in range(n):
        center = grid[i][j]
        explode(center, i,j)

print(max_count)