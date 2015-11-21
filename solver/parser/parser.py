from solver.staff.instance_validator import processInput


class Parser(object):
    """
    Parses an input file, making use of the validator document
    provided by the CS170 Course Staff. Use the generate_matrix
    function to dump the file data into a matrix (in Python,
    just nested lists).
    """
    def __init__(self, input_file):
        self.input_file = input_file

    def generate_matrix(self):
        if processInput(self.input_file) != 'instance ok':
            raise ValueError('Invalid instance file.')
        else:
            it = 0
            with open(self.input_file, 'r') as fp:
                for line in fp:
                    if it == 0:
                        vertex_count = line
                        matrix = [[None for i in range(vertex_count)] for j in range(vertex_count)]
                    else:
                        edges = line.split(' ')
                        for p in range(vertex_count):
                            matrix[it - 1][p] = edges[p]
                    it += 1

        return matrix
