import unittest

from src import graphs, explorers, data


class BfsExplorerTests(unittest.TestCase):
    def setUp(self):
        self.test_proper_matrix = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        self.test_proper_list = [[2], [2], [0, 1]]

    def test_find_path_direct_matrix(self):
        """
        Tests if BfsExplorer can find direct path
        (uses matrix representation)
        """
        test_matrix_big = [[0, 1, 1, 0, 0],
                           [1, 0, 0, 1, 0],
                           [1, 0, 0, 0, 1],
                           [0, 1, 0, 0, 1],
                           [0, 0, 1, 1, 0]]
        test_graph = graphs.MatrixDefinedGraph(test_matrix_big)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 1])

    def test_find_path_direct_list(self):
        """
        Tests if BfsExplorer can find direct path
        (uses list representation)
        """
        test_list_big = [[2, 1],
                         [3, 0],
                         [0, 4],
                         [1, 4],
                         [2, 3]]
        test_graph = graphs.ListDefinedGraph(test_list_big)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 1])

    def test_find_path_1stop_matrix(self):
        """
        Tests if BfsExplorer can find path if on the route
        there is at least one stop
        (uses matrix representation)
        """
        test_graph = graphs.MatrixDefinedGraph(self.test_proper_matrix)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 2, 1])

    def test_find_path_1stop_list(self):
        """
        Tests if BfsExplorer can find path if on the route
        there is at least one stop
        (uses list representation)
        """
        test_list = graphs.ListDefinedGraph(self.test_proper_list)
        explorer = explorers.BfsExplorer(test_list)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 2, 1])

    def test_find_path_3stops_matrix(self):
        """
        Tests if BfsExplorer can find path if on the route
        there is at least three stops
        (uses matrix representation of a graph)
        """
        test_matrix_big = [[0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0],
                           [1, 0, 0, 0, 1],
                           [0, 1, 0, 0, 1],
                           [0, 0, 1, 1, 0]]
        test_graph = graphs.MatrixDefinedGraph(test_matrix_big)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 2, 4, 3, 1])

    def test_find_path_3stops_list(self):
        """
        Tests if BfsExplorer can find path if on the route
        there is at least three stops
        (uses list representation of a graph)
        """
        test_list_big = [[2],
                         [3],
                         [0, 4],
                         [1, 4],
                         [2, 3]]
        test_graph = graphs.ListDefinedGraph(test_list_big)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [0, 2, 4, 3, 1])

    def test_should_not_find_path_matrix(self):
        """
        Tests if BfsExplorer can't find path
        if there are no connections to destination city
        """
        test_matrix_big = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 1],
                           [0, 0, 1, 1, 0]]
        test_graph = graphs.MatrixDefinedGraph(test_matrix_big)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [])

    def test_should_not_find_path_list(self):
        """
        Tests if BfsExplorer can't find path
        if there are no connections to destination city
        """
        test_list_big = [[],
                         [],
                         [4],
                         [4],
                         [2, 3]]
        test_graph = graphs.ListDefinedGraph(test_list_big)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path(0, 1)
        self.assertSequenceEqual(path, [])

    def test_find_path_cities(self):
        """
        Same as test_find_path_1stop_matrix, uses
        city names instead of node ids
        """
        test_graph = graphs.MatrixDefinedGraph(self.test_proper_matrix)
        explorer = explorers.BfsExplorer(test_graph)
        path = explorer.find_path_cities(data.cities[0], data.cities[1])
        self.assertSequenceEqual(path, [0, 2, 1])


if __name__ == '__main__':
    unittest.main()
