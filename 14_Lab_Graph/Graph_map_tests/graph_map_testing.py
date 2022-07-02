"""
Lab 14 Test map graph
"""
import unittest
from dfs import DFS
from bfs import BFS
from topological_sort import topological_sort
from graph import Graph

def read_file(path, directed=False):
    """
    Read file. Create and return graph wirh file edges
    """
    graph = Graph(directed)
    edges = []
    with open(path, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            # remove useless symbols, split data
            for delete_symb in '(),':
                line = line.replace(delete_symb, "")
            line = line.split()
            # add line vertix to the graph
            graph.insert_vertex(line[0])
            for node in line[1:]:
                edges.append((line[0], node))
    # add edges to the graph if they exsists
    for (vert, node) in edges:
        if node != 'none':
            graph.insert_edge(get_vertex(graph, vert), get_vertex(graph, node))
    return graph

def get_vertex(graph:Graph, element):
    """ Helper function. Return graph vertix by its name """
    for vertex in graph.vertices():
        if vertex.element() == element:
            return vertex


PATH = 'stanford_cs.txt'
class TestGraph(unittest.TestCase):
    """
    Class to test file reading and graph
    functions: bfs, dfs, topological sort
    """

    def test_read(self):
        """
        Test read_file function
        """
        # undirected graph
        graph1 = read_file(PATH)
        self.assertFalse(graph1.is_directed())
        self.assertEqual(graph1.edge_count(), 22)
        self.assertEqual(graph1.vertex_count(), 24)
        # directed graph
        graph2 = read_file(PATH, directed=True)
        self.assertTrue(graph2.is_directed())
        self.assertEqual(graph2.edge_count(), 22)
        self.assertEqual(graph2.vertex_count(), 24)
        self.assertEqual([node.element() for node in graph2.vertices()],
                 ['MATH19', 'MATH20',  'MATH21', 'MATH51', 'CS108', 'PHYS21',
                  'PHYS23', 'CS106A', 'CS106B', 'CS194W', 'CS221', 'CS155',
                  'CS145', 'CS161', 'CS154', 'CS140', 'CS144', 'CS109', 'CS103',
                  'CS110','CS107', 'ENGR40M', 'MATH52', 'MATH53'])


    def test_bfs(self):
        """
        Test BFS function
        """
        graph1 = read_file(PATH)
        vx1 = get_vertex(graph1,'ENGR40M')
        visited1 = {vx1:None}
        BFS(graph1, vx1, visited1)

        self.assertEqual(len(visited1), 3)
        self.assertIn(get_vertex(graph1, 'PHYS23'),visited1)
        self.assertNotIn(get_vertex(graph1, 'CS194W'),visited1)
        self.assertEqual(list(node.element() for node in visited1),
                        ['ENGR40M', 'PHYS23', 'PHYS21'])


        graph2 = read_file(PATH, True)
        vx2 = get_vertex(graph2, 'MATH53')
        visited2 = {vx2:None}
        BFS(graph2, vx2, visited2)

        self.assertEqual(len(visited2), 5)
        self.assertIn(get_vertex(graph2, 'MATH53'),visited2)
        self.assertNotIn(get_vertex(graph2, 'CS194W'),visited2)
        self.assertEqual(list(node.element() for node in visited2),
                    ['MATH53', 'MATH51', 'MATH21', 'MATH20', 'MATH19'])


    def test_dfs(self):
        """
        Test DFS function
        """
        graph1 = read_file(PATH)
        vx1 = get_vertex(graph1,'CS221')
        visited1 = {vx1:None}
        DFS(graph1, vx1, visited1)

        self.assertEqual(len(visited1), 15)
        self.assertIn(get_vertex(graph1, 'CS145'),visited1)
        self.assertNotIn(get_vertex(graph1, 'MATH53'),visited1)
        self.assertEqual(set(node.element() for node in visited1),
                        {'CS140', 'CS110', 'CS194W', 'CS103', 'CS221',
                         'CS155', 'CS109', 'CS154', 'CS106A', 'CS107',
                         'CS108', 'CS161', 'CS106B', 'CS145', 'CS144'})

        graph2 = read_file(PATH, True)
        vx2 = get_vertex(graph2,'PHYS23')
        visited2 = {vx2:None}
        DFS(graph2, vx2, visited2)

        self.assertEqual(len(visited2), 2)
        self.assertIn(get_vertex(graph2, 'PHYS23'),visited2)
        self.assertNotIn(get_vertex(graph2, 'CS106A'),visited2)
        self.assertEqual(list(node.element() for node in visited2),
                        ['PHYS23', 'PHYS21'])


    def test_topological_sort(self):
        """
        Test Topological sort function (for inderecte graph)
        """
        graph = read_file(PATH, True)
        top_sorted = [node.element() for node in topological_sort(graph)]
        self.assertEqual(len(top_sorted), graph.vertex_count())
        self.assertEqual(top_sorted, ['MATH53', 'MATH52', 'MATH51',
                    'MATH21', 'MATH20', 'MATH19', 'ENGR40M', 'PHYS23',
                    'PHYS21', 'CS144', 'CS140', 'CS154', 'CS145', 'CS155',
                    'CS110', 'CS107', 'CS221', 'CS194W', 'CS108', 'CS161',
                    'CS109', 'CS103', 'CS106B', 'CS106A'])

if  __name__ == '__main__':
    unittest.main()
