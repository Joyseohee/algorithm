t = int(input())

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

REVERSE_DIRECTION = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def read_marble_input():
    x, y, d = input().split()
    return (int(x) - 1, int(y) - 1, d)

def move(marble, n):
    x, y, d = marble
    dx, dy = DIRECTIONS[d]
    nx, ny = x + dx, y + dy
    if in_range(nx, ny, n):
        return (nx, ny, d)
    else:
        return (x, y, REVERSE_DIRECTION[d])

def remove_collided(marbles, n):
    grid = [[0] * n for _ in range(n)]
    for x, y, _ in marbles:
        grid[x][y] += 1
    return [m for m in marbles if grid[m[0]][m[1]] == 1]

def simulate(marbles, n):
    for _ in range(2 * n):
        marbles = [move(m, n) for m in marbles]
        marbles = remove_collided(marbles, n)
    return marbles

for _ in range(t):
    n, m = map(int, input().split())
    marbles = [read_marble_input() for _ in range(m)]
    result = simulate(marbles, n)
    print(len(result))
