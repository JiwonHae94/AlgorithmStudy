from collections import deque

# m, n = map(int, input().split(' '))
# space = [list(map(int, input().split())) for _ in range(m)]
m, n = 7, 4
space = [[0,0,0,1],[0,1,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,1,0,0],[0,0,0,1]]


def sharks(space):
    shark_lst = []
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == 0:
                shark_lst.append((i,j))
                
    return shark_lst
 
def bfs(start, space):

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    q = deque()
    sx, sy = start
    q.append((sx, sy))

    visited = [[False]*n for _ in range(m)]
    visited[sx][sy] = True
    
    cnt = [[0]*n for _ in range(m)]

    while q:
        
        x, y = q.popleft()
        for i in range(8):
            mx, my = x+dx[i], y+dy[i]
            if mx < 0 or my < 0 or mx >= m or my >= n:
                continue
            if not visited[mx][my]:
                if space[mx][my] == 1:
                    return cnt[x][y] + 1
                else:
                    cnt[mx][my] =  cnt[x][y] + 1
                    visited[mx][my] = True
                    q.append((mx, my))
                    


    
shark_lst = sharks(space)
movements_lst = []
for shark in shark_lst:
    movements_lst.append(bfs(shark, space))
print(max(movements_lst))
