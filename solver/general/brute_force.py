from solver.staff.scorer_single import scoreSolution

from itertools import permutations


class BruteForceSolver(object):
    '''
    Computes an optimal solution to MAS by using the brute force strategy,
    namely by exploring every possible topological sort of edges in the graph.
    This can only be used for graphs will less than ___ nodes (experimentation
    was used to determine this number).

    The runtime of this algorithm is O(n!).
    '''
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def maximum_acyclic_subgraph(self):
        vertices = range(len(self.adj_matrix))
        vertex_permutations = permutations(vertices)
        max_score = 0
        max_ordering = vertices
        for permutation in vertex_permutations:
            score = scoreSolution(self.adj_matrix, permutation)
            if score > max_score:
                max_score = score
                max_ordering = permutation
        return list(max_ordering)
