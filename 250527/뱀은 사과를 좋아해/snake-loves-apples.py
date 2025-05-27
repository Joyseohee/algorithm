from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
# 사과 위치 집합
apple_set = { (r-1, c-1) for r, c in (map(int, input().split()) for _ in range(m)) }
# 명령 리스트
moves = [tuple(input().split()) for _ in range(k)]

# 뱀 몸통: deque로 (머리…꼬리)
snake = deque([(0, 0)])
# 점유 셀 집합
body = {(0, 0)}
# 방향 맵
dirs = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

t = 0
for d, p_str in moves:
    dx, dy = dirs[d]
    p = int(p_str)
    for _ in range(p):
        t += 1
        hx, hy = snake[0]
        nx, ny = hx + dx, hy + dy

        # 1) 벽 충돌
        if not (0 <= nx < n and 0 <= ny < n):
            print(t)
            sys.exit()

        # 2) 사과 여부에 따라 꼬리 미리 제거
        if (nx, ny) not in apple_set:
            tx, ty = snake.pop()         # 꼬리 꺼내고
            body.remove((tx, ty))        # 점유 해제
        # (사과가 있으면 꼬리를 그대로 두고 길이 +1)

        # 3) 자기 몸 충돌 검사
        if (nx, ny) in body:
            print(t)
            sys.exit()

        # 4) 머리 추가·사과 제거
        if (nx, ny) in apple_set:
            apple_set.remove((nx, ny))
        snake.appendleft((nx, ny))
        body.add((nx, ny))

# 모든 명령 정상 수행 시
print(t)
