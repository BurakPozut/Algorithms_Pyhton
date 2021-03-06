def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:   # Neighbor means values in the []. Ex A:[b,c] b and c is the neighbor
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []
}
visited = []
queue = []

bfs(visited, graph, 'A')
