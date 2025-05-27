from collections import deque

n, m, k = map(int, input().split())
apple_set = { (r-1, c-1) for r,c in (map(int,input().split()) for _ in range(m)) }
moves = [tuple(input().split()) for _ in range(k)]

# 뱀 초기화
snake = deque([(0,0)])
body = set([(0,0)])
t = 0

dirs = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

for d,p_str in moves:
    dx,dy = dirs[d]
    p = int(p_str)
    for _ in range(p):
        t += 1
        hx, hy = snake[0]
        nx, ny = hx + dx, hy + dy
        
        # 1) 벽 충돌
        if not (0 <= nx < n and 0 <= ny < n):
            print(t); exit()
        # 2) 자기 몸 충돌
        if (nx,ny) in body:
            print(t); exit()
        
        # 3) 사과 있으면 꼬리 유지, 없으면 꼬리 제거
        if (nx,ny) in apple_set:
            apple_set.remove((nx,ny))
        else:
            tx, ty = snake.pop()
            body.remove((tx,ty))
        
        # 4) 머리 추가
        snake.appendleft((nx,ny))
        body.add((nx,ny))

print(t)
