def adjacency_matrix_to_file(adj_matrix, file_string):
    string_adj_matrix = [
        [str(adj_matrix[i][j]) for j in range(len(adj_matrix))]
        for i in range(len(adj_matrix))
    ]
    with open(file_string, 'w') as target:
        for line in string_adj_matrix:
            formatted_line = ' '.join(line)
            target.write(formatted_line + '\n')
