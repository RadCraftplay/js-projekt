import unittest

from src import graphs


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


if __name__ == '__main__':
    unittest.main()
