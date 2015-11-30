import unittest

from solver.parser.parser import Parser
from solver.general.brute_force import BruteForceSolver


class BruteForceTest(unittest.TestCase):

    def setUp(self):
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_cycle = 'tests/input_files/test_cycle.in'
        self.test_input_dag_one = 'tests/input_files/test_input_dag_one.in'

        self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
        self.matrix_input_cycle = Parser(self.test_input_cycle).generate_matrix()
        self.matrix_input_dag_one = Parser(self.test_input_dag_one).generate_matrix()

    def test_brute_force(self):
        expected_output_one = [0, 2, 1, 3]
        observed_output_one = \
            BruteForceSolver(self.matrix_input_one).maximum_acyclic_subgraph()
        self.assertEqual(expected_output_one, observed_output_one)

        expected_output_cycle = [0, 1, 2, 3]
        observed_output_cycle = \
            BruteForceSolver(self.matrix_input_cycle).maximum_acyclic_subgraph()
        self.assertEqual(expected_output_cycle, observed_output_cycle)

        expected_output_dag_one = [0, 1, 2, 3]
        observed_output_dag_one = \
            BruteForceSolver(self.matrix_input_dag_one).maximum_acyclic_subgraph()
        self.assertEqual(expected_output_dag_one, observed_output_dag_one)
