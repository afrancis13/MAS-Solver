import unittest
import random

from solver.parser.parser import Parser
from solver.general.two_approx import TwoApproximationSolver


class TwoApproximationTest(unittest.TestCase):

    def setUp(self):
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_dag_one = 'tests/input_files/test_input_dag_one.in'
        self.test_input_dag_two = 'tests/input_files/test_input_dag_two.in'
        self.test_input_cycle = 'tests/input_files/test_cycle.in'
        self.test_input_nonplanar_one = 'tests/input_files/test_input_nonplanar_one.in'
        self.test_input_nonplanar_two = 'tests/input_files/test_input_nonplanar_two.in'

        self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
        self.matrix_input_dag_one = Parser(self.test_input_dag_one).generate_matrix()
        self.matrix_input_dag_two = Parser(self.test_input_dag_two).generate_matrix()
        self.matrix_input_cycle = Parser(self.test_input_cycle).generate_matrix()
        self.matrix_input_nonplanar_one = Parser(self.test_input_nonplanar_one).generate_matrix()
        self.matrix_input_nonplanar_two = Parser(self.test_input_nonplanar_two).generate_matrix()

    def test_two_approximation(self):
        '''
        Tests that the approximation algorithm correctly returns a specified
        linearized ordering. Note that this algorithm is randomized, so
        we set a seed before running the tests.

        Gyazo links are attached for the constructed graphs, and the first cut
        made is denoted for each graph (the seed is set accordingly).
        '''
        random.seed(170)

        expected_output_one = [1, 3, 2, 4]
        observed_output_one = \
            TwoApproximationSolver(self.matrix_input_one).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_one, expected_output_one)

        expected_output_dag_one = [0, 1, 2, 3]
        observed_output_dag_one = \
            TwoApproximationSolver(self.matrix_input_dag_one).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_dag_one, expected_output_dag_one)

        expected_output_cycle = [1, 2, 3, 4]
        observed_output_cycle = \
            TwoApproximationSolver(self.matrix_input_cycle).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_cycle, expected_output_cycle)

        # Could also be linearized as [1, 2, 0, 3, 4, 5, 6] but the algorithm
        # should break ties arbitrarily and this is chosen
        expected_output_dag_two = [1, 0, 2, 3, 4, 5, 6]
        observed_output_dag_two = \
            TwoApproximationSolver(self.matrix_input_dag_two).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_dag_two, expected_output_dag_two)

        expected_output_nonplanar_one = []
        observed_output_nonplanar_one = \
            TwoApproximationSolver(self.matrix_input_nonplanar_one).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_one, expected_output_nonplanar_one)

        expected_output_nonplanar_two = []
        observed_output_nonplanar_two = \
            TwoApproximationSolver(self.matrix_input_nonplanar_two).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_two, expected_output_nonplanar_two)


if __name__ == '__main__':
    unittest.main()
