import unittest
from src import *


class MatrixDefinedGraphTests(unittest.TestCase):
    def test_incidence_matrix_generation(self):
        self.test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        incidence_matrix = graph.get_incidental_matrix()
        self.assertSequenceEqual(incidence_matrix[0], [1, 0])
        self.assertSequenceEqual(incidence_matrix[1], [0, 1])
        self.assertSequenceEqual(incidence_matrix[2], [1, 1])

    def test_get_node_list_should_return_valid_nodes(self):
        self.test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        self.assertSequenceEqual(graph.get_node_list(), [0, 1, 2])

    def test_get_incidental_edges_returns_proper_list(self):
        self.test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        edges_0 = graph.get_incidental_edges(0)
        edges_1 = graph.get_incidental_edges(1)
        edges_2 = graph.get_incidental_edges(2)
        self.assertSequenceEqual(edges_0, [0])
        self.assertSequenceEqual(edges_1, [1])
        self.assertSequenceEqual(edges_2, [0, 1])

    def test_get_nodes_connected_by_edge_returns_proper_sequence(self):
        self.test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        nodes_0 = graph.get_nodes_connected_by_edge(0)
        nodes_1 = graph.get_nodes_connected_by_edge(1)
        self.assertSequenceEqual(nodes_0, [0, 2])
        self.assertSequenceEqual(nodes_1, [1, 2])

    def test_get_neighbour_nodes_returns_proper_nodes(self):
        self.test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        neighbours_0 = graph.get_neighbour_nodes(0)
        neighbours_1 = graph.get_neighbour_nodes(1)
        neighbours_2 = graph.get_neighbour_nodes(2)
        self.assertSequenceEqual(neighbours_0, [2])
        self.assertSequenceEqual(neighbours_1, [2])
        self.assertSequenceEqual(neighbours_2, [0, 1])


if __name__ == '__main__':
    unittest.main()
