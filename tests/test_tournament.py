import unittest
import pickle

from solver.parser.parser import Parser
from solver.general.final_solver import FinalSolver
from solver.staff.scorer_single import scoreSolution


class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.test_input_nfl = 'tests/input_files/test_nfl_2015.in'
        self.test_matrix_nfl = Parser(self.test_input_nfl).generate_matrix()

    def test_tournament_nfl(self):
        '''
        Tests three input files for a correctly generated matrix.
        The third test checks if the validator is working correctly,
        so we check if a ValueError is appropriately raised.
        '''
        observed_output_nfl = FinalSolver(self.test_matrix_nfl).maximum_acyclic_subgraph()
        team_index_mapping = pickle.load(open('tests/input_files/nfl_data_structure', 'rb'))

        observed_score_nfl = scoreSolution(self.test_matrix_nfl, observed_output_nfl)
        print 'Score on 2015 NFL season: %d' % observed_score_nfl

        ranked_teams = []
        for team in team_index_mapping:
            team_rank = observed_output_nfl.index(team_index_mapping[team]['team_index'])
            ranked_teams.append((team, team_rank))

        sorted_ranked_teams = sorted(ranked_teams, key=lambda x: x[1])
        for sorted_team in sorted_ranked_teams:
            name, rank = sorted_team[0], sorted_team[1]
            print 'Rank %d: %s' % (rank + 1, name)

if __name__ == '__main__':
    unittest.main()
