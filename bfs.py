"""Module for Breadth First Search algorithm implementation in Python."""

# representation of the graph using dictionary
graph = {
    "S": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["H"],
    "E": ["G", "I"],
    "F": ["J"],
    "H": [],
    "G": [],
    "I": [],
    "J": [],
}


visited_nodes: list = []  # a list to keep track of visited nodes
queue: list = []  # a list to keep track of adjacent nodes that need to be visited next


def bfs(graph: dict[str, any], visited_nodes: list, start_node: str, goal_node: str):
    """Breadth First Search function that takes the whole graph, list of visited nodes, start node and goal node as input.

    Returns: list of visited nodes
    """

    # Add the current node to the list of visited nodes and the queue
    visited_nodes.append(start_node)
    queue.append(start_node)

    # If the goal node is already in the list of visited nodes, return the list of visited nodes
    if goal_node in visited_nodes:
        return visited_nodes

    while queue:
        # Take the first node from the queue and check it's neighnours and add them to the queue and visited_nodes list
        current_node = queue.pop(0)

        for neighbour in graph[current_node]:
            if neighbour not in visited_nodes:
                visited_nodes.append(neighbour)
                queue.append(neighbour)

                # If the immediate neighbour is the goal node meaning we've reached the goal node, return the list of visited nodes
                if neighbour == goal_node:
                    return visited_nodes

    return visited_nodes


path = bfs(graph, visited_nodes, "S", "G")
print(path)
