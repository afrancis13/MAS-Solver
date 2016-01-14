import pdb; pdb.set_trace()
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
        scc_adj_matrix = [[0 for i in range(len(scc))] for j in range(len(scc))]
        for i in range(len(scc)):
            for j in range(len(scc)):
                if self.has_edge(self.adj_matrix, scc[i], scc[j]):
                    scc_adj_matrix[i][j] = 1
        return scc_adj_matrix

    def obtain_library_solution(self, scc_adj_matrix):
        num_vertices = len(scc_adj_matrix)
        library_graph = Graph().Adjacency(scc_adj_matrix)

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
            print "Score is %.4f" % scoreSolution(self.adj_matrix, topo_sort)
            return topo_sort

        # For some reason, this is returned in reverse order by the algorithm.
        # So reverse to get the topologically sorted SCCs.
        scc_graph = self.find_strongly_connected_components()[::-1]

        solution = []

        for scc in scc_graph:
            scc_adj_matrix = self.create_scc_adj_matrix(scc)
            if len(scc_adj_matrix) <= 8:
                brute_force_solver = BruteForceSolver(scc_adj_matrix)
                brute_force_solution = brute_force_solver.maximum_acyclic_subgraph()
                scc_solution = [i for i in range(len(scc_adj_matrix))]
                for i in range(len(brute_force_solution)):
                    scc_conversion_index = brute_force_solution[i]
                    scc_solution[i] = scc[scc_conversion_index]
            else:
                pq = []
                library_solution = self.obtain_library_solution(scc_adj_matrix)
                library_score = scoreSolution(scc_adj_matrix, library_solution)

                print "Finished scoring using library"

                two_approx_solver = TwoApproximationSolver(scc_adj_matrix)
                for i in range(5000):
                    this_solution = two_approx_solver.maximum_acyclic_subgraph()
                    this_score = scoreSolution(scc_adj_matrix, this_solution)

                    # If pq still small, add this solution
                    # Otherwise, new score better than the worst one so far
                    if len(pq) < 5:
                        heapq.heappush(pq, (this_score, this_solution))
                    elif this_score > pq[0][0]:
                        heapq.heappushpop(pq, (this_score, this_solution))

                print "Finished Two Approximation"

                # Add library solution last so it doesn't get overwritten
                heapq.heappush(pq, (library_score, library_solution))

                annealing_score = -float('inf')
                annealing_solution = None
                while len(pq) > 0:
                    curr_soln = heapq.heappop(pq)
                    curr_ordering = curr_soln[1]
                    simulated_annealing_solver = SimulatedAnnealingSolver(
                        curr_ordering,
                        scc_adj_matrix
                    )
                    curr_annealing_solution = simulated_annealing_solver.maximum_acyclic_subgraph()
                    curr_annealing_score = scoreSolution(scc_adj_matrix, curr_annealing_solution)
                    if curr_annealing_score > annealing_score:
                        annealing_score = curr_annealing_score
                        annealing_solution = curr_annealing_solution

                scc_solution = [i for i in range(len(scc_adj_matrix))]
                for i in range(len(annealing_solution)):
                    scc_conversion_index = annealing_solution[i]
                    scc_solution[i] = scc[scc_conversion_index]

            solution.extend(scc_solution)

        print "Score is %.4f" % scoreSolution(self.adj_matrix, solution)
        return solution
