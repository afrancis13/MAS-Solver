import os

from random import randint
from file_utils import adjacency_matrix_to_file


SIZES_TO_GENERATE = [100, 1000, 10000]
DENSITIES = [30, 30, 30, 30, 30]


def generate_random_graph():
    for size_index in range(len(SIZES_TO_GENERATE)):
        size = SIZES_TO_GENERATE[size_index]
        adjacency_matrix = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                random_density = randint(1, 100)
                if random_density % 100 < DENSITIES[size_index]:
                    adjacency_matrix[i][j] = 1

        file_string = '../../tests/input_files/test_random_graph_size_%d' % size
        file_path = os.path.abspath(file_string)
        adjacency_matrix_to_file(adjacency_matrix, file_path)

generate_random_graph()
