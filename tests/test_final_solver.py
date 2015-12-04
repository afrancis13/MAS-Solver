import random
import unittest

from solver.parser.parser import Parser
from solver.general.final_solver import FinalSolver


class FinalSolverTest(unittest.TestCase):

    def setUp(self):
        self.test_foster = 'tests/input_files/foster.in'
        self.test_connected = 'tests/input_files/connected.in'
        self.test_new_graph = 'tests/input_files/new_graph.in'
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_dag_one = 'tests/input_files/test_input_dag_one.in'
        self.test_input_dag_two = 'tests/input_files/test_input_dag_two.in'
        self.test_input_cycle = 'tests/input_files/test_cycle.in'
        self.test_input_nonplanar_one = 'tests/input_files/test_nonplanar_one.in'
        self.test_input_nonplanar_two = 'tests/input_files/test_nonplanar_two.in'
        self.test_gray = 'tests/input_files/test_gray.in'
        self.test_new_graph = 'tests/input_files/test_new_graph.in'

        self.matrix_new_graph = Parser(self.test_new_graph).generate_matrix()

        self.matrix_foster = Parser(self.test_foster).generate_matrix()
        self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
        self.matrix_input_dag_one = Parser(self.test_input_dag_one).generate_matrix()
        self.matrix_input_dag_two = Parser(self.test_input_dag_two).generate_matrix()
        self.matrix_input_cycle = Parser(self.test_input_cycle).generate_matrix()
        self.matrix_input_nonplanar_one = Parser(self.test_input_nonplanar_one).generate_matrix()
        self.matrix_input_nonplanar_two = Parser(self.test_input_nonplanar_two).generate_matrix()
        self.matrix_input_gray = Parser(self.test_gray).generate_matrix()

    def test_final_solver(self):
        '''
        TODO: Add more tests, especially on our own instances.

        Tests a variety of input graphs (the same as those tested for the two
        approximation). Since the algorithm is randomized, the seed is set,
        though this algorithm should converge towards an optimal solution at a
        much faster rate, especially on graphs of this size.

        Gyazo links are attached for the constructed graphs, and the first cut
        made is denoted for each graph (the seed is set accordingly).
        1. Test input one: https://gyazo.com/74dcc4c2eccd617381867274ce981859
        2. Test input DAG one: https://gyazo.com/eae09e06bf5f4b0150977bf487399001
        3. Test input DAG two: https://gyazo.com/8b241b60a8339d993fcda0b6ca6401a6
        4. Test input cycle: https://gyazo.com/48c0e885e8baca8c0bd34a2f290171c8
        5. Test input nonplanar one: https://gyazo.com/e91def6e27e59de97a5a779b87e659a9
        6. Test input nonplanar two: https://gyazo.com/1295ad7498c8f80ff7ff260287a8d0ae
        '''
        # random.seed(170)

        # expected_output_one = [0, 2, 1, 3]
        # observed_output_one = \
        #     FinalSolver(self.matrix_input_one).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_one, expected_output_one)

        # expected_output_dag_one = [0, 1, 2, 3]
        # observed_output_dag_one = \
        #     FinalSolver(self.matrix_input_dag_one).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_dag_one, expected_output_dag_one)

        # expected_output_cycle = [0, 1, 2, 3]
        # observed_output_cycle = \
        #     FinalSolver(self.matrix_input_cycle).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_cycle, expected_output_cycle)

        # # Could also be linearized as [1, 2, 0, 3, 4, 5, 6] but the algorithm
        # # should break ties arbitrarily and this is chosen
        # expected_output_dag_two = [1, 0, 2, 3, 4, 5, 6]
        # observed_output_dag_two = \
        #     FinalSolver(self.matrix_input_dag_two).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_dag_two, expected_output_dag_two)

        # expected_output_nonplanar_one = [9, 0, 1, 6, 7, 8, 2, 3, 4, 10, 5, 11, 12, 13]
        # observed_output_nonplanar_one = \
        #     FinalSolver(self.matrix_input_nonplanar_one).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_nonplanar_one, expected_output_nonplanar_one)

        # expected_output_nonplanar_two = [5, 0, 7, 6, 4, 3, 1, 2]
        # observed_output_nonplanar_two = \
        #     FinalSolver(self.matrix_input_nonplanar_two).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_nonplanar_two, expected_output_nonplanar_two)

        # expected_output_foster = [
        #     2, 12, 13, 19, 20, 28, 29, 33, 35, 41, 42, 43, 34, 49,
        #     51, 14, 56, 3, 4, 57, 63, 26, 69, 74, 21, 22, 23, 24, 25,
        #     75, 38, 39, 40, 77, 60, 61, 62, 52, 53, 36, 37, 78, 5, 6, 79,
        #     70, 71, 54, 55, 80, 27, 81, 44, 45, 46, 47, 30, 31, 32, 82,
        #     83, 84, 85, 76, 86, 87, 50, 88, 7, 8, 9, 10, 11, 89, 72, 73,
        #     64, 65, 66, 67, 68, 15, 16, 17, 18, 58, 59, 48, 0, 1
        # ]
        # observed_output_foster = \
        #     FinalSolver(self.matrix_foster).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_foster, expected_output_foster)

        # expected_output_gray = [
        #     10, 13, 14, 7, 8, 21, 22, 9, 27, 28, 15, 16, 3, 29, 30, 32, 25,
        #     26, 36, 11, 38, 31, 42, 17, 46, 33, 34, 35, 47, 18, 19, 20, 48,
        #     23, 49, 50, 43, 44, 45, 4, 5, 6, 37, 51, 52, 39, 40, 41, 12, 53,
        #     24, 0, 1, 2
        # ]
        # observed_output_gray = \
        #     FinalSolver(self.matrix_input_gray).maximum_acyclic_subgraph()
        # self.assertEquals(observed_output_gray, expected_output_gray)

        expected_output_new_graph = [

        ]

        observed_output_new_graph = \
            FinalSolver(self.matrix_new_graph).maximum_acyclic_subgraph()
        print observed_output_new_graph
        self.assertEquals(observed_output_new_graph, expected_output_new_graph)


if __name__ == '__main__':
    unittest.main()
