n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
max_time = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def change_dirc(slash, last_dirc):
    directions = {
        1 : {
            0 : 1,
            1 : 0,
            2 : 3,
            3 : 2
        },
        2: {
            0 : 3,
            3 : 0,
            2 : 1,
            1 : 2
        }
    }
    return directions[slash][last_dirc]

def go(r, c, dirc):
    t = 1
    x, y = r, c
    dirc_dict = [
        (1, 0), (0, -1), (-1, 0), (0, 1)
    ]

    while in_range(x,y):
        if grid[x][y] != 0:
            dirc = change_dirc(grid[x][y], dirc)

        t+=1
        dx, dy = dirc_dict[dirc]
        x, y = x + dx, y + dy
    return t

# 테두리 순회
for i in range(n):
    max_time = max(go(0, i, 0), max_time)
    max_time = max(go(i, n-1, 1), max_time)
    max_time = max(go(n-1, i, 2), max_time)
    max_time = max(go(i, 0, 3), max_time)

print(max_time)


