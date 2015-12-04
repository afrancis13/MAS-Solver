import random

from solver.parser.parser import Parser
from solver.general.final_solver import FinalSolver

num_instance_files = 100
output_file 	   = open('./solutions/solutions.out', 'a')
instance_uri 	   = './instances/'


def main():
	for i in range(1, num_instance_files + 1):
		current_instance = instance_uri + str(i) + '.in'
		current_matrix   = Parser(current_instance).generate_matrix()
		current_solution = FinalSolver(current_matrix).maximum_acyclic_subgraph()

		for j in range(0, len(current_solution) - 1):
			output_file.write(str(current_solution[j]) + ' ')

		output_file.write(str(current_solution[-1]) + '\n')

main()