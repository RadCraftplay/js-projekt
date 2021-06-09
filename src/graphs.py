from queue import Queue
from src import utils


class AbstractGraph(object):
    def get_node_list(self):
        raise NotImplementedError()

    def get_amount_of_nodes(self):
        return len(self.get_node_list())

    def get_incidental_edges(self, node):
        raise NotImplementedError()

    def get_nodes_connected_by_edge(self, edge):
        raise NotImplementedError()

    def get_neighbour_nodes(self, node):
        edges = self.get_incidental_edges(node)
        nodes = [self.get_nodes_connected_by_edge(edge) for edge in edges]
        nodes = utils.flatmap(nodes)
        return list(filter(node.__ne__, nodes))


class GraphExplorer(object):
    def __init__(self, graph):
        if graph is not AbstractGraph:
            raise TypeError("Value of a \"graph\" parameter has to be AbstractGraph")
        self.graph = graph

    def find_path(self, starting_node, ending_node):
        raise NotImplementedError()


class BfsExplorer(GraphExplorer):
    def find_path(self, starting_node, last_node):
        previous_nodes = self._solve(starting_node)
        return self._reconstruct_path(starting_node, last_node, previous_nodes)

    def _solve(self, starting_node):
        node_queue = Queue()
        node_queue.put(starting_node)

        visited = [False if i != starting_node else True for i in range(self.graph.get_node_list())]
        previous_nodes = [None for i in range(self.graph.get_node_list())]

        while node_queue.not_empty:
            current_node = node_queue.get()
            neighbours = self.graph.get_neighbour_nodes(current_node)

            for next_node in neighbours:
                if not visited[next_node]:
                    node_queue.put(next_node)
                    visited[next_node] = True
                    previous_nodes[next_node] = current_node
        return previous_nodes

    @staticmethod
    def _reconstruct_path(starting_node, last_node, previous_nodes):
        path = []
        actual = last_node

        while actual is not None:
            path.append(actual)
            actual = previous_nodes[actual]

        path.reverse()

        if path[0] == starting_node:
            return path
        return []
