def brute_force_path(start, goal, graph):
    paths = [[start]]
    while paths:
        path = paths.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            paths.append(new_path)
    return None  # No path found

# Define a simple graph
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

# Test pathfinding
start = "A"
goal = "F"
path = brute_force_path(start, goal, graph)
print("Path found:", path)
