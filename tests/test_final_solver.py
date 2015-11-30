import random
import unittest

from solver.parser.parser import Parser
from solver.general.final_solver import FinalSolver


class FinalSolverTest(unittest.TestCase):

    def setUp(self):
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_dag_one = 'tests/input_files/test_input_dag_one.in'
        self.test_input_dag_two = 'tests/input_files/test_input_dag_two.in'
        self.test_input_cycle = 'tests/input_files/test_cycle.in'
        self.test_input_nonplanar_one = 'tests/input_files/test_nonplanar_one.in'
        self.test_input_nonplanar_two = 'tests/input_files/test_nonplanar_two.in'

        self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
        self.matrix_input_dag_one = Parser(self.test_input_dag_one).generate_matrix()
        self.matrix_input_dag_two = Parser(self.test_input_dag_two).generate_matrix()
        self.matrix_input_cycle = Parser(self.test_input_cycle).generate_matrix()
        self.matrix_input_nonplanar_one = Parser(self.test_input_nonplanar_one).generate_matrix()
        self.matrix_input_nonplanar_two = Parser(self.test_input_nonplanar_two).generate_matrix()

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
        random.seed(170)

        expected_output_one = [2, 1, 3, 0]
        observed_output_one = \
            FinalSolver(self.matrix_input_one).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_one, expected_output_one)

        expected_output_dag_one = [0, 1, 2, 3]
        observed_output_dag_one = \
            FinalSolver(self.matrix_input_dag_one).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_dag_one, expected_output_dag_one)

        expected_output_cycle = [3, 0, 1, 2]
        observed_output_cycle = \
            FinalSolver(self.matrix_input_cycle).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_cycle, expected_output_cycle)

        # Could also be linearized as [1, 2, 0, 3, 4, 5, 6] but the algorithm
        # should break ties arbitrarily and this is chosen
        expected_output_dag_two = [1, 0, 2, 3, 4, 5, 6]
        observed_output_dag_two = \
            FinalSolver(self.matrix_input_dag_two).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_dag_two, expected_output_dag_two)

        expected_output_nonplanar_one = [1, 2, 3, 9, 10, 11, 13, 4, 5, 6, 7, 12, 8, 0]
        observed_output_nonplanar_one = \
            FinalSolver(self.matrix_input_nonplanar_one).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_one, expected_output_nonplanar_one)

        expected_output_nonplanar_two = [3, 1, 0, 5, 7, 6, 4, 2]
        observed_output_nonplanar_two = \
            FinalSolver(self.matrix_input_nonplanar_two).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_two, expected_output_nonplanar_two)


if __name__ == '__main__':
    unittest.main()
