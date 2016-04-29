import unittest
import time

from solver.parser.parser import Parser
from solver.dag.dag_solver import DAGSolver
from solver.general.brute_force import BruteForceSolver
from solver.general.simulated_annealing import SimulatedAnnealingSolver
from solver.general.two_approx import TwoApproximationSolver
from solver.general.final_solver import FinalSolver
from solver.staff.scorer_single import scoreSolution


class Benchmark(unittest.TestCase):
    '''
    Simply uses the time library to perform benchmarks
    on the empirical running time of different deterministic
    and approximation algorithms, both exclusively and
    in conjunction. These results are recorded in the paper
    attached to the README.
    '''

    @classmethod
    def setUpClass(cls):
        cls.benchmark_file = open('benchmark.txt', 'w')

        cls.test_input_dag_one = 'tests/input_files/test_input_dag_one.in'
        cls.test_input_dag_two = 'tests/input_files/test_input_dag_two.in'
        cls.test_input_dag_three = 'tests/input_files/test_random_dag_size_20.in'
        cls.test_input_dag_four = 'tests/input_files/test_random_dag_size_100.in'
        cls.test_input_dag_five = 'tests/input_files/test_random_dag_size_1000.in'
        # cls.test_input_dag_six = 'tests/input_files/test_random_dag_size_10000.in'

        cls.matrix_input_dag_one = Parser(cls.test_input_dag_one).generate_matrix()
        cls.matrix_input_dag_two = Parser(cls.test_input_dag_two).generate_matrix()
        cls.matrix_input_dag_three = Parser(cls.test_input_dag_three).generate_matrix()
        cls.matrix_input_dag_four = Parser(cls.test_input_dag_four).generate_matrix()
        cls.matrix_input_dag_five = Parser(cls.test_input_dag_five).generate_matrix()
        # cls.matrix_input_dag_six = Parser(cls.test_input_dag_six).generate_matrix()

        cls.test_input_brute_force_one = 'tests/input_files/test_random_graph_size_2.in'
        cls.test_input_brute_force_two = 'tests/input_files/test_random_graph_size_4.in'
        cls.test_input_brute_force_three = 'tests/input_files/test_random_graph_size_8.in'
        cls.test_input_brute_force_six = 'tests/input_files/test_random_graph_size_10.in'
        cls.test_input_brute_force_seven = 'tests/input_files/test_random_graph_size_12.in'
        cls.test_input_brute_force_four = 'tests/input_files/test_random_graph_size_16.in'
        cls.test_input_brute_force_five = 'tests/input_files/test_random_graph_size_25.in'

        cls.matrix_input_brute_force_one = Parser(cls.test_input_brute_force_one).generate_matrix()
        cls.matrix_input_brute_force_two = Parser(cls.test_input_brute_force_two).generate_matrix()
        cls.matrix_input_brute_force_three = Parser(cls.test_input_brute_force_three).generate_matrix()
        cls.matrix_input_brute_force_four = Parser(cls.test_input_brute_force_four).generate_matrix()
        cls.matrix_input_brute_force_five = Parser(cls.test_input_brute_force_five).generate_matrix()
        cls.matrix_input_brute_force_six = Parser(cls.test_input_brute_force_six).generate_matrix()
        cls.matrix_input_brute_force_seven = Parser(cls.test_input_brute_force_seven).generate_matrix()

        cls.test_random_graph_size_100 = 'tests/input_files/test_random_graph_size_100.in'
        cls.test_random_graph_size_1000 = 'tests/input_files/test_random_graph_size_1000.in'
        # cls.test_random_graph_size_10000 = 'tests/input_files/test_random_graph_size_10000.in'

        cls.matrix_input_size_100 = Parser(cls.test_random_graph_size_100).generate_matrix()
        cls.matrix_input_size_1000 = Parser(cls.test_random_graph_size_1000).generate_matrix()
        # cls.matrix_input_size_10000 = Parser(cls.test_random_graph_size_10000).generate_matrix()

    @classmethod
    def tearDownClass(cls):
        cls.benchmark_file.close()

    def test_benchmark_dag(self):
        '''
        Tests that random graph generators are working properly, and generates the
        benchmark data that is saved to `benchmark.txt` in the root directory for
        this project.
        '''
        # |V| = 4
        pre_time_dag_one = time.time()
        output_dag_one = DAGSolver(self.matrix_input_dag_one).topological_sort()
        post_time_dag_one = time.time()
        solving_time_dag_one = post_time_dag_one - pre_time_dag_one
        self.assertIsNotNone(output_dag_one)
        score_dag_one = scoreSolution(self.matrix_input_dag_one, output_dag_one)
        file_string_one = "DAG, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_dag_one, solving_time_dag_one)
        self.benchmark_file.write(file_string_one)
        print "Finished Benchmark 1, DAG"

        # |V| = 7
        pre_time_dag_two = time.time()
        output_dag_two = DAGSolver(self.matrix_input_dag_two).topological_sort()
        post_time_dag_two = time.time()
        solving_time_dag_two = post_time_dag_two - pre_time_dag_two
        self.assertIsNotNone(output_dag_two)
        score_dag_two = scoreSolution(self.matrix_input_dag_two, output_dag_two)
        file_string_two = "DAG, |V| = 7: Score = %.4f, Time = %.4f\n" % (score_dag_two, solving_time_dag_two)
        self.benchmark_file.write(file_string_two)
        print "Finished Benchmark 2, DAG"

        # |V| = 20
        pre_time_dag_three = time.time()
        output_dag_three = DAGSolver(self.matrix_input_dag_three).topological_sort()
        post_time_dag_three = time.time()
        solving_time_dag_three = post_time_dag_three - pre_time_dag_three
        self.assertIsNotNone(output_dag_three)
        score_dag_three = scoreSolution(self.matrix_input_dag_three, output_dag_three)
        file_string_three = "DAG, |V| = 20: Score = %.4f, Time = %.4f\n" % (score_dag_three, solving_time_dag_three)
        self.benchmark_file.write(file_string_three)
        print "Finished Benchmark 3, DAG"

        # |V| = 100
        pre_time_dag_four = time.time()
        output_dag_four = DAGSolver(self.matrix_input_dag_four).topological_sort()
        post_time_dag_four = time.time()
        solving_time_dag_four = post_time_dag_four - pre_time_dag_four
        self.assertIsNotNone(output_dag_four)
        score_dag_four = scoreSolution(self.matrix_input_dag_four, output_dag_four)
        file_string_four = "DAG, |V| = 100: Score = %.4f, Time = %.4f\n" % (score_dag_four, solving_time_dag_four)
        self.benchmark_file.write(file_string_four)
        print "Finished Benchmark 4, DAG"

        # |V| = 1000
        pre_time_dag_five = time.time()
        output_dag_five = DAGSolver(self.matrix_input_dag_five).topological_sort()
        post_time_dag_five = time.time()
        solving_time_dag_five = post_time_dag_five - pre_time_dag_five
        self.assertIsNotNone(output_dag_five)
        score_dag_five = scoreSolution(self.matrix_input_dag_five, output_dag_five)
        file_string_five = "DAG, |V| = 1000: Score = %.4f, Time = %.4f\n" % (score_dag_five, solving_time_dag_five)
        self.benchmark_file.write(file_string_five)
        print "Finished Benchmark 5, DAG"

        # |V| = 10000
        # pre_time_dag_six = time.time()
        # output_dag_six = DAGSolver(self.matrix_input_dag_six).topological_sort()
        # post_time_dag_six = time.time()
        # solving_time_dag_six = post_time_dag_six - pre_time_dag_six
        # self.assertIsNotNone(output_dag_six)
        # score_dag_six = scoreSolution(self.matrix_input_dag_six, output_dag_six)
        # file_string_six = "DAG, |V| = 10000: Score = %.4f, Time = %.4f\n" % (score_dag_six, solving_time_dag_six)
        # self.benchmark_file.write(file_string_six)
        # print "Finished Benchmark 6, DAG"

    def test_benchmark_brute_force(self):
        # |V| = 2
        pre_time_brute_force_one = time.time()
        output_brute_force_one = BruteForceSolver(self.matrix_input_brute_force_one).maximum_acyclic_subgraph()
        post_time_brute_force_one = time.time()
        solving_time_brute_force_one = post_time_brute_force_one - pre_time_brute_force_one
        self.assertIsNotNone(output_brute_force_one)
        score_brute_force_one = scoreSolution(self.matrix_input_brute_force_one, output_brute_force_one)
        file_string_one = "Brute Force, |V| = 2: Score = %.4f, Time = %.4f\n" % (score_brute_force_one, solving_time_brute_force_one)
        self.benchmark_file.write(file_string_one)
        print("Finished Benchmark 1, Brute Force")

        # |V| = 4
        pre_time_brute_force_two = time.time()
        output_brute_force_two = BruteForceSolver(self.matrix_input_brute_force_two).maximum_acyclic_subgraph()
        post_time_brute_force_two = time.time()
        solving_time_brute_force_two = post_time_brute_force_two - pre_time_brute_force_two
        self.assertIsNotNone(output_brute_force_two)
        score_brute_force_two = scoreSolution(self.matrix_input_brute_force_two, output_brute_force_two)
        file_string_two = "Brute Force, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_brute_force_two, solving_time_brute_force_two)
        self.benchmark_file.write(file_string_two)
        print "Finished Benchmark 2, Brute Force"

        # |V| = 8
        pre_time_brute_force_three = time.time()
        output_brute_force_three = BruteForceSolver(self.matrix_input_brute_force_three).maximum_acyclic_subgraph()
        post_time_brute_force_three = time.time()
        solving_time_brute_force_three = post_time_brute_force_three - pre_time_brute_force_three
        self.assertIsNotNone(output_brute_force_three)
        score_brute_force_three = scoreSolution(self.matrix_input_brute_force_three, output_brute_force_three)
        file_string_three = "Brute Force, |V| = 8: Score = %.4f, Time = %.4f\n" % (score_brute_force_three, solving_time_brute_force_three)
        self.benchmark_file.write(file_string_three)
        print "Finished Benchmark 3, Brute Force"

        # |V| = 10
        # pre_time_brute_force_six = time.time()
        # output_brute_force_six = BruteForceSolver(self.matrix_input_brute_force_six).maximum_acyclic_subgraph()
        # post_time_brute_force_six = time.time()
        # solving_time_brute_force_six = post_time_brute_force_six - pre_time_brute_force_six
        # self.assertIsNotNone(output_brute_force_six)
        # score_brute_force_six = scoreSolution(self.matrix_input_brute_force_six, output_brute_force_six)
        # file_string_six = "Brute Force, |V| = 10: Score = %.4f, Time = %.4f\n" % (score_brute_force_six, solving_time_brute_force_six)
        # self.benchmark_file.write(file_string_six)
        # print "Finished Benchmark 4, Brute Force"

        # |V| = 12
        # pre_time_brute_force_seven = time.time()
        # output_brute_force_seven = BruteForceSolver(self.matrix_input_brute_force_seven).maximum_acyclic_subgraph()
        # post_time_brute_force_seven = time.time()
        # solving_time_brute_force_seven = post_time_brute_force_seven - pre_time_brute_force_seven
        # self.assertIsNotNone(output_brute_force_seven)
        # score_brute_force_seven = scoreSolution(self.matrix_input_brute_force_seven, output_brute_force_seven)
        # file_string_seven = "Brute Force, |V| = 12: Score = %.4f, Time = %.4f\n" % (score_brute_force_seven, solving_time_brute_force_seven)
        # self.benchmark_file.write(file_string_seven)
        # print "Finished Benchmark 5, Brute Force"

    def test_benchmark_planar_graphs(self):
        # |V| = 4
        # |V| = 25
        # |V| = 100
        # |V| = 1000
        # |V| = 10000
        pass

    def test_benchmark_simulated_annealing(self):
        # |V| = 4
        pre_time_sa_one = time.time()
        output_sa_one = SimulatedAnnealingSolver(
            range(len(self.matrix_input_brute_force_two)),
            self.matrix_input_brute_force_two
        ).maximum_acyclic_subgraph()
        post_time_sa_one = time.time()
        solving_time_sa_one = post_time_sa_one - pre_time_sa_one
        self.assertIsNotNone(output_sa_one)
        score_sa_one = scoreSolution(self.matrix_input_brute_force_two, output_sa_one)
        file_string_one = "Simulated Annealing, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_sa_one, solving_time_sa_one)
        self.benchmark_file.write(file_string_one)

        # |V| = 25
        pre_time_sa_two = time.time()
        output_sa_two = SimulatedAnnealingSolver(
            range(len(self.matrix_input_brute_force_five)),
            self.matrix_input_brute_force_five
        ).maximum_acyclic_subgraph()
        post_time_sa_two = time.time()
        solving_time_sa_two = post_time_sa_two - pre_time_sa_two
        self.assertIsNotNone(output_sa_two)
        score_sa_two = scoreSolution(self.matrix_input_brute_force_five, output_sa_two)
        file_string_two = "Simulated Annealing, |V| = 25: Score = %.4f, Time = %.4f\n" % (score_sa_two, solving_time_sa_two)
        self.benchmark_file.write(file_string_two)

        # |V| = 100
        pre_time_sa_three = time.time()
        output_sa_three = SimulatedAnnealingSolver(
            range(len(self.matrix_input_size_100)),
            self.matrix_input_size_100
        ).maximum_acyclic_subgraph()
        post_time_sa_three = time.time()
        solving_time_sa_three = post_time_sa_three - pre_time_sa_three
        self.assertIsNotNone(output_sa_three)
        score_sa_three = scoreSolution(self.matrix_input_size_100, output_sa_three)
        file_string_three = "Simulated Annealing, |V| = 100: Score = %.4f, Time = %.4f\n" % (score_sa_three, solving_time_sa_three)
        self.benchmark_file.write(file_string_three)

        # |V| = 1000
        # pre_time_sa_four = time.time()
        # output_sa_four = SimulatedAnnealingSolver(
        #     range(len(self.matrix_input_size_1000)),
        #     self.matrix_input_size_1000
        # ).maximum_acyclic_subgraph()
        # post_time_sa_four = time.time()
        # solving_time_sa_four = post_time_sa_four - pre_time_sa_four
        # self.assertIsNotNone(output_sa_four)
        # score_sa_four = scoreSolution(self.matrix_input_size_1000, output_sa_four)
        # file_string_four = "Simulated Annealing, |V| = 1000: Score = %.4f, Time = %.4f\n" % (score_sa_four, solving_time_sa_four)
        # self.benchmark_file.write(file_string_four)

        # |V| = 10000
        # pre_time_sa_five = time.time()
        # output_sa_five = SimulatedAnnealingSolver(self.matrix_input_size_10000).maximum_acyclic_subgraph()
        # post_time_sa_five = time.time()
        # solving_time_sa_five = post_time_sa_five - pre_time_sa_five
        # self.assertIsNotNone(output_sa_five)
        # score_sa_five = scoreSolution(self.matrix_input_size_10000, output_sa_five)
        # file_string_five = "Simulated Annealing, |V| = 10000: Score = %.4f, Time = %.4f\n" % (score_sa_five, solving_time_sa_five)
        # self.benchmark_file.write(file_string_five)

    def test_benchmark_two_approximation(self):
        # |V| = 4
        pre_time_two_approx_one = time.time()
        output_two_approx_one = TwoApproximationSolver(self.matrix_input_brute_force_two).maximum_acyclic_subgraph()
        post_time_two_approx_one = time.time()
        solving_time_two_approx_one = post_time_two_approx_one - pre_time_two_approx_one
        self.assertIsNotNone(output_two_approx_one)
        score_two_approx_one = scoreSolution(self.matrix_input_brute_force_two, output_two_approx_one)
        file_string_one = "Two Approximation, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_two_approx_one, solving_time_two_approx_one)
        self.benchmark_file.write(file_string_one)

        # |V| = 25
        pre_time_two_approx_two = time.time()
        output_two_approx_two = TwoApproximationSolver(self.matrix_input_brute_force_five).maximum_acyclic_subgraph()
        post_time_two_approx_two = time.time()
        solving_time_two_approx_two = post_time_two_approx_two - pre_time_two_approx_two
        self.assertIsNotNone(output_two_approx_two)
        score_two_approx_two = scoreSolution(self.matrix_input_brute_force_five, output_two_approx_two)
        file_string_two = "Two Approximation, |V| = 25: Score = %.4f, Time = %.4f\n" % (score_two_approx_two, solving_time_two_approx_two)
        self.benchmark_file.write(file_string_two)

        # |V| = 100
        pre_time_two_approx_three = time.time()
        output_two_approx_three = TwoApproximationSolver(self.matrix_input_size_100).maximum_acyclic_subgraph()
        post_time_two_approx_three = time.time()
        solving_time_two_approx_three = post_time_two_approx_three - pre_time_two_approx_three
        self.assertIsNotNone(output_two_approx_three)
        score_two_approx_three = scoreSolution(self.matrix_input_size_100, output_two_approx_three)
        file_string_three = "Two Approximation, |V| = 100: Score = %.4f, Time = %.4f\n" % (score_two_approx_three, solving_time_two_approx_three)
        self.benchmark_file.write(file_string_three)

        # |V| = 1000
        pre_time_two_approx_four = time.time()
        output_two_approx_four = TwoApproximationSolver(self.matrix_input_size_1000).maximum_acyclic_subgraph()
        post_time_two_approx_four = time.time()
        solving_time_two_approx_four = post_time_two_approx_four - pre_time_two_approx_four
        self.assertIsNotNone(output_two_approx_four)
        score_two_approx_four = scoreSolution(self.matrix_input_size_1000, output_two_approx_four)
        file_string_four = "Two Approximation, |V| = 1000: Score = %.4f, Time = %.4f\n" % (score_two_approx_four, solving_time_two_approx_four)
        self.benchmark_file.write(file_string_four)

        # |V| = 10000
        # pre_time_two_approx_five = time.time()
        # output_two_approx_five = TwoApproximationSolver(self.matrix_input_size_10000).maximum_acyclic_subgraph()
        # post_time_two_approx_five = time.time()
        # solving_time_two_approx_five = post_time_two_approx_five - pre_time_two_approx_five
        # self.assertIsNotNone(output_two_approx_five)
        # score_two_approx_five = scoreSolution(self.matrix_input_size_10000, output_two_approx_five)
        # file_string_five = "Two Approximation, |V| = 10000: Score = %.4f, Time = %.4f\n" % (score_two_approx_five, solving_time_two_approx_five)
        # self.benchmark_file.write(file_string_five)

    def test_benchmark_feedback_arc_set_ip(self):
        # |V| = 2
        pre_time_ip_one = time.time()
        output_solver_one = FinalSolver(self.matrix_input_brute_force_one)
        output_ip_one = output_solver_one.obtain_library_solution(output_solver_one.adj_matrix, force_ip=True)
        post_time_ip_one = time.time()
        solving_time_ip_one = post_time_ip_one - pre_time_ip_one
        self.assertIsNotNone(output_ip_one)
        score_ip_one = scoreSolution(self.matrix_input_brute_force_one, output_ip_one)
        file_string_one = "Ip Approximation, |V| = 2: Score = %.4f, Time = %.4f\n" % (score_ip_one, solving_time_ip_one)
        self.benchmark_file.write(file_string_one)

        # |V| = 4
        pre_time_ip_two = time.time()
        output_solver_two = FinalSolver(self.matrix_input_brute_force_two)
        output_ip_two = output_solver_two.obtain_library_solution(output_solver_two.adj_matrix, force_ip=True)
        post_time_ip_two = time.time()
        solving_time_ip_two = post_time_ip_two - pre_time_ip_two
        self.assertIsNotNone(output_ip_two)
        score_ip_two = scoreSolution(self.matrix_input_brute_force_two, output_ip_two)
        file_string_two = "Ip Approximation, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_ip_two, solving_time_ip_two)
        self.benchmark_file.write(file_string_two)

        # |V| = 8
        pre_time_ip_three = time.time()
        output_solver_three = FinalSolver(self.matrix_input_brute_force_three)
        output_ip_three = output_solver_three.obtain_library_solution(output_solver_three.adj_matrix, force_ip=True)
        post_time_ip_three = time.time()
        solving_time_ip_three = post_time_ip_three - pre_time_ip_three
        self.assertIsNotNone(output_ip_three)
        score_ip_three = scoreSolution(self.matrix_input_brute_force_three, output_ip_three)
        file_string_three = "Ip Approximation, |V| = 8: Score = %.4f, Time = %.4f\n" % (score_ip_three, solving_time_ip_three)
        self.benchmark_file.write(file_string_three)

        # |V| = 16
        # pre_time_ip_four = time.time()
        # output_solver_four = FinalSolver(self.matrix_input_brute_force_four)
        # output_ip_four = output_solver_four.obtain_library_solution(output_solver_four.adj_matrix)
        # post_time_ip_four = time.time()
        # solving_time_ip_four = post_time_ip_four - pre_time_ip_four
        # self.assertIsNotNone(output_ip_four)
        # score_ip_four = scoreSolution(self.matrix_input_brute_force_four, output_ip_four)
        # file_string_four = "Ip Approximation, |V| = 16: Score = %.4f, Time = %.4f\n" % (score_ip_four, solving_time_ip_four)
        # self.benchmark_file.write(file_string_four)

        # # |V| = 25
        # pre_time_ip_five = time.time()
        # output_solver_five = FinalSolver(self.matrix_input_brute_force_five)
        # output_ip_five = output_solver_five.obtain_library_solution(output_solver_five.adj_matrix)
        # post_time_ip_five = time.time()
        # solving_time_ip_five = post_time_ip_five - pre_time_ip_five
        # self.assertIsNotNone(output_ip_five)
        # score_ip_five = scoreSolution(self.matrix_input_brute_force_five, output_ip_five)
        # file_string_five = "Ip Approximation, |V| = 25: Score = %.4f, Time = %.4f\n" % (score_ip_five, solving_time_ip_five)
        # self.benchmark_file.write(file_string_five)

    def test_benchmark_feedback_arc_set_eades(self):
        # |V| = 4
        pre_time_eades_one = time.time()
        output_solver_one = FinalSolver(self.matrix_input_brute_force_two)
        output_eades_one = output_solver_one.obtain_library_solution(output_solver_one.adj_matrix, force_eades=True)
        post_time_eades_one = time.time()
        solving_time_eades_one = post_time_eades_one - pre_time_eades_one
        self.assertIsNotNone(output_eades_one)
        score_eades_one = scoreSolution(self.matrix_input_brute_force_two, output_eades_one)
        file_string_one = "Eades Approximation, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_eades_one, solving_time_eades_one)
        self.benchmark_file.write(file_string_one)

        # |V| = 25
        pre_time_eades_two = time.time()
        output_solver_two = FinalSolver(self.matrix_input_brute_force_five)
        output_eades_two = output_solver_two.obtain_library_solution(output_solver_two.adj_matrix)
        post_time_eades_two = time.time()
        solving_time_eades_two = post_time_eades_two - pre_time_eades_two
        self.assertIsNotNone(output_eades_two)
        score_eades_two = scoreSolution(self.matrix_input_brute_force_five, output_eades_two)
        file_string_two = "Eades Approximation, |V| = 25: Score = %.4f, Time = %.4f\n" % (score_eades_two, solving_time_eades_two)
        self.benchmark_file.write(file_string_two)

        # |V| = 100
        pre_time_eades_three = time.time()
        output_solver_three = FinalSolver(self.matrix_input_size_100)
        output_eades_three = output_solver_three.obtain_library_solution(output_solver_three.adj_matrix)
        post_time_eades_three = time.time()
        solving_time_eades_three = post_time_eades_three - pre_time_eades_three
        self.assertIsNotNone(output_eades_three)
        score_eades_three = scoreSolution(self.matrix_input_size_100, output_eades_three)
        file_string_three = "Eades Approximation, |V| = 100: Score = %.4f, Time = %.4f\n" % (score_eades_three, solving_time_eades_three)
        self.benchmark_file.write(file_string_three)

        # |V| = 1000
        pre_time_eades_four = time.time()
        output_solver_four = FinalSolver(self.matrix_input_size_1000)
        output_eades_four = output_solver_four.obtain_library_solution(output_solver_four.adj_matrix)
        post_time_eades_four = time.time()
        solving_time_eades_four = post_time_eades_four - pre_time_eades_four
        self.assertIsNotNone(output_eades_four)
        score_eades_four = scoreSolution(self.matrix_input_size_1000, output_eades_four)
        file_string_four = "Eades Approximation, |V| = 1000: Score = %.4f, Time = %.4f\n" % (score_eades_four, solving_time_eades_four)
        self.benchmark_file.write(file_string_four)

        # |V| = 10000
        # pre_time_eades_five = time.time()
        # output_solver_five = FinalSolver(self.matrix_input_size_10000)
        # output_eades_five = output_solver_five.obtain_library_solution(output_solver_five.adj_matrix)
        # post_time_eades_five = time.time()
        # solving_time_eades_five = post_time_eades_five - pre_time_eades_five
        # self.assertIsNotNone(output_eades_five)
        # score_eades_five = scoreSolution(self.matrix_input_size_10000, output_eades_five)
        # file_string_five = "Eades Approximation, |V| = 10000: Score = %.4f, Time = %.4f\n" % (score_eades_five, solving_time_eades_five)
        # self.benchmark_file.write(file_string_five)

    def test_benchmark_final_solver(self):
        # |V| = 4
        pre_time_final_one = time.time()
        output_final_one = FinalSolver(self.matrix_input_brute_force_two).maximum_acyclic_subgraph()
        post_time_final_one = time.time()
        solving_time_final_one = post_time_final_one - pre_time_final_one
        self.assertIsNotNone(output_final_one)
        score_final_one = scoreSolution(self.matrix_input_brute_force_two, output_final_one)
        file_string_one = "Final Approximation, |V| = 4: Score = %.4f, Time = %.4f\n" % (score_final_one, solving_time_final_one)
        self.benchmark_file.write(file_string_one)

        # |V| = 25
        pre_time_final_two = time.time()
        output_final_two = FinalSolver(self.matrix_input_brute_force_five).maximum_acyclic_subgraph()
        post_time_final_two = time.time()
        solving_time_final_two = post_time_final_two - pre_time_final_two
        self.assertIsNotNone(output_final_two)
        score_final_two = scoreSolution(self.matrix_input_brute_force_five, output_final_two)
        file_string_two = "Final Approximation, |V| = 25: Score = %.4f, Time = %.4f\n" % (score_final_two, solving_time_final_two)
        self.benchmark_file.write(file_string_two)

        # |V| = 100
        pre_time_final_three = time.time()
        output_final_three = FinalSolver(self.matrix_input_size_100).maximum_acyclic_subgraph()
        post_time_final_three = time.time()
        solving_time_final_three = post_time_final_three - pre_time_final_three
        self.assertIsNotNone(output_final_three)
        score_final_three = scoreSolution(self.matrix_input_size_100, output_final_three)
        file_string_three = "Final Approximation, |V| = 100: Score = %.4f, Time = %.4f\n" % (score_final_three, solving_time_final_three)
        self.benchmark_file.write(file_string_three)

        # |V| = 1000
        # pre_time_final_four = time.time()
        # output_final_four = FinalSolver(self.matrix_input_size_1000).maximum_acyclic_subgraph()
        # post_time_final_four = time.time()
        # solving_time_final_four = post_time_final_four - pre_time_final_four
        # self.assertIsNotNone(output_final_four)
        # score_final_four = scoreSolution(self.matrix_input_size_1000, output_final_four)
        # file_string_four = "Final Approximation, |V| = 1000: Score = %.4f, Time = %.4f\n" % (score_final_four, solving_time_final_four)
        # self.benchmark_file.write(file_string_four)

        # |V| = 10000
        # pre_time_final_five = time.time()
        # output_final_five = FinalSolver(self.matrix_input_size_10000).maximum_acyclic_subgraph()
        # post_time_final_five = time.time()
        # solving_time_final_five = post_time_final_five - pre_time_final_five
        # self.assertIsNotNone(output_final_five)
        # score_final_five = scoreSolution(self.matrix_input_size_10000, output_final_five)
        # file_string_five = "Final Approximation, |V| = 10000: Score = %.4f, Time = %.4f\n" % (score_final_five, solving_time_final_five)
        # self.benchmark_file.write(file_string_five)
