import random

from solver.parser.parser import Parser
from solver.general.final_solver import FinalSolver
from solver.staff.solutions_validator import processTest 

num_instance_files = 1
output_file 	   = open('./solutions/solutions.out', 'a')
instance_uri 	   = './instances/'


def main():
	for i in range(1, num_instance_files + 1):
		try:
			print "Currently analyzing input file " + str(i) + ".in"
			current_instance = instance_uri + str(i) + '.in'
			current_matrix   = Parser(current_instance).generate_matrix()
			print "Got past parsing"
			current_solution = FinalSolver(current_matrix).maximum_acyclic_subgraph()
			fixed_solution = []
			for item in current_solution:
				fixed_solution.append(item+1)
			print "Got past final solver"
			solution = ''

			for j in range(0, len(current_solution) - 1):
				solution += (str(current_solution[j]+1) + ' ')

			solution += str(current_solution[-1]) + '\n'
			print processTest(fixed_solution,66)
			#if processTest(current_solution, 66) == 'solution ok':
			output_file.write(solution)
			# else:

			# 	"Ran into a formatting issue with the solution for input file " + str(i) + ".in"
			# 	continue 
		except: 
			print "Ran into issue with input file " + str(i) + ".in"
			continue 

main()