import unittest

from src import graphs, explorers, data


class BfsExplorerTests(unittest.TestCase):
    def setUp(self):
        self.test_proper_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]

    def test_find_path_matrix(self):
        """
        Tests if BfsExplorer can find path if on the route
        there is at least one stop
        (uses matrix representation)
        """
        test_graph = graphs.MatrixDefinedGraph(self.test_proper_matrix)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 2, 1])

    def test_should_not_find_path(self):
        """
        Tests if BfsExplorer can't find path
        if there are no connections to destination city
        """
        test_matrix = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
        test_graph = graphs.MatrixDefinedGraph(test_matrix)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [])

    def test_find_path_cities(self):
        """
        Same as test_find_path_matrix, uses
        city names instead of node ids
        """
        test_graph = graphs.MatrixDefinedGraph(self.test_proper_matrix)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path_cities(data.cities[0], data.cities[1])
        self.assertSequenceEqual(path, [0, 2, 1])


if __name__ == '__main__':
    unittest.main()
