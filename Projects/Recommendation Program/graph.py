class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

    def get_edge_weight(self, vertex):
        return self.edges[vertex]


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)


def print_graph(graph: Graph) -> None:
    """Prints out a graph."""

    for vertex in graph.graph_dict:
        print('')
        print(f'{vertex} is connected to')
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print('No edges!')
        for adjacent_vertex in vertex_neighbors:
            edge_weight = graph.graph_dict[vertex].get_edge_weight(adjacent_vertex)
            print(f'=> {adjacent_vertex}, edge weight is: {edge_weight}')


# Unused in the current version, these functions can perform a BFS on the graph and find the shortest
# path from one movie to another

# def bfs(graph: dict, start_vertex: str, target_value: str) -> list | None:
#     """Breadth-First Search."""
#     path = [start_vertex]
#     vertex_and_path = [start_vertex, path]
#     bfs_queue = [vertex_and_path]
#     visited = set()
#
#     while bfs_queue:
#         current_vertex, path = bfs_queue.pop(0)
#         visited.add(current_vertex)
#
#         for neighbor in graph[current_vertex]:
#             if neighbor not in visited:
#                 if neighbor == target_value:
#                     path.append(neighbor)
#                     return path
#                 else:
#                     bfs_queue.append([neighbor, path + [neighbor]])
#
#
# def get_formatted_graph(graph: Graph) -> dict:
#     """Returns graph formatted as dictionary suitable for BFS."""
#     graph_dictionary = {}
#
#     for vertex in graph.graph_dict:
#         graph_dictionary[vertex] = {neighbor for neighbor in graph.graph_dict[vertex].edges}
#
#     return graph_dictionary
