from heapq import heappop, heappush
from math import inf

graph_one = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
}


def dijkstras(graph_one, start):
    distances = {}

    for vertex in graph_one:
        distances[vertex] = inf

    distances[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph_one[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances


distances_from_d = dijkstras(graph_one, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
