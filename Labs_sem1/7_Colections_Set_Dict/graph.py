"""
Module which creates list of the graph from txt file
Create dictionary with nodes, edges and do operations with it (add/remove nodes/edges)
Convert graph into dot format
"""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.


def get_graph_from_file(file_name):
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> type(get_graph_from_file("data1.txt"))
    <class 'list'>
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        edges_list = []
        for line in file:
            edges_list.append([int(x) for x in line.strip().split(',')])
    return edges_list


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    >>> to_edge_dict([[1, 2], [2, 3], [3, 1], [4, 2], [3, 5], [1, 5],[4, 4], [1, 3]])
    {1: [2, 3, 5], 2: [1, 3, 4], 3: [1, 2, 5], 4: [2, 4], 5: [1, 3]}
    """
    graph, result = {}, {}
    for current_edge in edge_list:
        graph[current_edge[1]] = graph.get(current_edge[1], set()) | {current_edge[0]}
        graph[current_edge[0]] = graph.get(current_edge[0], set()) | {current_edge[1]}
    for key in sorted(graph):
        result[key] = sorted(list(graph[key]))
    return result


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    >>> is_edge_in_graph({1: [5], 2: [3, 4], 3: [2, 4], 4: [2, 3], 5: [1]}, (3, 2))
    True
    """
    if edge[0] in graph.keys():
        if edge[1] in graph[edge[0]]:
            return True
    return False


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    >>> add_edge({1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if not is_edge_in_graph(graph, edge):
        add_node(graph, edge[0])
        add_node(graph, edge[1])
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    if is_edge_in_graph(graph, edge):
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    >>> add_node({1: [2], 2: [1]}, 1)
    {1: [2], 2: [1]}
    """
    if node not in graph.keys():
        graph[node] = []
    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 6)
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    if node in graph.keys():
        incident_nodes = graph[node]
        for cur_node in incident_nodes:
            graph[cur_node].remove(node)
        graph.pop(node, 0)
    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    with open('graph.dot', 'w', encoding='utf-8') as file:
        file.write('graph{\n')
        for key, vertixes in graph.items():
            for vertix in vertixes:
                file.write(f'      {key}--{vertix}\n')
        file.write('}\n')

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
