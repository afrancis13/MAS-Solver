from igraph import Graph
from tarjan import tarjan
import heapq

from solver.dag.dag_solver import DAGSolver
from solver.general.brute_force import BruteForceSolver
from solver.general.two_approx import TwoApproximationSolver
from solver.staff.scorer_single import scoreSolution
from solver.general.simulated_annealing import SimulatedAnnealingSolver


class FinalSolver(object):
    '''
    TODO: Integrate planar graph logic into the following.

    Here's the strategy for the final solver:
    1. Try to run a topological sort on G. This will only work if G is
       a DAG.
    2. Divide the graph into it's strongly connected components.
        a. For all subgraphs of size > 8, run the TwoApproximationSolver on
           it 10000 times. This will likely find a pretty good subgraph MAS.
        b. Otherwise, brute force it.

    This will run fairly well on all instances except ones in which there
    is one single, large, strongly connected component. This will be the
    motivation for the extreme cases.
    '''
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def has_edge(self, graph, vertex_one, vertex_two):
        return graph[vertex_one][vertex_two] == 1

    def find_strongly_connected_components(self):
        formatted_graph = {}
        for vertex_one in range(len(self.adj_matrix)):
            edges_from_vertex_one = []
            for vertex_two in range(len(self.adj_matrix)):
                if self.has_edge(self.adj_matrix, vertex_one, vertex_two):
                    edges_from_vertex_one.append(vertex_two)
            formatted_graph[vertex_one] = edges_from_vertex_one

        strongly_connected_components = tarjan(formatted_graph)

        return strongly_connected_components

    def create_scc_adj_matrix(self, scc):
        scc_adj_matrix = [[0 for i in range(len(self.adj_matrix))] for j in range(len(self.adj_matrix))]
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if i in scc and j in scc and self.has_edge(self.adj_matrix, i, j):
                    scc_adj_matrix[i][j] = 1
        return scc_adj_matrix

    def obtain_library_solution(self):
        num_vertices = len(self.adj_matrix)
        library_graph = Graph().Adjacency(self.adj_matrix)

        if num_vertices < 10:
            removed_edges = library_graph.feedback_arc_set(method='ip')
        else:
            removed_edges = library_graph.feedback_arc_set(method='eades')

        library_graph.delete_edges(removed_edges)
        library_graph_adj_matrix = library_graph.get_adjacency()._get_data()
        library_graph_dag_solver = DAGSolver(library_graph_adj_matrix)
        solution = library_graph_dag_solver.topological_sort()

        return solution

    def maximum_acyclic_subgraph(self):
        topo_sort = DAGSolver(self.adj_matrix).topological_sort()

        if topo_sort is not None:
            # print "Score is %.4f" % scoreSolution(self.adj_matrix, topo_sort)
            return topo_sort

        # For some reason, this is returned in reverse order by the algorithm,
        # so reverse to get the topologically sorted SCCs.
        scc_graph = self.find_strongly_connected_components()[::-1]

        solution = []

        for scc in scc_graph:
            scc_adj_matrix = self.create_scc_adj_matrix(scc)
            if len(scc_adj_matrix) <= 8:
                brute_force_solver = BruteForceSolver(scc_adj_matrix)
                scc_solution = brute_force_solver.maximum_acyclic_subgraph()
            else:
                max_library_score = 0
                max_library_soln = None
                PQ = []
                library_solution = self.obtain_library_solution()
                library_score = scoreSolution(scc_adj_matrix, library_solution)
                if library_score > max_library_score:
                    max_library_score = library_score
                    max_library_soln = library_solution
                

                two_approx_solver = TwoApproximationSolver(scc_adj_matrix)
                max_score = 0
                scc_solution = scc
                for i in range(10000):
                    this_solution = two_approx_solver.maximum_acyclic_subgraph()
                    this_score = scoreSolution(scc_adj_matrix, this_solution)
                    # if this_score > max_score:
                    #     max_score = this_score
                    #     scc_solution = this_solution

                    if len(PQ) < 5: #if PQ still small, add this solution
                        heapq.heappush(PQ, (-this_score, this_solution))

                    elif -this_score < pq[0][1]: #new score better than the worst one so far
                        heapq.heappushpop(PQ, (-this_score, this_solution))

                #add library solution last so it doesn't get overwritten
                heapq.heappush(PQ, (-max_library_score, max_library_soln))

                annealing_score = -float('inf')
                annealing_soln = scc_solution
                while len(PQ) > 0:
                    curr_soln = heapq.heappop(PQ)[1]
                    simulated_annealing_solver = SimulatedAnnealingSolver(curr_soln, scc_adj_matrix)
                    this_solution = simulated_annealing_solver.maximum_acyclic_subgraph()
                    this_score = scoreSolution(scc_adj_matrix, this_solution)
                    if this_score > annealing_score:
                        annealing_score = this_score
                        annealing_soln = this_solution


            solution.extend(annealing_soln)
            #solution.extend(scc_solution)

        # print "Score is %.4f" % scoreSolution(self.adj_matrix, solution)
        return solution
