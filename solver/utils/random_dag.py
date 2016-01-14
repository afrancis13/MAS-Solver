import os

from random import randint
from file_utils import adjacency_matrix_to_file


SIZES_TO_GENERATE = [100000]
MIN_PER_RANK = 1
MAX_PER_RANK = 5
DENSITY = 30


def generate_random_dag():
    for size in SIZES_TO_GENERATE:
        adjacency_matrix = [[0 for i in range(size)] for j in range(size)]
        nodes = 0
        while nodes < size:
            random_new_nodes = randint(0, MAX_PER_RANK - MIN_PER_RANK)
            new_nodes = MIN_PER_RANK + random_new_nodes
            for i in range(nodes):
                for j in range(new_nodes):
                    random_density = randint(1, 100)
                    if random_density % 100 < DENSITY and j + nodes < size:
                        adjacency_matrix[i][j + nodes] = 1
            nodes += new_nodes

        file_string = '../../tests/input_files/test_random_dag_size_%d' % size
        file_path = os.path.abspath(file_string)
        adjacency_matrix_to_file(adjacency_matrix, file_path)

generate_random_dag()
