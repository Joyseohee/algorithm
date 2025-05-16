n,m,r,c=map(int,input().split())
grid=[[0 for _ in range(n)] for _ in range(n)]
grid[r-1][c-1]=1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def explode(row,col,t,new_grid):
    dxs,dys=[0,0,1,-1],[1,-1,0,0]

    for dx,dy in zip(dxs,dys):
        nr,nc=row+dx*t,col+dy*t
        if not in_range(nr,nc):
            continue

        new_grid[nr][nc]=1

def bomb(t):
    # 현재 폭탄이 있는 칸 기준으로 t 거리 동서남북에 bomb 추가
    new_grid=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[i][j]=grid[i][j]

    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                # print(f"i={i},j={j}")
                explode(i,j,t,new_grid)
    
    for i in range(n):
        for j in range(n):
            grid[i][j]=new_grid[i][j]

for i in range(1,m+1):
    bomb(i)

print(sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
]))