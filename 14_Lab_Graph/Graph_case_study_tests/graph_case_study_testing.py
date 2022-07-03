"""
Lab 14 Test study graph
"""
import unittest
from graph import LinkedDirectedGraph
from algorithms import topological_sort, dfs, bfs
from linkedstack import LinkedStack


def read_file(path):
    """
    Read file. Create and return graph wirh file edges
    """
    graph = LinkedDirectedGraph()
    edges_dict  = {}
    with open(path, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            # remove useless symbols, split data
            for delete_symb in '(),':
                line = line.replace(delete_symb, "")
            line = line.split()
            # add line vertix to the graph
            graph.addVertex(line[0])
            edges_dict[line[0]] = line[1:]
    # add edges to the graph if they exsist
    for (vert, neighbours) in edges_dict.items():
        for node in neighbours:
            if node != 'none':
                graph.addEdge(vert, node, 0)
    return graph


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
        graph = read_file(PATH)
        self.assertEqual(graph.sizeEdges(), 22)
        self.assertEqual(graph.sizeVertices(), 24)
        vertices_labels = [node.getLabel() for node in graph.vertices()]
        self.assertEqual(vertices_labels, ['MATH19', 'MATH20',  'MATH21', 'MATH51',
                 'CS108', 'PHYS21', 'PHYS23', 'CS106A', 'CS106B', 'CS194W', 'CS221',
                 'CS155', 'CS145', 'CS161', 'CS154', 'CS140', 'CS144', 'CS109',
                 'CS103', 'CS110','CS107', 'ENGR40M', 'MATH52', 'MATH53'])


    def test_bfs(self):
        """
        Test BFS function
        """
        graph1 = read_file(PATH)
        vx1 = 'ENGR40M'
        result1= bfs(graph1, vx1)

        self.assertEqual(len(result1), 3)
        self.assertIn('PHYS23',result1)
        self.assertNotIn('CS194W',result1)
        self.assertEqual(result1, ['ENGR40M', 'PHYS23', 'PHYS21'])


        graph2 = read_file(PATH)
        vx2 = 'MATH53'
        result2 = bfs(graph2, vx2)

        self.assertEqual(len(result2), 5)
        self.assertIn('MATH53',result2)
        self.assertNotIn('CS194W',result2)
        self.assertEqual(result2, ['MATH53', 'MATH51', 'MATH21', 'MATH20', 'MATH19'])


    def test_dfs(self):
        """
        Test DFS function
        """
        graph1 = read_file(PATH)
        vx1 = graph1.getVertex('CS221')
        visited1 = LinkedStack()
        dfs(graph1, vx1, visited1)

        self.assertEqual(len(visited1), 5)
        self.assertIn(graph1.getVertex('CS221'),visited1)
        self.assertNotIn(graph1.getVertex('MATH53'), visited1)
        self.assertEqual([vx.getLabel() for vx in visited1],
                        ['CS106A', 'CS106B', 'CS103', 'CS109', 'CS221'])

        graph2 = read_file(PATH)
        vx2 = graph2.getVertex('PHYS23')
        visited2 = LinkedStack()
        dfs(graph2, vx2, visited2)

        self.assertEqual(len(visited2), 2)
        self.assertIn(graph2.getVertex('PHYS23'),visited2)
        self.assertNotIn(graph2.getVertex('CS106A'),visited2)
        self.assertEqual([vx.getLabel() for vx in visited2],
                        ['PHYS21', 'PHYS23'])


    def test_topological_sort(self):
        """
        Test Topological sort function
        """
        graph = read_file(PATH)
        # get node labels from the stack from tail to the head
        top_sorted = [node.getLabel() for node in topological_sort(graph)][::-1]

        self.assertEqual(len(top_sorted), graph.sizeVertices())
        self.assertEqual(top_sorted, ['MATH53', 'MATH52', 'ENGR40M', 'CS144',
                    'CS140', 'CS154', 'CS145', 'CS155', 'CS110', 'CS107', 'CS221',
                    'CS194W', 'PHYS23', 'PHYS21', 'CS108', 'CS161', 'CS109', 'CS103',
                    'CS106B', 'CS106A', 'MATH51', 'MATH21', 'MATH20', 'MATH19'])


if  __name__ == '__main__':
    unittest.main()
