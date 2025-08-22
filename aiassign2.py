import heapq
import math

directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def heuristic(x, y, goal):
    return math.sqrt((goal[0]-x)**2 + (goal[1]-y)**2)


def best_first_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    goal = (n-1, n-1)
    visited = set()
    pq = [(heuristic(0, 0, goal), (0, 0), [(0, 0)])]  

    while pq:
        _, (x, y), path = heapq.heappop(pq)
        if (x, y) == goal:
            return len(path), path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                heapq.heappush(pq, (heuristic(nx, ny, goal), (nx, ny), path+[(nx, ny)]))

    return -1, []



def a_star_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    goal = (n-1, n-1)
    pq = [(heuristic(0, 0, goal), 0, (0, 0), [(0, 0)])]  # (f = g+h, g, node, path)
    visited = {}

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)
        if (x, y) == goal:
            return len(path), path
        if (x, y) in visited and visited[(x, y)] <= g:
            continue
        visited[(x, y)] = g

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                new_g = g+1
                heapq.heappush(pq, (new_g + heuristic(nx, ny, goal), new_g, (nx, ny), path+[(nx, ny)]))

    return -1, []



grids = [
    [[0, 1], [1, 0]],
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
]

for i, grid in enumerate(grids, 1):
    bf_len, bf_path = best_first_search(grid)
    a_len, a_path = a_star_search(grid)
    print(f"Example {i}:")
    print(f"Best First Search  →  Path length: {bf_len}, Path: {bf_path}")
    print(f"A* Search          →  Path length: {a_len}, Path: {a_path}\n")
