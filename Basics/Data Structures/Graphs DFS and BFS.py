# Breadth-First Search
def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor == target_value:
                    path.append(neighbor)
                    return path
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])


# Depth-First Search
def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
    visited.append(current_vertex)
    if current_vertex is target_value:
        return visited

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path


the_most_dangerous_graph = {
    'lava': {'sharks', 'piranhas'},
    'sharks': {'lava', 'bees', 'lasers'},
    'piranhas': {'lava', 'crocodiles'},
    'bees': {'sharks'},
    'lasers': {'sharks', 'crocodiles'},
    'crocodiles': {'piranhas', 'lasers'}
}

print(bfs(the_most_dangerous_graph, 'crocodiles', 'sharks'))
print(dfs(the_most_dangerous_graph, 'crocodiles', 'sharks'))
