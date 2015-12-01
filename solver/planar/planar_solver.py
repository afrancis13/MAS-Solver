# from graph_tool import Graph


class PlanarSolver(object):

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def has_edge(self, graph, vertex_one, vertex_two):
        return graph[vertex_one][vertex_two] == 1

    def obtain_edge_list(self):
        edge_list = []
        for vertex_one in range(len(self.adj_matrix)):
            for vertex_two in range(len(self.adj_matrix)):
                if self.has_edge(self.adj_matrix, vertex_one, vertex_two):
                    edge_list.append((vertex_one, vertex_two))
        return edge_list

    def is_planar(self):
        """
        See the following library:
        https://graph-tool.skewed.de/static/doc/topology.html
        """
        edges = self.obtain_edge_list()
        graph = Graph().add_vertex(len(self.adj_matrix)).add_edge_list(edges)
        return graph.is_planar()

    def maximum_acyclic_subgraph(self):
        """
        Here's the argument:

        The maximum acyclic subgraph problem can be solved in O(n^3) time
        in a planar graph. These finding are found in the literature
        surrounding this problem, namely in Algorithms and Combinitorics 2,
        and an article which cites that text. Both of these are cited in
        cited.txt.

        The computation borrows from a brilliant Python library called igraph
        http://igraph.org/

        It is possible to run an exact computation on small graphs using one
        method. "Smallness" is defined as having less than 15 nodes. Otherwise,
        an approximation algorithm is used.

        Note that the problem actually being solved here is the minimum
        feedback arc set problem, which is equivalent to MAS.
        """
        if not self.is_planar():
            return None

        return None
