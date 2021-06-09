from collections import deque
from graphs import AbstractGraph


class GraphExplorer(object):
    def __init__(self, graph):
        if not isinstance(graph, AbstractGraph):
            raise TypeError("Value of a \"graph\" parameter has to be AbstractGraph")
        self._graph = graph

    def find_path(self, starting_node, ending_node):
        raise NotImplementedError()


class BfsExplorer(GraphExplorer):
    def find_path(self, starting_node, last_node):
        previous_nodes = self._solve(starting_node)
        return self._reconstruct_path(starting_node, last_node, previous_nodes)

    def _solve(self, starting_node):
        node_queue = deque()
        node_queue.append(starting_node)

        visited = [False if i != starting_node else True for i in self._graph.get_node_list()]
        previous_nodes = [None for _ in self._graph.get_node_list()]

        while len(node_queue):
            current_node = node_queue.popleft()
            neighbours = self._graph.get_neighbour_nodes(current_node)

            for next_node in neighbours:
                if not visited[next_node]:
                    node_queue.append(next_node)
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
