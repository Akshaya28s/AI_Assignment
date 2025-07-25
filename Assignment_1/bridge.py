from collections import deque

people = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

initial_state = (frozenset(people.keys()), frozenset(), 0, "left")  

def bfs():
    queue = deque()
    visited = set()

    queue.append((initial_state, []))  
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()
        left, right, time_elapsed, umbrella_side = state

        if len(right) == 4 and time_elapsed <= 60:
            return path + [state]  

        if umbrella_side == "left":
    
            for p1 in left:
                for p2 in left:
                    if p1 < p2:  
                        new_left = set(left) - {p1, p2}
                        new_right = set(right) | {p1, p2}
                        cross_time = max(people[p1], people[p2])
                        new_time = time_elapsed + cross_time
                        new_state = (frozenset(new_left), frozenset(new_right), new_time, "right")

                        if new_time <= 60 and new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, path + [state]))

        else:
            
            for p in right:
                new_left = set(left) | {p}
                new_right = set(right) - {p}
                return_time = people[p]
                new_time = time_elapsed + return_time
                new_state = (frozenset(new_left), frozenset(new_right), new_time, "left")

                if new_time <= 60 and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))

    return None  


result = bfs()

if result:
    print("Solution found in the following steps:\n")
    for idx, step in enumerate(result):
        left, right, time_elapsed, umbrella = step
        print(f"Step {idx}:")
        print(f" Left side: {sorted(left)}")
        print(f" Right side: {sorted(right)}")
        print(f" Time elapsed: {time_elapsed} min")
        print(f" Umbrella is on the {umbrella} side\n")
else:
    print("No solution found within 60 minutes.")
