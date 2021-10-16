from itertools import combinations
from collections import deque


def find_idx(n, lab):
    idx = []
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == n:
                idx.append((i,j))
    return idx

def find_nearest_zero(lab, virus_idx):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n, m = len(lab), len(lab[0])
    nearest = []
    for idx in virus_idx:
        x, y = idx
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lab[nx][ny] == 0:
                nearest.append((nx, ny))

    nearest = list(set(list(nearest)))
    return nearest

def bfs(lab, s):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n = len(lab)
    m = len(lab[0])
    visited = [[False]*m for _ in range(n)]
    sx, sy = s
    q = deque()
    q.append((sx, sy))

    cnt = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lab[nx][ny] == 0 and not visited[nx][ny]:
                lab[nx][ny] = 2
                visited[nx][ny] = True
                q.append((nx, ny))

    return lab

def change_lab(combi, lab):
    for com in combi:
        x, y = com
        lab[x][y] = 1

    return lab

if __name__ == '__main__':
    n, m = map(int, input().split())
    lab = []
    for i in range(n):
        lab.append(list(map(int, input().split())))

    virus_idx = find_idx(2, lab)
    nearest_zero = find_idx(0, lab)
    combi_nearest = list(combinations(nearest_zero, 3))
    max_cnt = -1
    for combi in combi_nearest:
        import copy
        chg_lab = copy.deepcopy(lab)
        chg_lab = change_lab(list(combi), chg_lab)
        temp = 0
        for virus in virus_idx:
            chg_lab = bfs(chg_lab, virus)

        temp = sum(i.count(0) for i in chg_lab)

        if max_cnt < temp:
            max_cnt = temp

    print(max_cnt)


