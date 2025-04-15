NONE=-1
n=4

grid=[list(map(int,input().split())) for _ in range(n)]
new_grid=[[0 for _ in range(n)] for _ in range(n)]

def rotate():
    for i in range(n):
        for j in range(n):
            new_grid[i][j]=grid[n-j-1][i]
    for i in range(n):
        for j in range(n):
            grid[i][j]=new_grid[i][j]

def initiate():
    for i in range(n):
        for j in range(n):
            new_grid[i][j]=0

def drop():
    initiate()

    for j in range(n):
        current_num,idx=NONE,n-1
        for i in range(n-1,-1,-1):
            if not grid[i][j]:
                continue
            if current_num==NONE:
                current_num=grid[i][j]
            elif grid[i][j]==current_num:
                new_grid[idx][j]=current_num*2
                current_num=NONE
                idx-=1
            else:
                new_grid[idx][j]=current_num
                current_num=grid[i][j]
                idx-=1
        if current_num!=NONE:
            new_grid[idx][j]=current_num
            idx-=1


    for i in range(n):
        for j in range(n):
            grid[i][j]=new_grid[i][j]


    
def tilt(dirc):
    for _ in range(dirc):
        rotate()

    drop()

    for _ in range(n-dirc):
        rotate()

dirc={
    "D":0,
    "R":1,
    "U":2,
    "L":3
}

tilt(dirc[input()])

for i in range(n):
    for j in range(n):
        print(grid[i][j],end=" ")
    print()