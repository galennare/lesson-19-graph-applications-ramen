import networkx as nx

def dfs(graph: nx.Graph, start_node: any) -> list:
    """
        Depth-First Search (DFS) algorithm implementation.
        Args:
        - graph: A networkx Graph object representing the graph to be traversed.
        - start_node: The starting node for the DFS traversal.

        Returns:
        - visited: A list of nodes visited during the DFS traversal.
    """
    visited = []
    stack = [start_node]  # Use a stack to keep track of nodes to visit

    while stack:
        current_node = stack.pop()  # Pop the last node from the stack
        if current_node not in visited:
            visited.append(current_node)  # Mark the current node as visited
            neighbors = list(graph.neighbors(current_node))
            stack.extend(neighbors)  # Add neighbors of current node to the stack

    return visited