from collections import deque

if __name__=='__main__':
    n, l, r = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))


    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    while True:
        nothing = True
        visited = [[False]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue

                visited[i][j] = True
                q = deque()
                q.append((i, j))
                union = [(i, j)]
                total_union = a[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        mx = x + dx[k]
                        my = y + dy[k]
                        if mx < 0 or my < 0 or mx >= n or my >= n:
                            continue
                        if l <= abs(a[x][y]-a[mx][my]) <= r and not visited[mx][my]:
                            union.append((mx, my))
                            visited[mx][my] = True
                            total_union += a[mx][my]
                            q.append((mx, my))
                            nothing = False

                for u in union:
                    x, y = u
                    a[x][y] = total_union//len(union)
        if nothing:
            break
        cnt += 1
    print(cnt)
