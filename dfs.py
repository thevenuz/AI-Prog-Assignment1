"""Module for Depth First Search algorithm implementation in Python."""

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


visited_nodes = []  # a list to keep track of visited nodes


def dfs(graph: dict[str, any], visited_nodes: list, start_node: str, goal_node: str):
    """Depth First Search function that takes the whole graph, list of visited nodes, start node and goal node as input.

    Returns: list of visited nodes
    """

    # If the goal node is already in the list of visited nodes, return the list of visited nodes
    if goal_node in visited_nodes:
        return visited_nodes

    # If the start node is not in the list of visited nodes, add it to the list of visited nodes and recursively
    # call the dfs function for each neighbour of the start node
    if start_node not in visited_nodes:
        visited_nodes.append(start_node)
        for neighbour in graph[start_node]:
            dfs(graph, visited_nodes, neighbour, goal_node)

    return visited_nodes


path = dfs(graph, visited_nodes, "S", "G")
print(path)
