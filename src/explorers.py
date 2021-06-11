from collections import deque

from abc import ABCMeta, abstractmethod
from src import utils
from src.graphs import AbstractGraph


class GraphExplorer(metaclass=ABCMeta):
    def __init__(self, graph):
        if not isinstance(graph, AbstractGraph):
            raise TypeError("Value of a \"graph\" parameter has to be AbstractGraph")
        self._graph = graph

    @abstractmethod
    def find_path(self, starting_node, ending_node):
        """
        Tries to find path from starting_node to ending_node

        :param starting_node: First node in a path
        :param ending_node: Last node in a path
        :return: Path in a form of node list (ex. [0, 1, 2])
        """
        pass

    def find_path_cities(self, starting_city, destination_city):
        """
        Tries to find path from starting_city to destination_city

        :param starting_city: First city in a path
        :param destination_city: Last city in a path
        :return: Path in a form of node list (ex. [0, 1, 2])
        """
        c_from = utils.get_node_id_of_city_by_name(starting_city)
        c_to = utils.get_node_id_of_city_by_name(destination_city)
        return self.find_path(c_from, c_to)


class BfsExplorer(GraphExplorer):
    def find_path(self, starting_node, last_node):
        solution = self._solve(starting_node, last_node)

        if not solution:
            return []

        return self._reconstruct_path(starting_node, last_node, solution)

    def _solve(self, starting_node, last_node):
        """
        Tries to find the route to the last_node from starting_node

        :param starting_node: First node in a path
        :param last_node: Last node in a path
        :return:
        """
        node_queue = deque()
        node_queue.append(starting_node)

        visited = [False if i != starting_node else True for i in self._graph.get_node_list()]
        soution = [None for _ in self._graph.get_node_list()]

        while len(node_queue):
            current_node = node_queue.popleft()
            neighbours = self._graph.get_neighbour_nodes(current_node)

            for next_node in neighbours:
                if not visited[next_node]:
                    node_queue.append(next_node)
                    visited[next_node] = True
                    soution[next_node] = current_node

        if len(visited) <= last_node or not visited[last_node]:
            return []

        return soution

    @staticmethod
    def _reconstruct_path(starting_node, last_node, solution):
        """
        Tries to reconstruct the path based on prev
        :param starting_node:
        :param last_node:
        :param solution: Found solution
        :return: Reconstructed path from starting_node to last_node
        """
        path = []
        actual = last_node

        while actual is not None:
            path.append(actual)
            actual = solution[actual]

        path.reverse()

        if path[0] == starting_node:
            return path
        return []
