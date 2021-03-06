from src import utils, data
from abc import ABCMeta, abstractmethod


class GenerationError(Exception):
    def __init__(self, inner_exception):
        self.inner_exception = inner_exception


class AdjacencyListGenerationError(GenerationError):
    def __str__(self):
        return "Wystąpił błąd w trakcie generowania listy sąsiedztwa:\n" + str(self.inner_exception)


class AdjacencyMatrixGenerationError(GenerationError):
    def __str__(self):
        return "Wystąpił błąd w trakcie generowania macierzy sąsiedztwa:\n" + str(self.inner_exception)


class Generators(object):
    @staticmethod
    def generate_adjacency_lists(list_of_node_pairs):
        """
        Generates adjacency lists based on list of node pairs

        :param list_of_node_pairs: Connected node pairs
        :return: Adjacency lists
        """
        adjacency_lists = [[] for _ in data.cities]

        for pair in list_of_node_pairs:
            try:
                a, b = pair.to_graph_node_ids()
            except utils.CityNotFoundError as err:
                raise AdjacencyListGenerationError(err)

            adjacency_lists[a].append(b)

        return adjacency_lists

    @staticmethod
    def generate_adjacency_matrix(list_of_node_pairs):
        """
        Generates adjacency matrix based on list of node pairs

        :param list_of_node_pairs: Connected node pairs
        :return: Adjacency matrix
        """
        adjacency_matrix = [[0 for _ in data.cities] for _ in data.cities]

        for pair in list_of_node_pairs:
            try:
                a, b = pair.to_graph_node_ids()
            except utils.CityNotFoundError as err:
                raise AdjacencyMatrixGenerationError(err)

            adjacency_matrix[a][b] = 1

        return adjacency_matrix


class NodePair(object):
    def __init__(self, city_a_name, city_b_name):
        self.a = city_a_name
        self.b = city_b_name

    def to_graph_node_ids(self):
        """
        Gets node ids from city names

        :return: Tuple of node ids
        """
        a_id = utils.get_node_id_of_city_by_name(self.a)
        b_id = utils.get_node_id_of_city_by_name(self.b)
        return a_id, b_id

    def __str__(self):
        return "{0} <=> {1}".format(self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


class AbstractGraph(metaclass=ABCMeta):
    @abstractmethod
    def get_node_list(self):
        """
        Returns list of nodes in a graph

        :return: List of nodes in a graph
        """
        pass

    def get_amount_of_nodes(self):
        """
        Returns amount of nodes in a graph

        :return: Amount nodes in a graph
        """
        return len(self.get_node_list())

    @abstractmethod
    def get_incidental_edges(self, node):
        """
        Returns incidental edges of a node

        :param node: Node id to look for edges of
        :return: Incidental edges of a node
        """
        pass

    @abstractmethod
    def get_nodes_connected_by_edge(self, edge):
        """
        Returns nodes connected by an edge

        :param edge: Id of an edge to look connected nodes for
        :return: List of nodes connected by an edge
        """
        pass

    def get_neighbour_nodes(self, node):
        """
        Returns list of neighbours (nodes) of an provided node

        :param node: Node id to look for neighbours of
        :return: List of neighbours (nodes) of an provided node
        """
        edges = self.get_incidental_edges(node)
        nodes = [self.get_nodes_connected_by_edge(edge) for edge in edges]
        nodes = utils.flatmap(nodes)
        return list(filter(node.__ne__, nodes))


class MatrixDefinedGraph(AbstractGraph):
    def __init__(self, adjacency_matrix):
        self._incidence_matrix = self.to_incidence_matrix(adjacency_matrix)

    @staticmethod
    def to_incidence_matrix(adjacency_matrix):
        """
        Creates incidence matrix from adjacency matrix
        """
        edges = []
        for node_id in range(len(adjacency_matrix)):
            for pointed_node_id in range(len(adjacency_matrix[node_id])):
                if adjacency_matrix[node_id][pointed_node_id] == 0:
                    continue
                if edges.__contains__((pointed_node_id, node_id)):
                    continue
                edges.append((node_id, pointed_node_id))

        incidence_matrix = []
        for node_id in range(len(adjacency_matrix)):
            ends = []
            for edge in edges:
                ends.append(1 if node_id in edge else 0)
            incidence_matrix.append(ends)

        return incidence_matrix

    def get_node_list(self):
        return [i for i in range(len(self._incidence_matrix))]

    def get_incidental_matrix(self):
        return self._incidence_matrix

    def get_incidental_edges(self, node):
        row = self._incidence_matrix[node]
        return [i for i in range(len(row)) if row[i] == 1]

    def get_nodes_connected_by_edge(self, edge):
        return [i for i in range(len(self._incidence_matrix)) if self._incidence_matrix[i][edge] == 1]


class ListDefinedGraph(AbstractGraph):
    def __init__(self, list_of_adjacency_lists):
        self._incidental_edges = self.to_incidental_edge_list(list_of_adjacency_lists)

    @staticmethod
    def to_incidental_edge_list(list_of_adjacency_lists):
        """
        Creates list of incidental edges from adjacency lists
        """
        edges = []
        for index, adjacency_list in enumerate(list_of_adjacency_lists):
            for node in adjacency_list:
                if edges.__contains__((node, index)):
                    continue
                edges.append((index, node))

        return edges

    def get_node_list(self):
        nodes = utils.flatmap(self._incidental_edges)
        max_val = 0 if nodes == [] else max(nodes) + 1
        return [i for i in range(max_val)]

    def get_incidental_edges(self, node):
        incidental_edges_to_node = []
        for index, edge in enumerate(self._incidental_edges):
            if node in edge:
                incidental_edges_to_node.append(index)

        return incidental_edges_to_node

    def get_nodes_connected_by_edge(self, edge):
        return self._incidental_edges[edge]
