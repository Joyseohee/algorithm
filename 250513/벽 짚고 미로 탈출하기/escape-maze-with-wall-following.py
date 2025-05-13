import sys

DIR_NUM = 4
n = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1

grid = [list(input()) for _ in range(n)]
visited = [[[False for _ in range(DIR_NUM)] for _ in range(n)] for _ in range(n)]
t=0
dirc=0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def is_wall(x,y):
    return in_range(x,y) and grid[y][x]=="#"

def move():
    global x,y,dirc,grid,t

    dxs,dys=[1,0,-1,0],[0,1,0,-1]
    
    if visited[y][x][dirc]:
        print(-1)
        sys.exit(0)

    visited[y][x][dirc]=True
    nx,ny = x+dxs[dirc], y+dys[dirc]

    if is_wall(nx,ny):
        dirc = (dirc - 1 + 4) % 4
    elif not in_range(nx,ny):
        x,y=nx,ny
        t+=1
    else:
        rx,ry = nx + dxs[(dirc + 1) % 4], ny + dys[(dirc + 1) % 4]
        if is_wall(rx,ry):
            x,y=nx,ny
            t+=1
        else:
            x,y=rx,ry
            t+=2
            dirc = (dirc + 1) % 4

while in_range(x,y):
    move()

print(t)