import sys
input = sys.stdin.readline

N = int(input().strip())
segments = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0
chosen = []  # 현재까지 선택한 선분들 (li, ri) 리스트


def is_overlap(a, b):
    aL, aR = a
    bL, bR = b
    # 끝점 공유도 겹침이므로, 완전히 떨어진 경우만 비겹침
    return not (aR < bL or bR < aL)


def dfs(idx):
    global answer

    # 남은 걸 전부 골라도 최댓값을 못 넘으면 가지치기
    if len(chosen) + (N - idx) <= answer:
        return

    # 모든 선분을 다 봤으면 갱신
    if idx == N:
        answer = max(answer, len(chosen))
        return

    # 1) idx번째 선분을 선택하지 않는 경우
    dfs(idx + 1)

    # 2) idx번째 선분을 선택하는 경우 (이미 고른 것들과 안 겹치면)
    seg = segments[idx]
    for c in chosen:
        if is_overlap(seg, c):
            break
    else:
        chosen.append(seg)
        dfs(idx + 1)
        chosen.pop()


dfs(0)
print(answer)
