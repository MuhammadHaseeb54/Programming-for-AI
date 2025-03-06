
# Task 03 
# Implement waterjug problem using dfs 
def waterJug(cap1, cap2, goal):
    stack = [(0, 0)]
    visited = set([(0, 0)])
    parents = {}
    while stack:
        cur_state = stack.pop()
        jug1, jug2 = cur_state

        if jug1 == goal or jug2 == goal:
            actions = []
            while cur_state != (0, 0):
                actions.append(cur_state)
                cur_state = parents[cur_state]
            actions.append((0, 0))
            actions.reverse()
            return actions

        rules = [
            (cap1, jug2), # 1: fill jug1 
            (jug1, cap2), # 2: full jug2 
            (0, jug2),    # 3: empty jug1 
            (jug1, 0),    # 4: empty jug2
            (min(cap1, jug1 + jug2), max(0, jug1 + jug2 - cap1)), # 5: pour jug1 into jug2 until jug2 is full
            (max(0, jug1 + jug2 - cap2), min(cap2, jug1 + jug2)), # 6: pour jug2 into jug1 until jug1 is full
            (jug1 - min(jug1, cap2 - jug2), jug2 + min(jug1, cap2 - jug2)),   # 7: pour jug1 into jug2 until jug1 is empty
            (jug1 + min(jug2, cap1 - jug1), jug2 - min(jug2, cap1 - jug1))# 8: pour jug2 into jug1 until jug2 is empty            
        ]

        for state in rules:
            if state not in visited:
                stack.append(state)
                visited.add(state)
                parents[state] = cur_state
    return None

jug1_cap = 4
jug2_cap = 3
goal_quantity = 2
solution = waterJug(jug1_cap, jug2_cap, goal_quantity)
print("Water Jug Problem using DFS:")
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")