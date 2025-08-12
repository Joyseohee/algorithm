from collections import deque

n, m, t, k = map(int, input().split())
bids = [() for _ in range(m)]


for i in range(m):
    r, c, d, v = tuple(input().split())
    r, c, v, = int(r), int(c), int(v)
    bids[i] = (r, c, d, v)

directions = {
    "U" : 0,
    "R" : 1,
    "D" : 2,
    "L" : 3
}

change_directions = {
    "U" : "D",
    "D" : "U",
    "R" : "L",
    "L" : "R"
}

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 1 <= x < n + 1 and 1 <= y < n + 1

def conflict():
    count = len(bids)
    # removal = []

    for i in range(count-1):
        if bids[i][0] == None:
            continue

        duplicated_bid = []
        duplicated_bid.append((i, bids[i][3]))
        for j in range(i + 1, count):
            if bids[i][0] == bids[j][0] and bids[i][1] == bids[j][1]:
                duplicated_bid.append((j, bids[j][3]))
        
        if len(duplicated_bid) > k:
            duplicated_bid.sort(key = lambda x: (-x[1], -x[0]))
            # 빠른 구슬 먼저 내보내기 # 만약 같다면 구슬 번호가 클수록
            for idx in range(len(duplicated_bid) - 1, k - 1, -1):
                bids[duplicated_bid[idx][0]] = (None, None, None, None)         

def move():
    for i, (r, c, d, v) in enumerate(bids):
        if r == None:
            continue
        for _ in range(v):
            dirc_num = directions[d]
            nr, nc = r + dx[dirc_num], c + dy[dirc_num]        
            
            if not in_range(nr, nc):
                d = change_directions[d]  
                dirc_num = directions[d]
                nr, nc = r + dx[dirc_num], c + dy[dirc_num]               
            
            r, c, d = nr, nc, d
            bids[i] = (r, c, d, v)        

for _ in range(t):
    move()
    conflict()


count = 0
for i in range(len(bids)):
    if bids[i][0] != None:
        count += 1


print(count) 
