import unittest
from src import *


class MatrixDefinedGraphTests(unittest.TestCase):
    def setUp(self):
        self.test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]

    def test_incidence_matrix_generation(self):
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        incidence_matrix = graph.get_incidental_matrix()
        self.assertSequenceEqual(incidence_matrix[0], [1, 0])
        self.assertSequenceEqual(incidence_matrix[1], [0, 1])
        self.assertSequenceEqual(incidence_matrix[2], [1, 1])

    def test_get_node_list_should_return_valid_nodes(self):
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        self.assertSequenceEqual(graph.get_node_list(), [0, 1, 2])

    def test_get_incidental_edges_returns_proper_list(self):
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        edges_0 = graph.get_incidental_edges(0)
        edges_1 = graph.get_incidental_edges(1)
        edges_2 = graph.get_incidental_edges(2)
        self.assertSequenceEqual(edges_0, [0])
        self.assertSequenceEqual(edges_1, [1])
        self.assertSequenceEqual(edges_2, [0, 1])

    def test_get_nodes_connected_by_edge_returns_proper_sequence(self):
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        nodes_0 = graph.get_nodes_connected_by_edge(0)
        nodes_1 = graph.get_nodes_connected_by_edge(1)
        self.assertSequenceEqual(nodes_0, [0, 2])
        self.assertSequenceEqual(nodes_1, [1, 2])

    def test_get_neighbour_nodes_returns_proper_nodes(self):
        graph = graphs.MatrixDefinedGraph(self.test_matrix)
        neighbours_0 = graph.get_neighbour_nodes(0)
        neighbours_1 = graph.get_neighbour_nodes(1)
        neighbours_2 = graph.get_neighbour_nodes(2)
        self.assertSequenceEqual(neighbours_0, [2])
        self.assertSequenceEqual(neighbours_1, [2])
        self.assertSequenceEqual(neighbours_2, [0, 1])


class ListDefinedGraphTests(unittest.TestCase):
    def setUp(self):
        self.test_list = [[2], [2], [0, 1]]

    def test_get_node_list_should_return_valid_nodes(self):
        graph = graphs.ListDefinedGraph(self.test_list)
        self.assertSequenceEqual(graph.get_node_list(), [0, 1, 2])

    def test_get_incidental_edges_returns_proper_list(self):
        graph = graphs.ListDefinedGraph(self.test_list)
        edges_0 = graph.get_incidental_edges(0)
        edges_1 = graph.get_incidental_edges(1)
        edges_2 = graph.get_incidental_edges(2)
        self.assertSequenceEqual(edges_0, [0])
        self.assertSequenceEqual(edges_1, [1])
        self.assertSequenceEqual(edges_2, [0, 1])

    def test_get_nodes_connected_by_edge_returns_proper_sequence(self):
        graph = graphs.ListDefinedGraph(self.test_list)
        nodes_0 = graph.get_nodes_connected_by_edge(0)
        nodes_1 = graph.get_nodes_connected_by_edge(1)
        self.assertSequenceEqual(nodes_0, [0, 2])
        self.assertSequenceEqual(nodes_1, [1, 2])

    def test_get_neighbour_nodes_returns_proper_nodes(self):
        graph = graphs.ListDefinedGraph(self.test_list)
        neighbours_0 = graph.get_neighbour_nodes(0)
        neighbours_1 = graph.get_neighbour_nodes(1)
        neighbours_2 = graph.get_neighbour_nodes(2)
        self.assertSequenceEqual(neighbours_0, [2])
        self.assertSequenceEqual(neighbours_1, [2])
        self.assertSequenceEqual(neighbours_2, [0, 1])


class BfsExplorerTests(unittest.TestCase):
    def test_find_path(self):
        test_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        test_graph = graphs.MatrixDefinedGraph(test_matrix)
        explorer = graphs.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 2, 1])

    def test_cant_find_path(self):
        test_matrix = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
        test_graph = graphs.MatrixDefinedGraph(test_matrix)
        explorer = graphs.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [])


def run_some_tests():
    # Run only the tests in the specified classes
    test_classes_to_run = [MatrixDefinedGraphTests, ListDefinedGraphTests, BfsExplorerTests]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    return runner.run(big_suite)


if __name__ == '__main__':
    results = run_some_tests()
