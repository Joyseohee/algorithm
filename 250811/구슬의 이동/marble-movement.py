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
    removal = deque()

    for i in range(count-1):
        duplicated_bid = deque()
        duplicated_bid.append(i)
        for j in range(i + 1, count):
            if bids[i][0] == bids[j][0] and bids[i][1] == bids[j][1]:
                duplicated_bid.append(j)
        
        while len(duplicated_bid) > k:
            removal.append(duplicated_bid.pop())

    while removal:
        del bids[removal.pop()]

def move():
    for i, (r, c, d, v) in enumerate(bids):
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
    

print(len(bids))



# 0 0 0 D1 
# R3 0 0 0 
# 0 0 0 U1 
# 0 0 0 0 

# 0 0 0 0
# 0 0 0 D1, U1
# 0 0 0 0  
# 0 0 0 0 