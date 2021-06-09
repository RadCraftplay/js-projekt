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


class MatrixDefinedGraph(AbstractGraph):
    def __init__(self, adjacency_matrix):
        self._incidence_matrix = self.to_incidence_matrix(adjacency_matrix)

    @staticmethod
    def to_incidence_matrix(adjacency_matrix):
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
