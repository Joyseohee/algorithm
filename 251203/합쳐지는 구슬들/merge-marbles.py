from collections import deque

n, m, t = map(int, input().split())
n += 1

bids = [() for _ in range(m)]
grid = [[() for _ in range(n)] for _ in range(n)]

for i in range(m):
    r, c, d, w = input().split()
    r, c, w = int(r), int(c), int(w)
    
    bids[i] = ((r, c, d, w))

direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

mirror = {
    'U':'D',
    'D':'U',
    'R':'L',
    'L':'R'
}

def in_range(x, y):
    return 1 <= x < n and 1 <= y < n

for i in range(t):
    new_grid = [[[0, -1] for _ in range(n)] for _ in range(n)]

    # 만나면 무게는 합치고
    # 방향은 가장 큰 index

    m = len(bids)


    for j in range(m):
        # print(j, bids)
        if bids[j][0] == -1:
            continue
        
        r, c, d, w = bids[j]
        dx, dy = direction[d]

        nr, nc = r + dx, c + dy
        # print(i,j,bids[j])
        if not in_range(nr, nc):
            d = mirror[d]
            nr, nc = r, c

        ow = new_grid[nr][nc][0]
        last_idx = new_grid[nr][nc][1]

        nw = ow + w
        
        new_grid[nr][nc][1] = j
        new_grid[nr][nc][0] = nw

        if last_idx != -1:
            bids[last_idx] = (-1, -1, None, -1)
        bids[j] = ((nr, nc, d, nw))
        # print(nr, nc, d, nw)
        # print(new_grid)
    # print(bids)

max_w = 0
left_count = 0
for r, _, _, w in bids:
    if r > -1:
        left_count+=1
    max_w = max(max_w, w)

print(left_count, max_w)
        

                


        
        

