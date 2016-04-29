import unittest
import random

from solver.parser.parser import Parser
from solver.general.simulated_annealing import SimulatedAnnealingSolver
from solver.staff.scorer_single import scoreSolution


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

        observed_output_new_graph = SimulatedAnnealingSolver(
            self.initial_ordering_new_graph,
            self.matrix_new_graph
        ).maximum_acyclic_subgraph()

        expected_score_new_graph = 54.0
        observed_score_new_graph = scoreSolution(self.matrix_new_graph, observed_output_new_graph)

        self.assertEquals(observed_score_new_graph, expected_score_new_graph)

        observed_output_foster = SimulatedAnnealingSolver(
            self.initial_ordering_foster,
            self.matrix_foster
        ).maximum_acyclic_subgraph()

        expected_score_foster = 113.0
        observed_score_foster = scoreSolution(self.matrix_foster, observed_output_foster)
        self.assertEquals(observed_score_foster, expected_score_foster)

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

        expected_output_nonplanar_one = [7, 8, 9, 2, 12, 13, 3, 10, 11, 4, 5, 0, 1, 6]
        observed_output_nonplanar_one = SimulatedAnnealingSolver(
            self.initial_ordering_input_nonplanar_one,
            self.matrix_input_nonplanar_one
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_one, expected_output_nonplanar_one)

        expected_output_nonplanar_two = [1, 5, 7, 2, 0, 6, 4, 3]
        observed_output_nonplanar_two = SimulatedAnnealingSolver(
            self.initial_ordering_input_nonplanar_two,
            self.matrix_input_nonplanar_two
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_two, expected_output_nonplanar_two)

        observed_output_gray = SimulatedAnnealingSolver(
            self.initial_ordering_input_gray,
            self.matrix_input_gray
        ).maximum_acyclic_subgraph()

        expected_score_gray = 70.0
        observed_score_gray = scoreSolution(self.matrix_input_gray, observed_output_gray)
        self.assertEquals(observed_score_gray, expected_score_gray)

if __name__ == '__main__':
    unittest.main()
