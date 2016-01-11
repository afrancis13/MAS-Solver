import unittest
import random

from solver.parser.parser import Parser
from solver.general.simulated_annealing import SimulatedAnnealingSolver


class SimulatedAnnealingTest(unittest.TestCase):

    def setUp(self):
        self.test_foster = 'tests/input_files/foster.in'
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_cycle = 'tests/input_files/test_cycle.in'
        self.test_input_nonplanar_one = 'tests/input_files/test_nonplanar_one.in'
        self.test_input_nonplanar_two = 'tests/input_files/test_nonplanar_two.in'
        self.test_gray = 'tests/input_files/test_gray.in'
        self.test_new_graph = 'tests/input_files/test_new_graph.in'

        self.matrix_new_graph = Parser(self.test_new_graph).generate_matrix()
        self.matrix_foster = Parser(self.test_foster).generate_matrix()
        self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
        self.matrix_input_cycle = Parser(self.test_input_cycle).generate_matrix()
        self.matrix_input_nonplanar_one = Parser(self.test_input_nonplanar_one).generate_matrix()
        self.matrix_input_nonplanar_two = Parser(self.test_input_nonplanar_two).generate_matrix()
        self.matrix_input_gray = Parser(self.test_gray).generate_matrix()

        self.initial_ordering_new_graph = [i for i in range(len(self.matrix_new_graph))]
        self.initial_ordering_foster = [i for i in range(len(self.matrix_foster))]
        self.initial_ordering_input_one = [i for i in range(len(self.matrix_input_one))]
        self.initial_ordering_input_cycle = [i for i in range(len(self.matrix_input_cycle))]
        self.initial_ordering_input_nonplanar_one = [
            i for i in range(len(self.matrix_input_nonplanar_one))
        ]
        self.initial_ordering_input_nonplanar_two = [
            i for i in range(len(self.matrix_input_nonplanar_two))
        ]
        self.initial_ordering_input_gray = [i for i in range(len(self.matrix_input_gray))]

    def test_simulated_annealing(self):
        random.seed(170)

        expected_output_new_graph = [
            10, 5, 11, 22, 33, 34, 6, 35, 7, 17, 23, 38, 39, 24, 0, 8,
            36, 25, 26, 1, 2, 9, 18, 3, 27, 19, 28, 29, 37, 12, 30, 31,
            20, 4, 13, 21, 32, 14, 15, 16
        ]
        observed_output_new_graph = SimulatedAnnealingSolver(
            self.initial_ordering_new_graph,
            self.matrix_new_graph
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_new_graph, expected_output_new_graph)

        expected_output_foster = [
            73, 56, 78, 57, 79, 67, 58, 37, 80, 84, 61, 47, 68, 62, 69, 85,
            75, 86, 49, 87, 88, 28, 89, 63, 81, 43, 44, 82, 17, 29, 59, 0,
            50, 51, 64, 38, 30, 65, 76, 52, 70, 7, 13, 48, 25, 45, 31, 1, 71,
            8, 32, 33, 34, 53, 54, 35, 39, 14, 9, 26, 2, 3, 77, 22, 23, 74,
            36, 40, 18, 15, 60, 72, 83, 41, 27, 66, 42, 4, 55, 19, 10, 16,
            11, 46, 5, 20, 12, 24, 6, 21
        ]
        observed_output_foster = SimulatedAnnealingSolver(
            self.initial_ordering_foster,
            self.matrix_foster
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_foster, expected_output_foster)

        expected_output_input_one = [0, 2, 1, 3]
        observed_output_input_one = SimulatedAnnealingSolver(
            self.initial_ordering_input_one,
            self.matrix_input_one
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_input_one, expected_output_input_one)

        expected_ouput_input_cycle = [0, 1, 2, 3]
        observed_output_input_cycle = SimulatedAnnealingSolver(
            self.initial_ordering_input_cycle,
            self.matrix_input_cycle
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_input_cycle, expected_ouput_input_cycle)

        expected_output_nonplanar_one = [1, 6, 7, 8, 9, 10, 2, 3, 11, 12, 13, 4, 0, 5]
        observed_output_nonplanar_one = SimulatedAnnealingSolver(
            self.initial_ordering_input_nonplanar_one,
            self.matrix_input_nonplanar_one
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_one, expected_output_nonplanar_one)

        expected_output_nonplanar_two = [5, 0, 3, 7, 6, 4, 1, 2]
        observed_output_nonplanar_two = SimulatedAnnealingSolver(
            self.initial_ordering_input_nonplanar_two,
            self.matrix_input_nonplanar_two
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_two, expected_output_nonplanar_two)

        expected_output_gray = [
            34, 50, 20, 44, 51, 52, 35, 8, 36, 53, 37, 13, 28, 45, 14, 46, 15,
            29, 47, 38, 16, 0, 21, 48, 30, 42, 3, 1, 22, 4, 43, 39, 49, 23, 5,
            24, 17, 31, 9, 40, 2, 10, 41, 32, 11, 6, 25, 7, 26, 27, 12, 18, 19,
            33
        ]
        observed_output_gray = SimulatedAnnealingSolver(
            self.initial_ordering_input_gray,
            self.matrix_input_gray
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_gray, expected_output_gray)

if __name__ == '__main__':
    unittest.main()
