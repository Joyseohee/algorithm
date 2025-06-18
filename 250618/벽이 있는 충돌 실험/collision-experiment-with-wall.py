t = int(input())

direction_map = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

reverse_dir = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}

def in_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n

def simulate(n, marbles):
    for _ in range(2 * n):
        next_positions = {}

        # move marbles
        for x, y, d in marbles:
            dx, dy = direction_map[d]
            nx, ny = x + dx, y + dy

            if not in_bounds(nx, ny, n):
                nx, ny = x, y
                d = reverse_dir[d]

            if (nx, ny) not in next_positions:
                next_positions[(nx, ny)] = []
            next_positions[(nx, ny)].append(d)

        # remove duplicates
        marbles = [
            (x, y, dirs[0])
            for (x, y), dirs in next_positions.items()
            if len(dirs) == 1
        ]
    return len(marbles)

for _ in range(t):
    n, m = map(int, input().split())
    marbles = [tuple(input().split()) for _ in range(m)]
    marbles = [(int(x)-1, int(y)-1, d) for x, y, d in marbles]

    print(simulate(n, marbles))
