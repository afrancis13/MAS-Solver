# import unittest

# from solver.parser.parser import Parser
# from solver.planar.planar_solver import PlanarSolver
# from solver.planar.planar_solver import PlanarSolver


# class PlanarTest(unittest.TestCase):
#     '''
#     Write the class.
#     '''
#     def setUp(self):
#         self.test_input_one = 'tests/input_files/test_large_planar.in'
#         self.test_input_two = 'tests/input_files/test_input_dag_one.in'
#         self.test_input_np_one = 'tests/input_files/test_nonplanar_one.in'
#         self.test_input_np_two = 'tests/input_files/test_nonplanar_two.in'

#         self.matrix_input_one = Parser(self.test_input_one).generate_matrix()
#         self.matrix_input_two = Parser(self.test_input_two).generate_matrix()
#         self.matrix_np_input_one = Parser(self.test_input_np_one).generate_matrix()
#         self.matrix_np_input_two = Parser(self.test_input_np_two).generate_matrix()

#     def test_is_planar(self):
#         self.assertEqual(PlanarSolver(self.matrix_input_one).is_planar, True)
#         self.assertEqual(PlanarSolver(self.matrix_input_two).is_planar, True)
#         self.assertEqual(PlanarSolver(self.matrix_np_input_one).is_planar, False)
#         self.assertEqual(PlanarSolver(self.matrix_np_input_two).is_planar, False)


#     def test_planar_solver(self):
#         pass

# if __name__ == '__main__':
#     unittest.main()
