class PlanarSolver(object):

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def is_planar(self):
        """
        Uses the following tests to determine if the inputted graph
        is planar or is not planar:
        1. If you have a graph G = (V, E) that is connected and has
           |V| > 2, then if |E| > 3|V| - 6, G is not planar.
        2. Check if graph G has K(5) or K(3,3) as minors,
           return True /False on planarity and nodes of "bad_minor"
        """
        num_vertices = len(self.adj_matrix)
        outgoing_edges = [node.count(1) for node in self.adj_matrix]
        num_edges = reduce(lambda x, y: x + y, outgoing_edges)
        if num_edges > 3 * num_vertices - 6:
            return False
        else:
            return True  # Replace with an appropriate checking function

    def maximum_acyclic_subgraph(self):
        if not self.is_planar():
            return None
        else:
            return True  # Replace with the algorithm for MAS on planar graphs.
