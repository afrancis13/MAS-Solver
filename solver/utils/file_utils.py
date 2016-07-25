def adjacency_matrix_to_file(adj_matrix, file_string):
    string_adj_matrix = [
        [str(adj_matrix[i][j]) for j in range(len(adj_matrix))]
        for i in range(len(adj_matrix))
    ]
    with open(file_string, 'w+') as target:
        target.write(str(len(adj_matrix)) + '\n')
        for i in range(len(string_adj_matrix)):
            line = string_adj_matrix[i]
            formatted_line = ' '.join(line)
            if i != len(string_adj_matrix) - 1:
                target.write(formatted_line + '\n')
            else:
                target.write(formatted_line)
