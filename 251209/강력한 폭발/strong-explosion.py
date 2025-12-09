n = int(input())

bombs = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)],
    [(-1, 1), (-1, -1), (0, 0), (1, 1), (1, -1)]
]


points = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            points.append((i, j))

max_explode = 0

bomb_idxs = list()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def activate():
    global max_explode

    exploded_set = set()
    
    for i, idx in enumerate(bomb_idxs):
        x, y = points[i]
        for dx, dy in bombs[idx]:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                exploded_set.add((nx, ny))

    max_explode = max(max_explode, len(exploded_set))


def explode(depth):
    global bomb_idxs

    if depth == len(points):
        activate()
        return

    for i in range(len(bombs)):
        bomb_idxs.append(i)
        explode(depth + 1)
        bomb_idxs.pop()


explode(0)

print(max_explode)
