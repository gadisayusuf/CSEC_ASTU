t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    for i in range(n):
        for j in range(m):
            current_sum = 0
            x, y = i, j
            while x >= 0 and y >= 0:
                current_sum += grid[x][y]
                x -= 1
                y -= 1
            x, y = i + 1, j + 1
            while x < n and y < m:
                current_sum += grid[x][y]
                x += 1
                y += 1
            x, y = i, j
            while x >= 0 and y < m:
                current_sum += grid[x][y]
                x -= 1
                y += 1
            x, y = i + 1, j - 1
            while x < n and y >= 0:
                current_sum += grid[x][y]
                x += 1
                y -= 1
            current_sum -= grid[i][j]
            max_sum = max(max_sum, current_sum)
    print(max_sum)