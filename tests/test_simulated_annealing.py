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

        expected_output_new_graph = []
        observed_output_new_graph = SimulatedAnnealingSolver(
            self.initial_ordering_new_graph,
            self.matrix_new_graph
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_new_graph, expected_output_new_graph)

        expected_output_foster = []
        observed_output_foster = SimulatedAnnealingSolver(
            self.initial_ordering_foster,
            self.matrix_foster
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_foster, expected_output_foster)

        expected_output_input_one = []
        observed_output_input_one = SimulatedAnnealingSolver(
            self.initial_ordering_input_one,
            self.matrix_input_one
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_input_one, expected_output_input_one)

        expected_ouput_input_cycle = []
        observed_output_input_cycle = SimulatedAnnealingSolver(
            self.initial_ordering_input_cycle,
            self.matrix_input_cycle
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_input_cycle, expected_ouput_input_cycle)

        expected_output_nonplanar_one = []
        observed_output_nonplanar_one = SimulatedAnnealingSolver(
            self.initial_ordering_input_nonplanar_one,
            self.matrix_input_nonplanar_one
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_one, expected_output_nonplanar_one)

        expected_output_nonplanar_two = []
        observed_output_nonplanar_two = SimulatedAnnealingSolver(
            self.initial_ordering_input_nonplanar_two,
            self.matrix_input_nonplanar_two
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_nonplanar_two, expected_output_nonplanar_two)

        expected_output_gray = []
        observed_output_gray = SimulatedAnnealingSolver(
            self.initial_ordering_input_gray,
            self.matrix_input_gray
        ).maximum_acyclic_subgraph()
        self.assertEquals(observed_output_gray, expected_output_gray)

if __name__ == '__main__':
    unittest.main()
