"""
Lab 14 - Graph Study Algorithms
"""

from linkedstack import LinkedStack
from linkedqueue import LinkedQueue

def topological_sort(graph, startLabel = None):
    """
    Return stack with topoligicaly sorted graph vertixes
    """
    stack = LinkedStack()
    graph.clearVertexMarks()
    for v in graph.vertices():
        if not v.isMarked():
            dfs(graph, v, stack)
    return stack

def dfs(graph, vertex, stack):
    """
    Visit nodes by dfs. Add nodes to the stack
    """
    vertex.setMark()
    for w in graph.neighboringVertices(vertex.getLabel()):
        if not w.isMarked():
            dfs(graph, w, stack)
    stack.push(vertex)

def bfs(graph, first_node):
    """
    Return list with the vertices visited by bfs
    """
    graph.clearVertexMarks()
    # set initail values
    result = []
    vertix_queue = LinkedQueue()
    vertix_queue.add(graph.getVertex(first_node))
    # iterate while there are nodes in a queue
    while not vertix_queue.isEmpty():
        current_vx = vertix_queue.pop()
        # check if note was visited
        if not current_vx.isMarked():
            current_vx.setMark()
            vx_label = current_vx.getLabel()
            result.append(vx_label)
            # add neighbours to the queue
            for node in graph.neighboringVertices(vx_label):
                if not node.isMarked():
                    vertix_queue.add(node)
    return result
