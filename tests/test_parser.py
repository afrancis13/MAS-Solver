import unittest

from solver.parser.parser import Parser


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.test_input_one = 'tests/input_files/test_input_one.in'
        self.test_input_two = 'tests/input_files/test_input_two.in'
        self.test_cancer = 'tests/input_files/test_cancer.in'
        self.test_parser_one = Parser(self.test_input_one)
        self.test_parser_two = Parser(self.test_input_two)
        self.test_parser_cancer = Parser(self.test_cancer)

    def test_matrix_generator(self):
        '''
        Tests three input files for a correctly generated matrix.
        The third test checks if the validator is working correctly,
        so we check if a ValueError is appropriately raised.
        '''
        observed_one = self.test_parser_one.generate_matrix()
        observed_two = self.test_parser_two.generate_matrix()
        expected_one = [[0, 0, 1, 0],
                        [0, 0, 0, 1],
                        [0, 1, 0, 1],
                        [1, 0, 0, 0]]
        expected_two = [[0 for i in range(15)] for j in range(15)]

        self.assertEqual(observed_one, expected_one)
        self.assertEqual(observed_two, expected_two)

        with self.assertRaises(ValueError):
            self.test_parser_cancer.generate_matrix()

if __name__ == '__main__':
    unittest.main()