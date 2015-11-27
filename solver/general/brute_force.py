import os

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
    def __init__(self, input_file, adj_matrix):
        self.adj_matrix = adj_matrix
        self.input_file = input_file
        self.output_file = open('order.out', 'w')
        self.path_to_order = os.path.abspath('order.out')

    def maximum_acyclic_subgraph(self):
        vertices = range(1, len(self.adj_matrix) + 1)
        vertex_permutations = permutations(vertices)
        max_score = 0
        max_ordering = vertices
        for permutation in vertex_permutations:
            str_permutation = str(permutation)
            str_permutation = str_permutation.replace('(', '')
            str_permutation = str_permutation.replace(')', '')
            str_permutation = str_permutation.replace(',', '')
            self.output_file.write(str_permutation)
            self.output_file.close()
            score = scoreSolution(self.input_file, self.path_to_order)
            if score > max_score:
                max_score = score
                max_ordering = permutation
            self.output_file = open(self.path_to_order, 'w')
        return list(max_ordering)
