from collections import deque

def is_goal(state):
    return state == ['W', 'W', 'W', '_', 'E', 'E', 'E']

def get_neighbors(state):
    neighbors = []
    idx = state.index('_')

    def swap_and_add(new_idx):
        new_state = state.copy()
        new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
        neighbors.append(new_state)

    
    if idx > 0 and state[idx - 1] == 'E':
        swap_and_add(idx - 1)
    if idx > 1 and state[idx - 2] == 'E' and state[idx - 1] in ['W', 'E']:
        swap_and_add(idx - 2)  

    if idx < len(state) - 1 and state[idx + 1] == 'W':
        swap_and_add(idx + 1)  
    if idx < len(state) - 2 and state[idx + 2] == 'W' and state[idx + 1] in ['E', 'W']:
        swap_and_add(idx + 2)  

    return neighbors

def bfs(start):
    queue = deque([(start, [start])])  
    visited = set()

    while queue:
        current, path = queue.popleft()
        current_tuple = tuple(current)
        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        if is_goal(current):
            return path

        for neighbor in get_neighbors(current):
            queue.append((neighbor, path + [neighbor]))
    return None


start_state = ['E', 'E', 'E', '_', 'W', 'W', 'W']


solution = bfs(start_state)

if solution:
    for step in solution:
        print(''.join(step))
else:
    print("No solution found.")
