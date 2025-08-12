# 변수 선언 및 입력:
n, m, t, k = tuple(map(int, input().split()))
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def next_pos(x, y, vnum, move_dir):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    # vnum 횟수만큼 이동한 이후의 위치를 반환합니다.
    for _ in range(vnum):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        # 벽에 부딪히면
        # 방향을 바꾼 뒤 이동합니다.
        if not in_range(nx, ny):
            move_dir = 3 - move_dir
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
        x, y = nx, ny

    return (x, y, move_dir)


def move_all():
    for x in range(n):
        for y in range(n):
            for v, num, move_dir in grid[x][y]:
                next_x, next_y, next_dir = next_pos(x, y, v, move_dir)
                next_grid[next_x][next_y].append((v, num, next_dir))


def select_marbles():
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) >= k:
                # 우선순위가 높은 k개만 남겨줍니다.
                next_grid[i][j].sort(key=lambda x: (-x[0], -x[1]))
                while len(next_grid[i][j]) > k:
                    next_grid[i][j].pop()
            

def simulate():
    # Step1. next_grid를 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []
		
    # Step2. 구슬들을 전부 움직입니다.
    move_all()
    
    # Step3. 각 칸마다 구슬이 최대 k개만 있도록 조정합니다.
    select_marbles()
    
    # Step4. next_grid 값을 grid로 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


dir_mapper = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}

for i in range(m):
    r, c, d, v = tuple(input().split())
    r, c, v = tuple(map(int, [r, c, v]))

    # 살아남는 구슬의 우선순위가 더 빠른 속도, 더 큰 번호 이므로
    # (속도, 방향, 번호) 순서를 유지합니다.
    grid[r - 1][c - 1].append((v, i + 1, dir_mapper[d]))

# t초에 걸쳐 시뮬레이션을 반복합니다.
for _ in range(t):
    simulate()

ans = sum([
    len(grid[i][j])
    for i in range(n)
    for j in range(n)
])
print(ans)
