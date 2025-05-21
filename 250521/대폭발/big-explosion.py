n,m,r,c=map(int,input().split())
grid=[[0 for _ in range(n)] for _ in range(n)]
grid[r-1][c-1]=1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def explode(row,col,t,new_grid):
    dxs,dys=[0,0,1,-1],[1,-1,0,0]

    for dx,dy in zip(dxs,dys):
        nr,nc=row+dx*(2**(t-1)),col+dy*(2**(t-1))
        if in_range(nr,nc):
            new_grid[nr][nc]=1

def bomb(t):
    new_grid = [row[:] for row in grid]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                explode(i, j, t, new_grid)

    # grid를 업데이트
    for i in range(n):
        for j in range(n):
            grid[i][j] = grid[i][j] or new_grid[i][j]

for i in range(1,m+1):
    bomb(i)

print(sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
]))