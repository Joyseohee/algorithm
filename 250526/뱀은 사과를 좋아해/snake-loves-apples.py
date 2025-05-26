n,m,k=map(int,input().split())
apples=[tuple(map(int,input().split())) for _ in range(m)]
x,y=0,0

directions={
    'U':(-1,0),
    'D':(1,0),
    'R':(0,1),
    'L':(0,-1),
}

t=0

grid=[[0 for _ in range(n)] for _ in range(n)]
dir_grid=[["" for _ in range(n)] for _ in range(n)]
lx, ly = x, y
lenght=1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(d,p):
    global t, lenght, x, y, lx, ly, grid, dir_grid

    dx, dy = directions[d]
    
    for i in range(p):
        t+=1

        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            # print("OUT OF RANGE")
            return False
        
        if grid[nx][ny] == 2:
            # 기존 거 그대로 두고 하나 더 1 추가
            lenght+=1

        # 꼬리를 옮기고 한칸 전진
        else:
            ls_dirc = dir_grid[lx][ly]
            if ls_dirc != "":
                ldx,ldy = directions[ls_dirc]
                grid[lx][ly] = 0
                lx, ly = lx + ldx, ly + ldy
            
        if grid[nx][ny] == 1:
            # print("MEET")
            return False
        
        #지나가기 직전에 현재 위치에 디렉션 표기
        dir_grid[x][y] = d
        
        #지나가기
        grid[nx][ny] = 1
        x, y = nx, ny
        # print(f"i={i}, nx={nx}, ny={ny}")
        # print("grid::" , grid)
        # print("dir_grid::", dir_grid)

    return True

for row, col in apples:
    grid[row-1][col-1] = 2

for _ in range(k):
    d,p=input().split()
    p=int(p)
    flag=move(d,p)
    if not flag:
        break

print(t)

    
    
