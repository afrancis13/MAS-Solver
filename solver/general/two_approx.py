from random import randint, choice, shuffle
from copy import deepcopy

from solver.dag.dag_solver import DAGSolver

from solver.staff.scorer_single import scoreSolution


class TwoApproximationSolver(object):
    '''
    Gives a two approximation on general graphs with the following
    strategy.

    Divide a graph G = (V, E) into two non-empty sets A, B. Examine the
    edges between A and B and examine the edges between B and A. Call the
    magnitudes of the set of edges |E_{a,b}| and |E_{b,a}|, respectively.
    Discard the edges in the smaller set. Recurse on the sides A and B until
    the topological sorting algorithm can be run!
    '''
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def has_edge(self, graph, vertex_one, vertex_two):
        return graph[vertex_one][vertex_two] == 1

    def compute_edges_over_cut(self, graph, cut):
        edges_over_cut = []
        for vertex_one in cut:
            vertex_candidates = graph[vertex_one]
            for vertex_two in range(len(vertex_candidates)):
                if vertex_two not in cut and self.has_edge(graph, vertex_one, vertex_two):
                    edges_over_cut.append((vertex_one, vertex_two))
        return edges_over_cut

    def make_cut(self, graph):
        vertices = [i for i in range(len(graph))]
        size_cut_one = randint(1, len(vertices))
        cut_one = []
        for i in range(size_cut_one):
            vertex_choice = choice(vertices)
            vertices.remove(vertex_choice)
            cut_one.append(vertex_choice)
        cut_two = vertices
        return cut_one, cut_two

    def maximum_acyclic_subgraph_helper(self, graph):
        '''
        Graph is an adjacency matrix, and is continuously changed.
        Calls make_cut to determine the cut, the computes the edges over each
        cut (from A to B and B to A, in the manner described above), removing
        edges in the graph and calling the helper function recursively on the
        new graphs.
        '''
        linearizing_agent = DAGSolver(graph)
        topo_sort = linearizing_agent.topological_sort()

        while topo_sort is None:
            cut_one, cut_two = self.make_cut(graph)
            edges_one_to_two = self.compute_edges_over_cut(graph, cut_one)
            edges_two_to_one = self.compute_edges_over_cut(graph, cut_two)

            if len(edges_one_to_two) >= len(edges_two_to_one):
                for vertex_one, vertex_two in edges_two_to_one:
                    graph[vertex_one][vertex_two] = 0
            else:
                for vertex_one, vertex_two in edges_one_to_two:
                    graph[vertex_one][vertex_two] = 0

            linearizing_agent = DAGSolver(graph)
            topo_sort = linearizing_agent.topological_sort()

        return topo_sort

    def maximum_acyclic_subgraph(self):
        # adj_matrix_copy = deepcopy(self.adj_matrix)
        # return self.maximum_acyclic_subgraph_helper(adj_matrix_copy)
        vertices = [i for i in range(len(self.adj_matrix))]
        shuffle(vertices)
        score_vertices = scoreSolution(self.adj_matrix, vertices)
        reverse_vertices = vertices[::-1]
        score_reverse = scoreSolution(self.adj_matrix, reverse_vertices)
        if score_vertices > score_reverse:
            return vertices
        else:
            return reverse_vertices
