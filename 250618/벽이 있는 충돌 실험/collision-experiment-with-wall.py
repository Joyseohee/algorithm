t = int(input())
directions = {
        "U" : (-1, 0),
        "D" : (1, 0),
        "L" : (0, -1),
        "R" : (0, 1)
}

change_dirc = {
        "U" : "D",
        "D" : "U",
        "L" : "R",
        "R" : "L"
}

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

def put_bids(marbles):
    x, y, d = tuple(input().split())
    x, y = int(x) - 1, int(y) - 1

    marbles.append((x,y,d))

def move(marble):
    x, y, d = marble
    dx, dy = directions[d]
    nx, ny = x + dx, y + dy
    if in_range(nx, ny):
        return (nx, ny, d)
    else:
        return (x, y, change_dirc[d])

def remove_duplicate(marbles):
    bids = [[0 for _ in range(n)] for _ in range(n)]

    for x, y, _ in marbles:
        bids[x][y] += 1
        
    return [
        marble
        for marble in marbles
        if bids[marble[0]][marble[1]] == 1
    ]


def move_bids(marbles):
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)
    
    return remove_duplicate(marbles)

for i in range(t):
    n, m = map(int, input().split())
    marbles = []

    for _ in range(m):
        put_bids(marbles)

    for _ in range(2 * n):
        marbles = move_bids(marbles)
        

    print(len(marbles))