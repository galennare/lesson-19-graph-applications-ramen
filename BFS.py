import networkx as nx

members = ["Rob", "Matthew", "Tom", "Kyle", "Jared", "Alex", "Giovanni", "Tyler", "Brett", 
           "Bart", "Amber", "Alisson", "Paige", "Nicole", "Kelsey", "Ashley", "Anna", "Shannon", "Jamie", "Emma"]
boys = ["Rob", "Matthew", "Tom", "Kyle", "Jared", "Alex", "Giovanni", "Tyler", "Brett", "Bart"]
girls = ["Amber", "Alisson", "Paige", "Nicole", "Kelsey", "Ashley", "Anna", "Shannon", "Jamie", "Emma"]

def is_bipartite(graph: nx.Graph, start: any) -> bool:
    queue = []
    queue.append(start)
    visited = []

    while queue:
        u = queue.pop()
        # Return false is there is a self loop
        if (graph.has_edge(u,u)):
            return False
        
        for v in range(len(graph.nodes)):
            if graph.has_edge(u,members[v]) and members[v] not in visited:
                if u in boys and members[v] in girls:
                    visited.append(members[v])
                    queue.append(members[v])
                elif u in girls and members[v] in boys:
                    visited.append(members[v])
                    queue.append(members[v])
                elif u in boys and members[v] in boys:
                    return False
                elif u in girls and members[v] in girls:
                    return False
    return True
