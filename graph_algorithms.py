import heapq


def bfs(graph, start_node, search_node=None):
    # graph: a dictionary representing the graph to be traversed.
    # start_node: a string representing the starting node of the traversal.
    # search_node: an optional string representing the node being searched for in the graph.
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
    # particular component can only be traversed. But the nodes belonging to other components must not be traversed
    # if those nodes were not reachable from the given start_node.

    # The output depends on whether the search_node is provided or not:
    # 1. If search_node is provided, the function returns 1 if the node is found during the search and 0 otherwise.
    # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    # Useful code snippets (not necessary but you can use if required)
    visited_nodes = set()
    bfs_queue = [start_node]
    path_traversed = []

    while bfs_queue:
        curr_node = bfs_queue.pop(0)
        if curr_node not in visited_nodes:
            visited_nodes.add(curr_node)
            path_traversed.append(curr_node)
            if search_node and curr_node == search_node:
                return 1  # search node found
            bfs_queue.extend([n for n in graph[curr_node] if n not in visited_nodes])

    if search_node is not None:
        return 0  # search node not found

    return path_traversed


def dfs(graph, start_node, visited=None, path=None, search_node=None):
    # graph: a dictionary representing the graph
    # start_node: the starting node for the search
    # visited: a set of visited nodes (optional, default is None)
    # path: a list of nodes in the current path (optional, default is None)
    # search_node: the node to search for (optional, default is None)
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
    # particular component can only be traversed. But the nodes belonging to other components must not be traversed
    # if those nodes were not reachable from the given start_node.

    # The function returns:
    # 1. If search_node is provided, the function returns 1 if the node is found and 0 if it is not found.
    # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    # Useful code snippets (not necessary but you can use if required)
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start_node)
    path.append(start_node)

    if start_node == search_node:
        return 1  # search node found

    for ngbh_node in graph[start_node]:
        if ngbh_node not in visited:
            result = dfs(graph, ngbh_node, visited, path, search_node)
            if result == 1:
                return result

    if search_node is not None:
        return 0  # search node not found

    return path  # search node not provided, return entire path [list of nconst id's of nodes visited]


def dijkstra(graph, start_node, end_node):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
    # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
    # 1. If the end_node is not reachable from the start_node, the function returns 0.

    # 2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
    # 2.1 The first element is a list representing the shortest path from start_node to end_node.
    # [list of nconst values in the visited order]
    # 2.2 The second element is the total distance of the shortest path.
    # (summation of the distances or edge weights between minimum visited nodes)
    # 2.3 The third element is Hop Count between start_node and end_node.

    # Return the shortest path and distances
    dist_array = {node: float("inf") for node in graph}
    dist_array[start_node] = 0
    prev_nodes = {node: None for node in graph}
    heap = [(0, start_node)]
    visited_nodes = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        visited_nodes.add(current_node)

        if current_distance > dist_array[current_node]:
            continue

        for ngbh_nodes, weight in graph[current_node].items():
            curr_distance = current_distance + weight
            if curr_distance < dist_array[ngbh_nodes]:
                dist_array[ngbh_nodes] = curr_distance
                prev_nodes[ngbh_nodes] = current_node
                heapq.heappush(heap, (curr_distance, ngbh_nodes))

    if dist_array[end_node] == float("inf"):
        return 0

    path = []
    hop_count = 0
    node = end_node
    while node != start_node:
        path.append(node)
        node = prev_nodes[node]
        hop_count += 1
    path.append(start_node)
    path.reverse()

    curr_distance = dist_array[end_node]

    # Return the shortest path and distances
    return [path, curr_distance, hop_count]


def kosaraju_dfs(graph, node, visited, stack):
    visited.add(node)
    for ngbh_node in graph[node]:
        if ngbh_node not in visited:
            kosaraju_dfs(graph, ngbh_node, visited, stack)
    stack.append(node)


# (strongly connected components)
def kosaraju(graph):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
    # are dictionaries representing the edges and their weights.
    # Note: Here you need to call dfs function multiple times so you can Implement seperate
    # kosaraju_dfs function if required.

    # The output:
    # list of strongly connected components in the graph,
    # where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    stack = []
    visited_nodes = set()
    for node in graph:
        if node not in visited_nodes:
            kosaraju_dfs(graph, node, visited_nodes, stack)

    traversed_graph = {node: {} for node in graph}
    for node in graph:
        for ngbh_node in graph[node]:
            traversed_graph[ngbh_node][node] = graph[node][ngbh_node]

    components = []
    visited_nodes = set()
    while stack:
        node = stack.pop()
        if node not in visited_nodes:
            component = []
            kosaraju_dfs(traversed_graph, node, visited_nodes, component)
            components.append(component)

    # The output:
    # list of strongly connected components in the graph,
    # where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    return components
