n, m, x, y = map(int, input().split())
x,y=x-1,y-1
moves = list(input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
dice=[1,6,2,5,4,3]
dice_num=6

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_dir_num(move):
    if move=='U':
        return 0
    if move=='D':
        return 1
    if move=='L':
        return 2
    return 3

def turn(move):
    #global dice

    dirc_map={
        "U":[0,2,1,3],
        "D":[0,3,1,2],
        "L":[0,5,1,4],
        "R":[0,4,1,5]
    }
    
    idx=dirc_map[move]

    tmp=dice[idx[0]]
    dice[idx[0]]=dice[idx[1]]
    dice[idx[1]]=dice[idx[2]]
    dice[idx[2]]=dice[idx[3]]
    dice[idx[3]]=tmp

def roll(move):
    global x,y
    dxs,dys=[-1,1,0,0],[0,0,-1,1]

    dirc=find_dir_num(move)

    nx,ny=x+dxs[dirc],y+dys[dirc]
    
    if not in_range(nx,ny):
        return

    turn(move)
    num=dice[1]
    x,y=nx,ny
    grid[nx][ny] = num

grid[x][y]=dice[1]
for move in moves:
    roll(move)

sum_num=0
for i in range(n):
    for j in range(n):
        sum_num+=grid[i][j]


print(sum_num)