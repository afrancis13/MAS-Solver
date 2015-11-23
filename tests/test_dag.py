import unittest

from solver.parser.parser import Parser
from solver.dag.dag_solver import DAGSolver


class DAGSolverTest(unittest.TestCase):

    def setUp(self):
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_dag_one = 'tests/input_files/test_input_dag_one.in'
        self.test_input_dag_two = 'tests/input_files/test_input_dag_two.in'

        self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
        self.matrix_input_dag_one = Parser(self.test_input_dag_one).generate_matrix()
        self.matrix_input_dag_two = Parser(self.test_input_dag_two).generate_matrix()

    def test_topological_sort(self):
    	'''
        Tests three input files with the Topological Sorting algorithm in
        the DAG package in solver. The first graph is not a DAG, so the algorithm
        should correctly make this determination.

        Gyazo links for the graphs are attached, for clarity:
        1. Test input one: https://gyazo.com/74dcc4c2eccd617381867274ce981859
        2. Test input DAG one: https://gyazo.com/eae09e06bf5f4b0150977bf487399001
        3. Test input DAG two: https://gyazo.com/8b241b60a8339d993fcda0b6ca6401a6
        '''
        expected_output_one = None
        observed_output_one = DAGSolver(self.matrix_input_one).topological_sort()
        self.assertEquals(observed_output_one, expected_output_one)

        expected_output_dag_one = [0, 1, 2, 3]
        observed_output_dag_one = DAGSolver(self.matrix_input_dag_one).topological_sort()
        self.assertEquals(observed_output_dag_one, expected_output_dag_one)

        # Could also be linearized as [1, 2, 0, 3, 4, 5, 6] but the algorithm
        # should break ties arbitrarily and this is chosen
        expected_output_dag_two = [1, 0, 2, 3, 4, 5, 6]
        observed_output_dag_two = DAGSolver(self.matrix_input_dag_two).topological_sort()
        self.assertEquals(observed_output_dag_two, expected_output_dag_two)

if __name__ == '__main__':
    unittest.main()
