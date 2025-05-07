n,r,c=map(int,input().split())
r,c=r-1,c-1
grid = [list(map(int,input().split())) for _ in range(n)]

visited = [grid[r][c]]

def in_range(x,y):
    return 0<=x<n and 0<=y<n



while True:
    dxs,dys=[0,0,-1,1],[-1,1,0,0]

    flag = False

    for dx,dy in zip(dxs,dys):
        nx,ny=c+dx,r+dy
        
        if in_range(nx,ny) and grid[ny][nx] > grid[r][c]:
            r,c=ny,nx
            visited.append(grid[r][c])
            flag=True
            break

    if not flag:
        break
        
for num in visited:
    print(num,end=" ")