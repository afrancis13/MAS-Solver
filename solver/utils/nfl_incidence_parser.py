import os
import requests
import pickle

from bs4 import BeautifulSoup

from file_utils import adjacency_matrix_to_file

url = 'http://espn.go.com/nfl/schedulegrid/_/year/2015'

req = requests.get(url)
data = req.text
soup = BeautifulSoup(data)

team_index_mapping = {}
team_index_counter = 0

for row in soup.find_all('tr')[2:]:

    element_index = 0
    row_team = None

    for el in row.find_all('td'):

        raw_element = el.text.strip('@')

        if raw_element == 'BYE':
            continue

        if raw_element not in team_index_mapping:
            team_index_mapping[raw_element] = {}
            team_index_mapping[raw_element]['team_index'] = team_index_counter
            team_index_mapping[raw_element]['incidence'] = [0 for _ in range(32)]
            team_index_counter += 1

        if element_index == 0:
            row_team = raw_element

        else:
            indicidence_index = team_index_mapping[raw_element]['team_index']
            boxscore_url = 'http://espn.go.com%s' % el.a['href']
            boxscore_req = requests.get(boxscore_url)
            boxscore_data = boxscore_req.text
            boxscore_soup = BeautifulSoup(boxscore_data)
            game_score = boxscore_soup.find_all('td', {'class': 'final-score'})

            # Check if score for row_team is first in list or not.
            if '@' in el.text:
                row_team_score, opponent_score = game_score
            else:
                opponent_score, row_team_score = game_score

            if int(row_team_score.text) > int(opponent_score.text):
                team_index_mapping[row_team]['incidence'][indicidence_index] = 1

        element_index += 1

    print 'Finished parsing incidence matrix for %s' % row_team

final_incidence_matrix = [[0 for i in range(32)] for j in range(32)]
for team in team_index_mapping:
    team_index = team_index_mapping[team]['team_index']
    final_incidence_matrix[team_index] = team_index_mapping[team]['incidence']

file_string = '../../tests/input_files/test_nfl_2015.in'
file_path = os.path.abspath(file_string)
adjacency_matrix_to_file(final_incidence_matrix, file_path)

pickle.dump(team_index_mapping, open('../../tests/input_files/nfl_data_structure', 'wb'), protocol=0)
