# Graph represented as an adjacency list (node: [(neighbor, distance)])
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    """
    Find shortest path(s) from `start` to all nodes or a specific `target`.
    """
    unvisited = list(graph)  # Nodes yet to be processed
    distances = {node: 0 if node == start else float('inf') for node in graph}  # Distance to each node
    paths = {node: [] for node in graph}  # Paths to each node
    paths[start].append(start)  # Start node path

    while unvisited:
        current = min(unvisited, key=distances.get)  # Node with smallest distance
        for node, distance in graph[current]:
            # Update distance and path if shorter path is found
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                paths[node] = paths[current][:] + [node]  # Update path
        unvisited.remove(current)  # Mark as visited

    # Print distances and paths
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node != start:  # Skip start node
            print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths  # Return for further use

# Find shortest path from 'A' to 'F'
shortest_path(my_graph, 'A', 'F')
